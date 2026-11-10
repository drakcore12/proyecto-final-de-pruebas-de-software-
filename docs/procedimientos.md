# Procedimientos, datos y entorno

## AMB-01: entorno

HTTPS a https://dummyjson.com; Python 3.10+ para automatización y cliente HTTP para manuales. Entorno real de ejecución: Linux-6.18.57-x86_64-with-glibc2.39; Python 3.12.14, cliente urllib de biblioteca estándar; fecha 09/11/2026, America/Bogota. El commit no estaba registrado durante las corridas; se conservan hashes de los scripts y evidencia original sin inventar un commit retroactivo. El cliente no debe reutilizar cookies de sesiones anteriores. Registrar problemas de red sin convertirlos en defectos funcionales automáticamente.

## Datos

| ID | Contenido | Preparación / reinicio |
|---|---|---|
| DAT-01 | Producto 1, título de línea base y marcador UUID | Obtener GET antes de cada escritura; no fijar título ni ID de alta |
| DAT-02 | Credenciales públicas emilys / emilyspass; token y refreshToken | Login por ciclo; mantener tokens solo en memoria o variables locales |
| DAT-03 | JWT firmado de un minuto, exp y reloj sincronizado | Esperar expiración real; no falsificar exp ni editar la firma para simular expiración |
| DAT-04 | Catálogo completo y total N | GET /products?limit=0&skip=0; repetir si cambia el conjunto |
| DAT-05 | Consulta existente y UUID ausente | Obtener título actual y verificar ausencia del marcador |

Las credenciales son las de demostración publicadas por DummyJSON; no se usan cuentas personales. Censurar accessToken, refreshToken, Authorization, Cookie y Set-Cookie en toda evidencia publicada.

## PROC-01: contrato crítico y sesión

Objetivo: R07 y R03. Preparación: AMB-01; DAT-01–03; comprobar disponibilidad y cookies vacías. Secuencia: seis casos automáticos CT-R07-01–03 y CT-R03-01–03; después CT-R03-04 manual con token firmado expirado. Cierre: conservar reporte y respuestas censuradas, borrar variables de sesión, registrar incidencias y revisión independiente. Si un caso depende de un dato no disponible, marcar Bloqueado y explicar; no saltarlo como aprobado.

## PROC-02: ampliación funcional

Objetivo: F-R01–F-R05. Preparación: línea base actual, credenciales de demostración y oráculos revisados. Secuencia: CT-F01-01–04; CT-F02-01–03; CT-F03-01–04; CT-F04-01–02; CT-F05-01–02. Aislar cada prueba negativa y limpiar cookies entre solicitudes. Cierre: capturar evidencias, censurar tokens, registrar resultados por caso y mantener separado el control válido de los casos inválidos.

## PROC-03: categorías

Objetivo: R17*. Preparación: catálogo vigente. Secuencia CT-R17-01 y CT-R17-02. Cierre: guardar respuesta y resultados de estructura/unicidad. Una diferencia estética no documentada no se declara defecto.

## Registro de un caso manual

Para cada caso conservar fecha ISO con zona horaria, ejecutor, commit, método/ruta, datos censurados, HTTP observado, cuerpo relevante, comparación de cada aserción, estado y defecto asociado. No basta una captura del cliente mostrando 200. Para R07 se requieren lecturas independientes antes/después.

## Ejecución asistida de los 18 casos manuales

Se enviaron solicitudes con un cliente HTTP genérico y se inspeccionaron cuerpos, códigos y cálculos de contraste. El documento conserva estos 18 diseños manuales; su ejecución fue asistida por ChatGPT y un conductor de solicitudes, no por interacción humana en Postman. Las seis pruebas automáticas sí ejecutaron aserciones en el script versionado. La revisión independiente no se infiere de la ejecución de los casos.
