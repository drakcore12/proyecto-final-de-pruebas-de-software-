# Informe de ejecución y cierre de DummyJSON

**Fecha:** 9 de noviembre de 2026, America/Bogota. **Autores académicos:** Miguel Ángel Noreña Cano, Marlon Maldonado y Aldair Estiven Novoa. **Ejecución y análisis:** mediante herramientas de prueba e inspección HTTP asistida. No se emite una aprobación académica por los resultados del proceso.

## Resultado

| Métrica | Resultado |
|---|---:|
| Casos planificados | 24 |
| Casos ejecutados con evidencia | 24 |
| Aprobados | 23 |
| Fallidos | 1 |
| Bloqueados al consolidar el último resultado | 0 |
| No ejecutados | 0 |
| Ejecución | 100 % |
| Aprobación | 95,83 % |
| Casos P1 aprobados | 6 de 7 (85,71 %) |
| Riesgos altos/críticos con diseño y ejecución completa | 5 de 5 (100 %) |
| Riesgos altos/críticos con todos sus casos aprobados | 4 de 5 (80 %) |
| Incidencias abiertas | 1, severidad media propuesta |

Cobertura de ejecución no equivale a mitigación total. El riesgo R03 conserva una desviación en CT-R03-03. No se midió cobertura interna de código, carga, disponibilidad prolongada ni seguridad profunda.

## Hallazgos comprobados

Las escrituras se comportan como simulaciones: alta con 201 sin recurso persistido, modificación con 200 sin cambio en el GET posterior y borrado con marcadores de simulación sin eliminar el recurso. El login válido permite consultar el perfil; ausencia y expiración del token reciben 401. El token expirado se consultó 42,14 segundos después de exp, con un control previo satisfactorio.

Credenciales inválidas y vacías recibieron 400. Refresh ausente recibió 401 y refresh alterado 403; el refresh válido permitió consultar el mismo usuario. El catálogo observado contenía 194 productos y 24 categorías. Se verificaron los límites de paginación y las dos clases de búsqueda; esos conteos son línea base de esta fecha, no constantes del servicio.

[INC-001](INC-001.md): la firma alterada del accessToken recibe 500 con invalid signature. Se reprodujo en dos solicitudes y no devolvió perfil. La clasificación inicial Bloqueado del ejecutor se corrigió y el caso se repitió, conservando la evidencia previa.

## Evidencias y método

[Registro completo por caso](registro-ejecucion.md). Cada JSON conserva método, ruta, datos censurados, estado HTTP y cuerpo. Los reportes de las seis pruebas automáticas contienen aserciones y resultado; las 18 inspecciones HTTP asistidas conservan observaciones evaluadas por caso. No se atribuye una ejecución manual humana ni se inventan firmas de revisión.

El script inicial y el corregido se conservan. El directorio de evidencias incluye un índice y hashes SHA-256 para verificar integridad. Los tokens y contraseñas se censuran; no se publican Authorization ni cookies.

## Decisión de cierre

**Se cierra la ejecución documental con un hallazgo abierto. No se emite aceptación satisfactoria del producto bajo la puerta P1 definida**, porque uno de sus siete casos falla. Que la API sea simulada no justifica cambiar el resultado esperado para aprobar el caso.

La entrega documenta resultados reales y puede presentarse como informe de pruebas con defectos. La reparación del proveedor y un futuro retest son trabajo externo pendiente. La evaluación académica corresponde al docente.

## Restricciones académicas y de calendario

Miguel confirmó tres integrantes. La guía propone cuatro; se declara la adaptación a tres personas, ocho casos por integrante y 72 horas-persona planificadas. La diferencia se documenta como adaptación del escenario de la guía. El cronograma presenta tres semanas relativas; los registros conservan la fecha y hora reales de cada prueba.

El paquete incluye control de versiones local. No se ha publicado en un repositorio remoto GitHub ni se inventa una URL de release.
