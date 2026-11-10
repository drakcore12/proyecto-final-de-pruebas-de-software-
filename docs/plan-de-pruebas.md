# Plan de pruebas esencial - API DummyJSON

# 1. Información específica del documento

| Campo | Registro |
| --- | --- |
| ID / versión / emisión | PP-DUMMYJSON-FINAL-01 / 2.1, publicación / 10 de noviembre de 2026 |
| Organización y autores | I. U. Pascual Bravo. Miguel Ángel Noreña Cano, Marlon Maldonado y Aldair Estiven Novoa. |
| Autoridad de aprobación | Docente de Pruebas de Software. No se atribuye una aprobación emitida. |
| Control de cambios | 1.1: expediente de ejecución. 2.0: síntesis sin cambios en las respuestas ni en los 24 resultados. Base local: tag v1.1.0-entrega; publicación en GitHub incorporada el 10 de noviembre de 2026 (versión 2.1). |

# 2. Introducción y adaptación (tailoring)

Objetivo: verificar el contrato observable de autenticación y productos, priorizando los fallos de sesión y la interpretación de escrituras simuladas. Se aplica una adaptación académica de la documentación basada en ISO/IEC/IEEE 29119-3. No se declara conformidad integral.

| Exclusión / adaptación | Justificación y riesgo residual |
| --- | --- |
| Unitarias, caja blanca y base de datos | Sin instrumentación del servicio externo. Quedan defectos internos sin evaluar. |
| Carga y seguridad profunda | Ventana de tres semanas y servicio compartido. Capacidad y vulnerabilidades fuera del alcance no determinadas. |
| Interfaz y pruebas visuales | El objeto es una API sin cliente propio. No se concluye sobre UX ni accesibilidad. |
| Tres integrantes y documentos agrupados | Equipo real de tres personas frente a cuatro en la guía. Ocho casos por persona; se conservan las relaciones y evidencias en Markdown. |

Glosario mínimo: RBT = pruebas basadas en riesgos; condición = regla evaluable; oráculo = criterio esperado; retest = repetir después de una corrección.

# 3. Contexto de las pruebas

Elementos: https://dummyjson.com; /auth/login, /auth/me, /auth/refresh, /products, /products/{id}, /products/add, /products/search y /products/categories. Incluye login, tokens, refresh, consulta, categorías, búsqueda, paginación y POST/PATCH/DELETE simulados. Excluye carritos, recetas, publicaciones, pagos y las actividades de la sección 2.

Supuestos: datos y contrato pueden cambiar; se captura una línea base por ciclo. Restricciones: sin acceso interno ni reparación del proveedor. Partes interesadas: tres integrantes, docente y proveedor externo. Usuario = cuenta ficticia autenticada; cliente HTTP = herramienta que envía solicitudes.



# 4. Gestión de riesgos y exposición

E = P x I, con probabilidad e impacto de 1 a 5. Bajo 1-4; medio 5-9; alto 10-14; crítico 15-25. Son valoraciones de planificación. Se conservan R07, R03 y R17* del Taller 4; F- y FP- distinguen las ampliaciones de producto y proyecto.

| ID | Riesgo | P x I / nivel | Tratamiento |
| --- | --- | --- | --- |
| R07 | Confundir escritura simulada con persistencia | 4 x 4 = 16 Crítico | CT-R07-01 a 03: contraste antes/después. |
| R03 | Acceso con sesión ausente, alterada o expirada | 3 x 5 = 15 Crítico | CT-R03-01 a 04: cuatro clases de sesión. |
| F-R01 | Credenciales aceptadas incorrectamente | 3 x 4 = 12 Alto | CT-F01-01 a 04. |
| F-R02 | Renovación de sesión indebida o inutilizable | 3 x 4 = 12 Alto | CT-F02-01 a 03. |
| F-R03 | Omisión o duplicación en paginación | 3 x 4 = 12 Alto | CT-F03-01 a 04. |
| F-R04 | Confundir recurso existente e inexistente | 2 x 3 = 6 Medio | Dos clases por dependencia de consultas. |
| F-R05 | Búsqueda incorrecta | 2 x 3 = 6 Medio | Dos clases por bajo costo y uso frecuente. |
| R17* | Inconsistencias menores en categorías | 2 x 2 = 4 Bajo | Dos controles históricos complementarios; aceptar riesgo residual de catálogo. |
| F-R06 | Capacidad y rendimiento no determinados | 2 x 4 = 8 Medio | Aceptar riesgo residual: no se somete el servicio externo a carga. |
| FP-01 | Caída o cambio del servicio | 3 x 4 = 12 Alto | Línea base, control previo, bloqueo y reprogramación. |
| FP-02 | Retraso del proyecto | 3 x 4 = 12 Alto | 72 h-persona e hitos semanales. |
| FP-03 | Publicación de tokens | 2 x 4 = 8 Medio | Censura y comprobación de evidencias. |
| FP-04 | Diferencia de equipo respecto a la guía | 3 x 4 = 12 Alto | Tres responsables reales; adaptación explícita de cuatro a tres. |

Tratamiento: todo riesgo de producto alto o crítico exige diseño y ejecución con evidencia. Los medios se prueban cuando hay justificación o se aceptan con alcance explícito. Los bajos pueden aceptarse. Los riesgos de proyecto se tratan con controles de gestión, sin inventar casos funcionales.

Cobertura: los cinco riesgos altos/críticos de producto tienen casos y ejecución completa. R03 conserva INC-001 abierto. Ejecutar todas las pruebas no equivale a mitigar todos los riesgos. F-R06 es una declaración adicional del riesgo residual de carga excluida, sin resultados inventados.



# 5. Estrategia, casos y trazabilidad

La relación se mantiene en ambos sentidos: riesgo - condición - técnica - caso - evidencia. Las fichas completas, pasos, precondiciones y resultados esperados permanecen en el anexo docs/casos-y-trazabilidad.md. Los seis casos automáticos enlazan a tests/pruebas_api.py.

| Caso | Riesgo / condición | Técnica | Dato derivado |
| --- | --- | --- | --- |
| CT-R07-01 | R07 / C07-01 | T3 + T4 | POST con título UUID y GET del ID devuelto |
| CT-R07-02 | R07 / C07-02 | T3 + T4 | GET / PATCH / GET; título UUID distinto |
| CT-R07-03 | R07 / C07-03 | T3 + T4 | GET / DELETE / GET; mismo recurso |
| CT-R03-01 | R03 / C03-01 | T1 | JWT válido recién emitido |
| CT-R03-02 | R03 / C03-02 | T1 | Sin Authorization y sin cookies |
| CT-R03-03 | R03 / C03-03 | T1 | Primer carácter de la firma alterado |
| CT-R03-04 | R03 / C03-04 | T3 | Mismo JWT: t < exp y t > exp + 5 s |
| CT-R17-01 | R17* / C17-01 | T1 | Cadenas no vacías |
| CT-R17-02 | R17* / C17-02 | T1 | Slug único y ruta URL correspondiente |
| CT-F01-01 | F-R01 / CF01-1 | T1 | Usuario y contraseña válidos |
| CT-F01-02 | F-R01 / CF01-2 | T1 | Usuario válido; contraseña incorrecta |
| CT-F01-03 | F-R01 / CF01-3 | T1 | Usuario inexistente; contraseña de control |
| CT-F01-04 | F-R01 / CF01-4 | T1 | Usuario y contraseña vacíos |
| CT-F02-01 | F-R02 / CF02-1 | T1 + T3 | Refresh válido |
| CT-F02-02 | F-R02 / CF02-2 | T1 + T3 | Refresh ausente, sin cookies |
| CT-F02-03 | F-R02 / CF02-3 | T1 + T3 | Firma del refresh alterada |
| CT-F03-01 | F-R03 / CF03-1 | T2 | limit=1; skip=0 |
| CT-F03-02 | F-R03 / CF03-2 | T2 | limit=1; skip=N-1 |
| CT-F03-03 | F-R03 / CF03-3 | T2 | limit=1; skip=N |
| CT-F03-04 | F-R03 / CF03-4 | T1 | limit=0: clase especial documentada |
| CT-F04-01 | F-R04 / CF04-1 | T1 | ID existente |
| CT-F04-02 | F-R04 / CF04-2 | T1 | max(ID) + 100000, ausente de línea base |
| CT-F05-01 | F-R05 / CF05-1 | T1 | Título conocido |
| CT-F05-02 | F-R05 / CF05-2 | T1 | Consulta UUID sin coincidencias |

T1: partición de equivalencia. T2: valores límite. T3: transición de estados. T4: tabla de decisión POST/PATCH/DELETE. N se obtiene del total observado; limit=0 es una clase especial, no un valor inválido. Cada caso del anexo identifica precondiciones, pasos o script y oráculo.

Volumen: 24 casos, seis automatizados y 18 diseños manuales ejecutados mediante inspección HTTP asistida. No se atribuye una ejecución manual humana ni una aprobación independiente no realizada.



# 5.4 Entorno y datos de prueba

Python 3.10 o posterior y cliente HTTP por HTTPS. Entorno utilizado: Linux y urllib, sin CookieJar. Credenciales públicas de demostración: emilys / emilyspass. Tokens solo en variables temporales; se censuran en evidencias. Registrar fecha, versión y línea base del ciclo.

| Dato | Preparación |
| --- | --- |
| Productos y categorías | Leer catálogo y producto 1; capturar N, IDs y orden. Usar títulos UUID. |
| Autenticación y refresh | Emitir tokens auténticos. Cambiar únicamente la firma en casos negativos. |
| Expiración | Solicitar un JWT firmado de un minuto. Comparar antes y después de exp; no editar el payload para simular expiración. |
| Búsqueda | Título actual conocido y UUID verificado como ausente de la línea base. |

# 5.5 Criterios de entrada, suspensión y cierre

Entrada: alcance, datos, oráculos y servicio disponibles. Suspensión: indisponibilidad, cambio de contrato, datos insuficientes o riesgo de publicar tokens. Reanudación: resolver la causa y ejecutar un control previo. Cierre satisfactorio: 24 casos con evidencia, todos los P1 aprobados, cero defectos críticos/altos abiertos y revisión independiente registrada. El caso P1 fallido impide ese dictamen.

# 6. Actividades y estimación

| ID | Actividad | Horas-persona | Dependencia |
| --- | --- | --- | --- |
| T1 | Alcance, referencias, riesgos y adaptación | 6 | Inicio |
| T2 | Entorno, datos y línea base | 4 | T1 |
| T3 | Diseño de 24 casos y trazabilidad | 14 | T1 |
| T4 | Seis automatizaciones y depuración | 14 | T2 / T3 parcial |
| T5 | Ejecución y registro de incidentes | 14 | T2 / T3 / T4 |
| T6 | Retest y regresión según hallazgos | 6 | T5 |
| T7 | Revisión y correcciones documentales | 6 | T3 / T5 |
| T8 | Informe y sustentación | 8 | T6 / T7 |
| Total | Capacidad planificada | 72 | 3 personas x 8 h/semana x 3 semanas |

Estimación académica de esfuerzo, sin incluir reparaciones del proveedor. No se afirma que las 72 horas hayan transcurrido durante las solicitudes asistidas.

# 7. Personal y responsabilidades

| Integrante | Rol | Casos |
| --- | --- | --- |
| Miguel Ángel Noreña Cano | Gestión: alcance, adaptación y riesgos | 1-8 |
| Marlon Maldonado | Análisis: condiciones, datos y trazabilidad | 9-16 |
| Aldair Estiven Novoa | Automatización, ejecución y evidencias | 17-24 |

La revisión propuesta se cruza: Marlon revisa 1-8; Aldair, 9-16; Miguel, 17-24. No se añaden firmas de revisiones no realizadas.



# 8. Cronograma de tres semanas

| Semana / fecha relativa | Actividades | Hito / carga |
| --- | --- | --- |
| 1 / días 1-7 | T1 6 h + T2 4 h + T3 14 h | Diseño y riesgos / 24 h |
| 2 / días 8-14 | T4 14 h + T5 10 h | Scripts y primera ejecución / 24 h |
| 3 / días 15-21 | T5 4 h + T6 6 h + T7 6 h + T8 8 h | Retest e informe / 24 h |

Las fechas son relativas a la ventana académica; no se inventa una fecha oficial de inicio o vencimiento. Emisión del informe y ejecución observada: 9 de noviembre de 2026.

# Resultado de ejecución y decisión de cierre

| Indicador | Resultado |
| --- | --- |
| Planificados / ejecutados | 24 / 24 |
| Aprobados / fallidos / bloqueados / no ejecutados | 23 / 1 / 0 / 0 |
| Aprobación / casos P1 aprobados | 95,83 % / 6 de 7 |
| Riesgos altos/críticos con ejecución completa | 5 de 5 |
| Riesgos altos/críticos con todos sus casos aprobados | 4 de 5 |

## INC-001 - CT-R03-03: firma JWT alterada

Esperado: 401 o 403, sin perfil. Observado dos veces: 500 con {"message":"invalid signature"}, sin acceso al perfil. La primera clasificación de bloqueo del cliente se corrigió y el retest confirmó el fallo. No se cambió el oráculo para aprobarlo. Severidad propuesta media; prioridad alta por afectar P1.

Dictamen: ejecución y documentación completas con un hallazgo abierto. No se emite aceptación satisfactoria del producto bajo P1. No se concluye sobre carga, cobertura interna o seguridad profunda. Las escrituras sin persistencia son comportamiento documentado del servicio.

# Evidencias y anexos obligatorios

docs/casos-y-trazabilidad.md: las 24 fichas y sus técnicas. tests/pruebas_api.py: seis automatizaciones. evidencias/: registros por caso, capturas originales y resultados. docs/INC-001.md: incidente y retest. El PDF esencial y las diapositivas no sustituyen estos anexos. El repositorio público conserva documentos, código y evidencias. Su historial de commits y sus Issues permiten registrar el seguimiento desde la publicación del 10 de noviembre de 2026. No se atribuye historial remoto previo.

# Referencias

Guía Plan de Pruebas de Software ISO 29119-3 y contenidoPlan.txt, suministrados por la asignatura. CasosDePruebas.pdf y Software_Testing_Fundamentals.pdf. Taller 4, API DummyJSON, 15/10/2026. Enunciado del Taller 5. Documentación oficial consultada para los oráculos: https://dummyjson.com/docs/auth y https://dummyjson.com/docs/products.
