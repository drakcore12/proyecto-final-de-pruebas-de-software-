# Registro de ejecución de DummyJSON

**Fecha:** 9 de noviembre de 2026. Zona horaria: America/Bogota. Ejecutor: ChatGPT mediante herramientas HTTP. Responsables académicos: Miguel Ángel Noreña Cano, Marlon Maldonado y Aldair Estiven Novoa. La columna de responsable no implica que esa persona haya ejecutado o aprobado el caso.

| Caso / riesgo | Estado / modalidad | Hora Bogotá | Resultado observado | Evidencia |
|---|---|---|---|---|
| CT-R07-01 / R07 | Aprobado / Automatizada | 09:59:01 | POST 201 con ID 195 y título UUID; GET /products/195 = 404. | [auto-20261109T145901-d128c7a2.json](../evidencias/auto-20261109T145901-d128c7a2.json) |
| CT-R07-02 / R07 | Aprobado / Automatizada | 09:59:01 | PATCH 200 refleja título temporal; GET conserva el título original. | [auto-20261109T145901-d128c7a2.json](../evidencias/auto-20261109T145901-d128c7a2.json) |
| CT-R07-03 / R07 | Aprobado / Automatizada | 09:59:01 | DELETE 200 con isDeleted=true y deletedOn; GET posterior = 200. | [auto-20261109T145901-d128c7a2.json](../evidencias/auto-20261109T145901-d128c7a2.json) |
| CT-R03-01 / R03 | Aprobado / Automatizada | 09:59:01 | Login 200; /auth/me 200 con id=1 y username=emilys. | [auto-20261109T145901-d128c7a2.json](../evidencias/auto-20261109T145901-d128c7a2.json) |
| CT-R03-02 / R03 | Aprobado / Automatizada | 09:59:01 | GET sin token = 401, Access Token is required; sin perfil. | [auto-20261109T145901-d128c7a2.json](../evidencias/auto-20261109T145901-d128c7a2.json) |
| CT-R03-03 / R03 | Fallido / Automatizada | 10:02:07 | Dos respuestas HTTP 500, invalid signature; sin perfil. Se esperaba 401/403. | [auto-20261109T150207-bbd30c6d.json](../evidencias/auto-20261109T150207-bbd30c6d.json) |
| CT-R03-04 / R03 | Aprobado / Inspección HTTP asistida | 10:04:40 | Control previo 200; token expirado consultado 42,14 s después de exp: 401 Token Expired!, sin perfil. | [manual-20261109T150248-CT-R03-04.json](../evidencias/manual-20261109T150248-CT-R03-04.json) |
| CT-R17-01 / R17* | Aprobado / Inspección HTTP asistida | 10:03:04 | 200; 24 categorías; slug, name y url son cadenas no vacías. | [manual-20261109T150248-CT-R17-01.json](../evidencias/manual-20261109T150248-CT-R17-01.json) |
| CT-R17-02 / R17* | Aprobado / Inspección HTTP asistida | 10:03:08 | 200; slugs únicos y cero diferencias entre slug y ruta de url. | [manual-20261109T150248-CT-R17-02.json](../evidencias/manual-20261109T150248-CT-R17-02.json) |
| CT-F01-01 / F-R01 | Aprobado / Inspección HTTP asistida | 10:03:13 | 200; usuario emilys; accessToken y refreshToken presentes. | [manual-20261109T150248-CT-F01-01.json](../evidencias/manual-20261109T150248-CT-F01-01.json) |
| CT-F01-02 / F-R01 | Aprobado / Inspección HTTP asistida | 10:03:18 | 400 Invalid credentials; sin tokens. | [manual-20261109T150248-CT-F01-02.json](../evidencias/manual-20261109T150248-CT-F01-02.json) |
| CT-F01-03 / F-R01 | Aprobado / Inspección HTTP asistida | 10:03:22 | 400 Invalid credentials; sin tokens. | [manual-20261109T150248-CT-F01-03.json](../evidencias/manual-20261109T150248-CT-F01-03.json) |
| CT-F01-04 / F-R01 | Aprobado / Inspección HTTP asistida | 10:03:26 | 400 Username and password required; sin tokens. | [manual-20261109T150248-CT-F01-04.json](../evidencias/manual-20261109T150248-CT-F01-04.json) |
| CT-F02-01 / F-R02 | Aprobado / Inspección HTTP asistida | 10:03:39 | Refresh 200 con tokens; /auth/me 200 para emilys. | [manual-20261109T150248-CT-F02-01.json](../evidencias/manual-20261109T150248-CT-F02-01.json) |
| CT-F02-02 / F-R02 | Aprobado / Inspección HTTP asistida | 10:03:43 | 401 Refresh token required; sin tokens. | [manual-20261109T150248-CT-F02-02.json](../evidencias/manual-20261109T150248-CT-F02-02.json) |
| CT-F02-03 / F-R02 | Aprobado / Inspección HTTP asistida | 10:03:53 | 403 Invalid refresh token; sin tokens. | [manual-20261109T150248-CT-F02-03.json](../evidencias/manual-20261109T150248-CT-F02-03.json) |
| CT-F03-01 / F-R03 | Aprobado / Inspección HTTP asistida | 10:04:02 | N=194; skip=0, limit=1 devuelve ID 1 y total=194. | [manual-20261109T150248-CT-F03-01.json](../evidencias/manual-20261109T150248-CT-F03-01.json) |
| CT-F03-02 / F-R03 | Aprobado / Inspección HTTP asistida | 10:04:06 | skip=193, limit=1 devuelve ID 194, último de línea base. | [manual-20261109T150248-CT-F03-02.json](../evidencias/manual-20261109T150248-CT-F03-02.json) |
| CT-F03-03 / F-R03 | Aprobado / Inspección HTTP asistida | 10:04:11 | skip=194 devuelve arreglo vacío y total=194. | [manual-20261109T150248-CT-F03-03.json](../evidencias/manual-20261109T150248-CT-F03-03.json) |
| CT-F03-04 / F-R03 | Aprobado / Inspección HTTP asistida | 10:04:15 | limit=0 devuelve 194 productos sin IDs duplicados; coincide con línea base. | [manual-20261109T150248-CT-F03-04.json](../evidencias/manual-20261109T150248-CT-F03-04.json) |
| CT-F04-01 / F-R04 | Aprobado / Inspección HTTP asistida | 10:04:19 | GET producto 1 = 200; id=1 y título no vacío. | [manual-20261109T150248-CT-F04-01.json](../evidencias/manual-20261109T150248-CT-F04-01.json) |
| CT-F04-02 / F-R04 | Aprobado / Inspección HTTP asistida | 10:04:24 | GET producto 100194 = 404; mensaje de recurso inexistente. | [manual-20261109T150248-CT-F04-02.json](../evidencias/manual-20261109T150248-CT-F04-02.json) |
| CT-F05-01 / F-R05 | Aprobado / Inspección HTTP asistida | 10:04:30 | Búsqueda por título completo = 200; un resultado, producto 1. | [manual-20261109T150248-CT-F05-01.json](../evidencias/manual-20261109T150248-CT-F05-01.json) |
| CT-F05-02 / F-R05 | Aprobado / Inspección HTTP asistida | 10:04:36 | Búsqueda por UUID ausente = 200; products=[] y total=0. | [manual-20261109T150248-CT-F05-02.json](../evidencias/manual-20261109T150248-CT-F05-02.json) |

## Historial del caso CT-R03-03

La primera corrida clasificó HTTP 500 como Bloqueado por una regla demasiado amplia del ejecutor v0.1. Se conserva el JSON original sin cambiarlo y el código v0.1 en tests/historico. La respuesta era JSON de aplicación (invalid signature), por lo que se corrigió la clasificación del ejecutor y se repitió el caso con el mismo oráculo 401/403. El retest volvió a responder 500 y quedó Fallido. No se relajó la expectativa para obtener una aprobación.

El resto de los cinco casos automáticos conservan el resultado de la primera corrida. Las 18 inspecciones HTTP fueron evaluadas sobre sus respuestas guardadas; no constituyen una revisión humana independiente.
