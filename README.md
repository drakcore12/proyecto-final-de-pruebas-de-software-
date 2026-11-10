# Proyecto final de Pruebas de Software

**Evaluación de la API DummyJSON mediante pruebas basadas en riesgos.**

Miguel Ángel Noreña Cano · Marlon Maldonado · Aldair Estiven Novoa  
Institución Universitaria Pascual Bravo · Pruebas de Software

## Documento y exposición

- [Documento técnico: plan, metodología y resultados](docs/plan-de-pruebas.md).
- [Presentación de 10 minutos, con notas de exposición](https://docs.google.com/presentation/d/1X2_pCfRGfzoN0ow7vTUFBQwWNWM1GYirXDvD3mtE5pU/edit).
- [Carpeta de entrega en Drive](https://drive.google.com/drive/folders/1L5MnloUN0epNl_G1xDRuxmgganr-nLw7).

## Anexos verificables

| Carpeta | Contenido |
| --- | --- |
| [docs](docs) | Plan esencial, 24 casos y trazabilidad, procedimientos, registro de ejecución, cierre, incidencia y referencias. |
| [tests](tests) | Script de seis pruebas automáticas, sin dependencias externas. |
| [evidencias](evidencias) | Registros JSON originales, resultados consolidados y capturas con procedencia. |

## Resultado registrado

El 9 de noviembre de 2026 se ejecutaron **24 casos: 23 aprobados y 1 fallido**. Seis pruebas automatizadas y 18 diseños manuales ejecutados mediante inspección HTTP asistida; no se atribuye interacción humana en Postman ni revisión independiente no realizada.

**INC-001:** firma JWT alterada produce HTTP 500 en dos ejecuciones; se esperaba 401/403 sin perfil. No se observó acceso al perfil. El hallazgo permanece abierto y el criterio de cierre P1 no se cumple. Las escrituras POST/PATCH/DELETE sin persistencia son comportamiento documentado de DummyJSON.

## Reproducir las pruebas

Con Python 3.10 o posterior, desde la raíz:

```bash
python tests/pruebas_api.py
```

Demostración de escritura simulada:

```bash
python tests/pruebas_api.py CT-R07-02
```

Cada ejecución genera un registro nuevo en `evidencias/`. Los datos del servicio pueden cambiar. Las evidencias publicadas son las del ciclo del 9 de noviembre; una ejecución nueva no debe sobrescribirlas. Se utilizan credenciales públicas de demostración; los tokens se censuran.

## Seguimiento del trabajo

Consultar [seguimiento y acuerdos del equipo](docs/seguimiento.md), el historial de commits y las Issues. Cada cambio debe indicar qué se hizo, por qué y qué evidencia lo comprueba. La publicación en GitHub comienza el 10 de noviembre de 2026; no representa actividad remota previa ni firmas de los otros integrantes.
