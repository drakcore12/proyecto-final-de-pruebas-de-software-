"""Seis casos de contrato DummyJSON. Ejecutar con Python 3.10+."""
import json
import os
import socket
import ssl
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE = 'https://dummyjson.com'
USER = os.environ.get('DUMMYJSON_USER', 'emilys')
PASSWORD = os.environ.get('DUMMYJSON_PASSWORD', 'emilyspass')
SENSITIVE = {'password', 'accesstoken', 'refreshtoken', 'authorization', 'cookie', 'set-cookie'}
TRACE = []


class EnvironmentBlocked(Exception):
    pass


def clean(value):
    if isinstance(value, dict):
        return {k: '[CENSURADO]' if k.lower() in SENSITIVE else clean(v) for k, v in value.items()}
    if isinstance(value, list):
        return [clean(v) for v in value]
    return value


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def request(method, path, body=None, token=None):
    headers = {'Accept': 'application/json', 'User-Agent': 'DummyJSON-Academic-Contract-Tests/0.1'}
    data = None
    if body is not None:
        headers['Content-Type'] = 'application/json'
        data = json.dumps(body).encode()
    if token:
        headers['Authorization'] = 'Bearer ' + token
    req = Request(BASE + path, data=data, headers=headers, method=method)
    start = time.monotonic()
    # urlopen no instala un CookieJar: las cookies de login no se reutilizan.
    try:
        with urlopen(req, timeout=20) as response:
            status = response.status
            raw = response.read().decode('utf-8', errors='replace')
    except HTTPError as exc:
        status = exc.code
        raw = exc.read().decode('utf-8', errors='replace')
    except (URLError, TimeoutError, socket.timeout, ssl.SSLError, OSError) as exc:
        # Guardar solo tipo, evitando exponer detalles del proxy o credenciales.
        TRACE.append({'method': method, 'path': path, 'transport_error': type(exc).__name__})
        raise EnvironmentBlocked('No fue posible completar la conexión HTTPS') from exc
    elapsed = round((time.monotonic() - start) * 1000, 2)
    try:
        result = json.loads(raw)
    except json.JSONDecodeError as exc:
        TRACE.append({'method': method, 'path': path, 'status': status, 'duration_ms': elapsed,
                      'response': '[RESPUESTA NO JSON] verificar con cliente HTTP'})
        if status == 429 or status >= 500:
            raise EnvironmentBlocked(f'HTTP {status}; investigar disponibilidad/entorno') from exc
        raise AssertionError(f'HTTP {status}: respuesta no JSON') from exc
    TRACE.append({'method': method, 'path': path, 'request': clean(body), 'status': status,
                  'duration_ms': elapsed, 'response': clean(result)})
    if status == 429:
        raise EnvironmentBlocked(f'HTTP {status}; límite de solicitudes del servicio')
    return status, result


def login():
    status, data = request('POST', '/auth/login', {'username': USER, 'password': PASSWORD})
    require(status == 200, f'Login de preparación: se esperaba 200, observado {status}')
    require(isinstance(data, dict), 'Login debe devolver un objeto')
    require(bool(data.get('accessToken')), 'Falta accessToken en login')
    return data


# CT-R07-01
def alta_simulada():
    title = 'QA-DummyJSON-' + uuid.uuid4().hex
    status, base = request('GET', '/products?limit=0')
    require(status == 200 and isinstance(base, dict), 'No se obtuvo línea base')
    ids = {p['id'] for p in base['products']}
    status, created = request('POST', '/products/add', {'title': title})
    require(status in (200, 201), f'Alta: estado inesperado {status}')
    require(isinstance(created, dict), 'Alta debe devolver objeto')
    require(created.get('title') == title and isinstance(created.get('id'), int), 'Alta simulada incorrecta')
    require(created['id'] not in ids, 'ID simulado colisiona con línea base')
    status, after = request('GET', '/products/' + str(created['id']))
    require(status == 404 and isinstance(after, dict), 'El recurso simulado no debe persistir')


# CT-R07-02
def cambio_simulado():
    status, before = request('GET', '/products/1')
    require(status == 200 and isinstance(before, dict), 'Línea base no disponible')
    title = 'QA-Cambio-' + uuid.uuid4().hex
    status, changed = request('PATCH', '/products/1', {'title': title})
    require(status == 200 and changed.get('title') == title, 'PATCH no refleja simulación')
    status, after = request('GET', '/products/1')
    require(status == 200 and after.get('title') == before.get('title'), 'PATCH persistió o cambió la línea base')


# CT-R07-03
def borrado_simulado():
    status, before = request('GET', '/products/1')
    require(status == 200 and isinstance(before, dict), 'Línea base no disponible')
    status, deleted = request('DELETE', '/products/1')
    require(status == 200 and deleted.get('id') == 1, 'DELETE no devuelve el recurso esperado')
    require(deleted.get('isDeleted') is True and bool(deleted.get('deletedOn')), 'Faltan marcadores de borrado')
    status, after = request('GET', '/products/1')
    require(status == 200 and after.get('id') == 1 and after.get('title') == before.get('title'),
            'El recurso original no se conserva')


# CT-R03-01
def sesion_valida():
    session = login()
    status, profile = request('GET', '/auth/me', token=session['accessToken'])
    require(status == 200 and isinstance(profile, dict), 'Sesión válida rechazada')
    require(profile.get('id') == session.get('id') and profile.get('username') == USER, 'Identidad incorrecta')


# CT-R03-02
def sesion_ausente():
    status, data = request('GET', '/auth/me')
    require(status in (401, 403), f'Se esperaba rechazo 401/403, observado {status}')
    require(isinstance(data, dict) and 'id' not in data and 'email' not in data, 'Respuesta expone perfil')


# CT-R03-03
def sesion_alterada():
    session = login()
    parts = session['accessToken'].split('.')
    require(len(parts) == 3 and bool(parts[2]), 'El token de preparación no tiene firma JWT')
    # Cambiar el primer carácter evita alterar solo bits de relleno de base64url.
    parts[2] = ('A' if parts[2][0] != 'A' else 'B') + parts[2][1:]
    status, data = request('GET', '/auth/me', token='.'.join(parts))
    require(status in (401, 403), f'Se esperaba rechazo 401/403, observado {status}')
    require(isinstance(data, dict) and 'id' not in data and 'email' not in data, 'Respuesta expone perfil')


CASES = [
    ('CT-R07-01', alta_simulada),
    ('CT-R07-02', cambio_simulado),
    ('CT-R07-03', borrado_simulado),
    ('CT-R03-01', sesion_valida),
    ('CT-R03-02', sesion_ausente),
    ('CT-R03-03', sesion_alterada),
]


def main():
    results = []
    selected = sys.argv[1:]
    if selected and not set(selected).issubset({case_id for case_id, _ in CASES}):
        raise SystemExit('ID de caso desconocido')
    for case_id, function in CASES:
        if selected and case_id not in selected:
            continue
        TRACE.clear()
        try:
            function()
            state, note = 'Aprobado', 'Todas las aserciones del caso se cumplieron'
        except EnvironmentBlocked as exc:
            state, note = 'Bloqueado', str(exc)
        except AssertionError as exc:
            state, note = 'Fallido', str(exc)
        except Exception as exc:
            state, note = 'Bloqueado', 'Revisar script/datos: ' + type(exc).__name__
        results.append({'case': case_id, 'state': state, 'note': note, 'evidence': list(TRACE)})
        print(case_id + ': ' + state)
        time.sleep(0.2)
    now = datetime.now(timezone.utc)
    report = {'timestamp': now.isoformat(), 'base_url': BASE, 'python': sys.version,
              'commit': os.environ.get('DUMMYJSON_COMMIT', 'No registrado'), 'results': results}
    folder = Path(__file__).resolve().parents[1] / 'evidencias'
    folder.mkdir(exist_ok=True)
    path = folder / ('auto-' + now.strftime('%Y%m%dT%H%M%S') + '-' + uuid.uuid4().hex[:8] + '.json')
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Reporte: ' + str(path))
    return 0 if all(r['state'] == 'Aprobado' for r in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
