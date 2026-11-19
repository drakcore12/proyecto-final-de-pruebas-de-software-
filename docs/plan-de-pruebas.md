Versión de consulta en Google Docs: https://docs.google.com/document/d/14eZrwDed-F5Lf6CiXBdScSnbSLmlF25YsoXzNlJ_lUc/edit

# Evaluación de la API DummyJSON mediante pruebas basadas en riesgos

Informe final de Pruebas de Software

Miguel Ángel Noreña Cano

Marlon Maldonado

Aldair Estiven Novoa

Institución Universitaria Pascual Bravo

Pruebas de Software

Docente: Roberto José Calderón Bermejo

19 de noviembre de 2026

## Resumen

Se evaluó el comportamiento observable de autenticación y productos de DummyJSON mediante pruebas de caja negra priorizadas por riesgo. El diseño comprende 24 casos: seis automatizados y 18 diseños manuales ejecutados mediante inspección HTTP asistida. En el ciclo del 9 de noviembre de 2026 se registraron 23 aprobados y un fallido. El hallazgo corresponde a HTTP 500 ante una firma JWT alterada, frente al rechazo 401/403 definido como esperado. Las escrituras simuladas conservaron el comportamiento documentado de ausencia de persistencia. El informe relaciona alcance, riesgos, condiciones, técnicas, casos y evidencia, con una adaptación académica de la documentación basada en ISO/IEC/IEEE 29119-3.

Palabras clave: pruebas de software, API REST, DummyJSON, riesgo, trazabilidad.

## 1. Información del documento

### 1.1 Identificador único del documento

PP-DUMMYJSON-FINAL-01. Versión 3.2. Revisión documental y sustentación: 19 de noviembre de 2026. Línea base técnica de código y evidencias: commit 7ddd782f639256043145a5856fc993b8125cfe4d del repositorio del proyecto.

### 1.2 Organización emisora y autores

Institución Universitaria Pascual Bravo. Autores: Miguel Ángel Noreña Cano, Marlon Maldonado y Aldair Estiven Novoa.

### 1.3 Autoridad de aprobación

Roberto José Calderón Bermejo, docente de Pruebas de Software, es la autoridad de aprobación académica de este plan y sus adaptaciones. Los autores presentan el expediente para evaluación; no consta una aprobación docente registrada ni se atribuye aceptación del servicio externo.

### 1.4 Historial de cambios y control de versiones

El historial de Google Docs conserva los cambios del informe y GitHub los del código y anexos. La revisión documental no constituye una nueva ejecución. La Tabla 1 resume las versiones.

Tabla 1

Historial de cambios del documento

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.1 | 09/11/2026 | Expediente de ejecución y retest. |
| 2.0 | No registrada | Síntesis del plan. |
| 2.1 | 10/11/2026 | Publicación inicial en GitHub. |
| 3.0 | 18/11/2026 | Consolidación en Google Docs y reglas D1–D3. |
| 3.1 | 18/11/2026 | Estructura de la guía, adaptación, condiciones y sustentación del 19/11/2026. |
| 3.2 | 19/11/2026 | Explicación de DummyJSON, HTTP/JSON, Python, diseño e identificación de casos e interpretación de resultados. |

## 2. Introducción y adaptación

### 2.1 Alcance del documento

DummyJSON es una API REST pública de práctica que ofrece datos ficticios de productos, usuarios y otros recursos. Una API permite que un programa solicite información o una operación a otro servicio; un endpoint es la ruta concreta de esa operación. En este proyecto se evalúa el servicio de terceros mediante solicitudes HTTP y respuestas JSON, sin desarrollar su servidor ni acceder a su código interno.

HTTP es el protocolo de intercambio. GET consulta información; POST envía datos, por ejemplo para iniciar sesión o simular un alta; PATCH modifica parcialmente un recurso; DELETE solicita su eliminación. JSON representa los datos mediante objetos, listas y valores. En DummyJSON, las escrituras evaluadas son simuladas: reflejan el cambio en la respuesta y no lo conservan para una lectura posterior (DummyJSON, s. f.-a, s. f.-b).

El objetivo es verificar el contrato observable de autenticación, consulta de productos y escrituras simuladas, con especial atención a sesiones no válidas y a la interpretación de la persistencia. La guía de la asignatura organiza el trabajo según ISO/IEC/IEEE 29119-3 y pruebas basadas en riesgos. Se aplica adaptación académica, sin declarar conformidad integral con la norma (International Organization for Standardization, 2021; Plan de pruebas de software, s. f.).

### 2.2 Referencias documentales

Se utilizan ISO/IEC/IEEE 29119-3:2021 como marco de documentación, la guía de estructura del plan y los materiales de diseño de casos de la asignatura. El contrato observable se consulta en la documentación de DummyJSON, Auth y Products. Las referencias completas se presentan al final; las evidencias y fichas de casos están enlazadas en el Apéndice A.

### 2.3 Conformidad y adaptación (tailoring)

Se aplica adaptación académica; no se declara conformidad íntegra con ISO/IEC/IEEE 29119-3. Se conservan planificación, análisis de riesgos, diseño, ejecución, registro de incidentes e informe de resultados. El uso evaluado tiene criticidad académica baja: se trabaja con datos ficticios y sin operaciones de producción. Esto no reduce la prioridad de los riesgos de autenticación ni permite aceptar resultados fallidos como aprobados.

La ventana de planificación es de tres semanas y la capacidad estimada es de 72 horas-persona. No se desarrollan políticas corporativas de prueba ni gobierno organizacional completo, porque el objeto es una práctica de un único equipo y una API de terceros; se asume menor generalización y reproducibilidad fuera de este contexto.

Se excluyen pruebas unitarias, de caja blanca y de base de datos por falta de acceso al código y a la infraestructura del proveedor; se asume el riesgo de defectos internos no detectados. La interfaz gráfica no aplica porque no se evalúa un cliente propio. Se excluyen pruebas de carga y seguridad profunda por la ventana de tres semanas, la criticidad del uso académico y el carácter compartido del servicio; se asume capacidad no determinada y posibles vulnerabilidades fuera de los escenarios de autenticación evaluados. Estas exclusiones limitan las conclusiones y no certifican aptitud para producción.

El equipo real tiene tres integrantes frente a cuatro indicados en la guía. La distribución contempla ocho casos por integrante y 72 horas-persona de capacidad planificada. Esta adaptación organizativa se declara para evaluación docente.

### 2.4 Glosario

API: interfaz para intercambiar datos u operaciones entre programas. Endpoint: ruta de una operación del servicio. HTTP: protocolo de las solicitudes y respuestas; HTTPS incorpora protección del transporte. JSON: formato de datos que se analiza para verificar los campos de una respuesta.

RBT: pruebas basadas en riesgos. Riesgo: posibilidad de un fallo y su impacto. Condición: propiedad observable que debe evaluarse. Caso de prueba: precondiciones, entradas y comprobaciones con un resultado esperado. Oráculo: criterio que decide si el resultado observado coincide con el esperado. Evidencia: registro que permite revisar lo ocurrido.

Línea base: estado inicial observado. Token: dato utilizado para acreditar una sesión; JWT: formato firmado del token empleado en los casos de autenticación. Retest: repetición dirigida de una prueba. CT: etiqueta propia que identifica un caso de prueba. P1: prioridad de prueba cuyo cumplimiento se exige para el cierre satisfactorio del ciclo.

## 3. Contexto de las pruebas

### 3.1 Elementos de prueba (test items)

API pública https://dummyjson.com. Recursos: /auth/login, /auth/me, /auth/refresh, /products, /products/{id}, /products/add, /products/search y /products/categories (DummyJSON, s. f.-a, s. f.-b).

### 3.2 Alcance y exclusiones de las pruebas

Se evalúan login, perfil, renovación de sesión, consultas, categorías, búsqueda, paginación y POST/PATCH/DELETE simulados. Se excluyen los demás módulos, la interfaz de un cliente propio, el código interno, las bases de datos, la carga y la seguridad profunda, conforme a la justificación y los riesgos residuales de 2.3. Como antecedente, la Actividad de clase 2, fechada el 24 de septiembre de 2026, identificó disponibilidad, autenticación, productos, usuarios, publicaciones/comentarios, carritos y tareas. El ciclo final concentra el esfuerzo en autenticación y productos; los demás elementos del taller inicial no se presentan como cubiertos por estas 24 pruebas (Actividad de clase 2, 2026).

### 3.3 Suposiciones y restricciones

Se supone acceso por HTTPS, disponibilidad de credenciales públicas de demostración y respuestas JSON. Los datos, identificadores, orden y total del catálogo pueden cambiar; cada ciclo obtiene una línea base propia. El equipo no controla las reparaciones del proveedor ni tiene acceso interno. Las restricciones son tres semanas planificadas, tres integrantes reales y el uso de un servicio compartido.

### 3.4 Partes interesadas

Los tres autores planifican, diseñan y documentan las pruebas. El docente evalúa y aprueba académicamente el plan y sus adaptaciones. El proveedor de DummyJSON administra el servicio y sus correcciones. El consumidor de la API utiliza cuentas ficticias y credenciales públicas de demostración.

## 4. Gestión de riesgos

### 4.1 Identificación de riesgos

La Tabla 2 registra los riesgos identificados dentro del alcance: integridad observable de las escrituras, autenticación, credenciales, renovación, paginación, consulta, búsqueda, categorías y rendimiento no evaluado; además, disponibilidad del entorno, tiempo, tokens y tamaño del equipo. Las amenazas internas y de seguridad profunda se reconocen como riesgo residual en 2.3; la selección no constituye un inventario universal de vulnerabilidades.

### 4.2 Matriz de análisis de riesgos

Exposición E = P × I. Probabilidad: 1, excepcional; 2, poco probable; 3, posible; 4, probable; 5, muy probable. Impacto: 1, efecto mínimo; 2, inconsistencia menor; 3, función degradada; 4, resultado funcional incorrecto o dato sensible expuesto; 5, acceso indebido o pérdida de confianza en una función esencial del alcance. Niveles: bajo, 1–4; medio, 5–9; alto, 10–14; crítico, 15–25. Son juicios de planificación del equipo, no frecuencias medidas. La columna Exposición conserva los factores P e I de cada riesgo.

La Tabla 2 presenta los riesgos y su tratamiento.

Tabla 2

Registro y tratamiento de riesgos

| ID | Riesgo | Exposición | Tratamiento |
| --- | --- | --- | --- |
| R07 | Falsa persistencia | 4 × 4 = 16; crítico | CT-R07-01–03; lectura antes/después. |
| R03 | Sesión no válida | 3 × 5 = 15; crítico | CT-R03-01–04; cuatro estados de sesión. |
| F-R01 | Credenciales incorrectas | 3 × 4 = 12; alto | CT-F01-01–04. |
| F-R02 | Renovación indebida | 3 × 4 = 12; alto | CT-F02-01–03. |
| F-R03 | Omisión o duplicación al paginar | 3 × 4 = 12; alto | CT-F03-01–04. |
| F-R04 | Recurso inexistente | 2 × 3 = 6; medio | CT-F04-01–02; dependencia de consultas. |
| F-R05 | Búsqueda incorrecta | 2 × 3 = 6; medio | CT-F05-01–02; uso frecuente y bajo costo. |
| R17* | Categorías inconsistentes | 2 × 2 = 4; bajo | CT-R17-01–02; controles complementarios. |
| F-R06 | Capacidad no determinada | 2 × 4 = 8; medio | Aceptación del riesgo residual de carga excluida. |
| FP-01 | Caída o cambio del servicio | 3 × 4 = 12; alto | Control previo, bloqueo y reprogramación. |
| FP-02 | Retraso | 3 × 4 = 12; alto | WBS, distribución y revisión de hitos. |
| FP-03 | Exposición de tokens | 2 × 4 = 8; medio | Censura y revisión de los registros. |
| FP-04 | Diferencia de tamaño de equipo | 3 × 4 = 12; alto | Adaptación y redistribución de carga. |

### 4.3 Tratamiento y mitigación

Los riesgos críticos y altos del producto se traducen obligatoriamente en condiciones y casos con evidencia. Para cada riesgo la Tabla 2 identifica su tratamiento y las pruebas asociadas. Los riesgos medios se prueban cuando hay dependencia funcional o bajo costo; F-R06 acepta el riesgo residual de carga excluida. R17*, bajo, recibe dos controles complementarios; la aceptación sin pruebas es una opción de planificación, no una obligación.

Se adapta el tratamiento de los riesgos del proyecto: FP-01 requiere comprobación previa del servicio y registro de bloqueos; FP-02 y FP-04, verificación de carga, responsables e hitos; FP-03, censura y revisión de registros. Son controles verificables de gestión, pues una prueba funcional de la API no demuestra ausencia de retrasos ni disponibilidad futura. Esta distinción no exime de probar los riesgos altos del producto.

Los cinco riesgos altos/críticos de producto tienen ejecución completa. Cuatro tienen todos sus casos aprobados. R03 conserva la incidencia INC-001. La cobertura de ejecución no equivale a mitigación total.

## 5. Estrategia y derivación de casos

### 5.1 Derivación de condiciones de prueba

Los casos se diseñan a partir de tres fuentes: la guía y las técnicas de la asignatura, el comportamiento documentado por DummyJSON y los riesgos evaluados del alcance. La guía establece un volumen de 20 a 24 casos; se seleccionan 24. Para cada riesgo se formula una condición, se elige una técnica para generar entradas y se fija el resultado esperado antes de ejecutar. El script implementa seis de esos casos y no reemplaza su justificación de diseño.

La identificación es una convención propia del proyecto. En CT-R07-02, CT identifica un caso de prueba, R07 remite al riesgo de falsa persistencia y 02 señala el segundo caso asociado a ese riesgo. C07-02 identifica su condición evaluable. En CT-F01-01, F01 identifica el grupo funcional de login vinculado con F-R01, y el último 01 distingue el caso. Los identificadores permiten localizar el mismo caso en la documentación, el código y sus registros; no son códigos de respuesta de la API.

Cada condición describe una propiedad observable y deriva de un riesgo evaluado. R07 genera C07-01, alta simulada sin persistencia; C07-02, PATCH refleja T1 pero el GET conserva T0; C07-03, DELETE informa eliminación simulada y el GET conserva el recurso. R03 genera C03-01, acceso con token válido; C03-02, rechazo sin token; C03-03, rechazo de firma alterada; C03-04, rechazo tras expiración real.

F-R01 genera CF01-1 a CF01-4: login válido, contraseña incorrecta, usuario inexistente y campos vacíos. F-R02 genera CF02-1 a CF02-3: renovación válida, ausencia de refreshToken y firma alterada. F-R03 genera CF03-1 a CF03-4: primer elemento, último elemento, desplazamiento N y limit=0 según contrato.

F-R04 genera CF04-1 y CF04-2: consulta existente e inexistente. F-R05 genera CF05-1 y CF05-2: búsqueda con y sin coincidencias. R17* genera C17-01, estructura válida de categorías, y C17-02, unicidad de slugs y correspondencia de rutas. La Tabla 4 vincula estas 24 condiciones con casos, técnicas y resultados; las fichas enlazadas completan precondiciones y oráculos.

### 5.2 Técnicas de diseño de pruebas

La trazabilidad se mantiene en ambos sentidos entre riesgo, condición, técnica, caso y evidencia. El anexo en Markdown contiene las 24 fichas, sus datos, precondiciones y oráculos. Las seis fichas automatizadas enlazan directamente a la implementación, que constituye la fuente de sus pasos (Casos de pruebas, s. f.; Fundamentos de testing, s. f.).

Equivalencia: clases de credenciales válidas, inválidas y vacías; tokens válidos, ausentes o alterados; recursos existentes o inexistentes; búsquedas con o sin coincidencias. Límites: para N productos, skip = 0, N−1 y N con limit = 1. limit = 0 se trata como clase especial documentada. Transición de estados: lecturas independientes antes/después de una escritura y comparación de un JWT antes/después de su expiración real.

Reglas de decisión de escrituras simuladas: cada regla supone recurso y datos disponibles. Para PATCH y DELETE se exige una lectura inicial satisfactoria. El título temporal se genera mediante UUID.

La Tabla 3 presenta las reglas de decisión.

Tabla 3

Reglas de decisión de escrituras simuladas

| Regla / caso | Operación y condición | Respuesta esperada | Lectura posterior |
| --- | --- | --- | --- |
| D1 / CT-R07-01 | POST /products/add; título UUID | 201; alta simulada con ID | GET del ID devuelto: 404. |
| D2 / CT-R07-02 | PATCH /products/1; título T1 distinto de T0 | 200; título T1 | GET del producto: 200 y título T0. |
| D3 / CT-R07-03 | DELETE /products/1; recurso existente | 200; isDeleted y deletedOn | GET del producto: 200; recurso conservado. |

La decisión de aprobación exige cumplir conjuntamente la respuesta inmediata y la lectura posterior de la regla. Los controles no atribuyen persistencia a la respuesta simulada.

### 5.3 Generación de casos de prueba y trazabilidad

La Tabla 4 presenta la trazabilidad de los casos.

Tabla 4

Trazabilidad de los 24 casos de prueba

| Caso | Riesgo / condición | Técnica y entrada | Resultado |
| --- | --- | --- | --- |
| CT-R07-01 | R07 / C07-01 | Transición de estados + tabla de decisión D1. Título único generado por UUID. | Aprobado |
| CT-R07-02 | R07 / C07-02 | Transición de estados + tabla de decisión D2. Producto 1 y título único. | Aprobado |
| CT-R07-03 | R07 / C07-03 | Transición de estados + tabla de decisión D3. Producto 1. | Aprobado |
| CT-R03-01 | R03 / C03-01 | Partición de equivalencia: token válido. Credenciales públicas de demostración y token recién emitido. | Aprobado |
| CT-R03-02 | R03 / C03-02 | Partición de equivalencia: token ausente. Sin Authorization y sin cookies. | Aprobado |
| CT-R03-03 | R03 / C03-03 | Partición de equivalencia: firma inválida. JWT válido con primer carácter de firma cambiado. | Fallido |
| CT-R03-04 | R03 / C03-04 | Transición de estados: válido a expirado; límite temporal. Token firmado obtenido con expiresInMins=1; instantes t<exp y t>exp+5 s. | Aprobado |
| CT-R17-01 | R17* / C17-01 | Partición de equivalencia: campos requeridos de tipo cadena. Respuesta completa de /products/categories. | Aprobado |
| CT-R17-02 | R17* / C17-02 | Partición de equivalencia: slug único y ruta coherente. Todos los slugs y URLs del catálogo. | Aprobado |
| CT-F01-01 | F-R01 / CF01-1 | Partición de equivalencia; variación aislada respecto al control válido. username='emilys'; password='emilyspass'. | Aprobado |
| CT-F01-02 | F-R01 / CF01-2 | Partición de equivalencia; variación aislada respecto al control válido. username='emilys'; password='qa_clave_incorrecta'. | Aprobado |
| CT-F01-03 | F-R01 / CF01-3 | Partición de equivalencia; variación aislada respecto al control válido. username='qa_usuario_inexistente_9f73'; password='emilyspass'. | Aprobado |
| CT-F01-04 | F-R01 / CF01-4 | Partición de equivalencia; variación aislada respecto al control válido. username=''; password=''. | Aprobado |
| CT-F02-01 | F-R02 / CF02-1 | Partición de equivalencia + transición de sesión. refreshToken recién emitido y expiresInMins=1 | Aprobado |
| CT-F02-02 | F-R02 / CF02-2 | Partición de equivalencia + transición de sesión. JSON {} sin cookies | Aprobado |
| CT-F02-03 | F-R02 / CF02-3 | Partición de equivalencia + transición de sesión. refreshToken con primer carácter de firma cambiado | Aprobado |
| CT-F03-01 | F-R03 / CF03-1 | Valores límite sobre desplazamiento [0,N-1]; limit=0 es clase especial. limit=1&skip=0 | Aprobado |
| CT-F03-02 | F-R03 / CF03-2 | Valores límite sobre desplazamiento [0,N-1]; limit=0 es clase especial. limit=1&skip=N-1 | Aprobado |
| CT-F03-03 | F-R03 / CF03-3 | Valores límite sobre desplazamiento [0,N-1]; limit=0 es clase especial. limit=1&skip=N | Aprobado |
| CT-F03-04 | F-R03 / CF03-4 | Equivalencia: limit=0, clase especial documentada. limit=0&skip=0 | Aprobado |
| CT-F04-01 | F-R04 / CF04-1 | Partición de equivalencia: identificador existente / inexistente. 1 | Aprobado |
| CT-F04-02 | F-R04 / CF04-2 | Partición de equivalencia: identificador existente / inexistente. max(ID de línea base)+100000 | Aprobado |
| CT-F05-01 | F-R05 / CF05-1 | Partición de equivalencia: consulta con / sin coincidencias. Título completo del producto 1, codificado como parámetro q | Aprobado |
| CT-F05-02 | F-R05 / CF05-2 | Partición de equivalencia: consulta con / sin coincidencias. qa_sin_coincidencias_ + UUID | Aprobado |

### 5.4 Requisitos de entorno y datos de prueba

Python se utiliza como cliente para las consultas y para la automatización de seis casos. En tests/pruebas_api.py, urllib.request construye y envía las solicitudes; json interpreta sus cuerpos; require compara el estado HTTP y los campos con el resultado esperado. El script registra método, ruta, respuesta y duración, censura datos sensibles y guarda un archivo JSON distinto por ejecución. Utiliza la biblioteca estándar de Python.

Consultar no equivale a probar: una prueba incorpora una expectativa y una comprobación. Por ejemplo, CT-R07-02 requiere GET 200 con título T0, PATCH 200 que refleje T1 y un nuevo GET 200 que conserve T0. Deben cumplirse todas las comprobaciones. Los 18 diseños manuales se ejecutaron mediante inspección HTTP asistida y se registran por separado; no se atribuye su ejecución al script de seis casos.

Entorno: Python 3.10 o posterior, cliente HTTP por HTTPS sin reutilización de cookies. Ejecución registrada: Linux, Python 3.12.14 y urllib. Datos: producto 1, títulos UUID, catálogo observado y credenciales públicas emilys/emilyspass. Los tokens se mantienen temporalmente y se censuran en las evidencias.

Para expiración se utiliza un token auténtico de un minuto, con control válido previo y lectura posterior a exp. En el ciclo registrado la consulta ocurrió 42,14 segundos después del vencimiento y recibió 401. El catálogo observado tenía 194 productos y 24 categorías; son datos de ese ciclo.

### 5.5 Criterios de suspensión y finalización

Entrada: alcance, datos, criterios esperados y servicio disponibles. Suspensión: indisponibilidad, cambio de contrato, datos insuficientes o exposición de tokens. Reanudación: resolver la causa y realizar un control previo. Cierre satisfactorio: 24 casos con evidencia, todos los P1 aprobados, cero defectos críticos/altos abiertos y revisión independiente registrada.

## 6. Actividades y estimación

### 6.1 Desglose de tareas

El trabajo se divide en alcance y riesgos (T1), entorno y datos (T2), diseño y trazabilidad (T3), automatización (T4), ejecución e incidentes (T5), retest y regresión (T6), revisión documental (T7), e informe y sustentación (T8). Las dependencias figuran en la Tabla 5.

### 6.2 Estimación de esfuerzo por actividad

La Tabla 5 presenta la estimación de las actividades.

Tabla 5

Actividades y estimación del esfuerzo

| Actividad | Horas-persona | Dependencia |
| --- | --- | --- |
| T1. Alcance, referencias y riesgos | 6 | Inicio |
| T2. Entorno y datos | 4 | T1 |
| T3. Diseño y trazabilidad | 14 | T1 |
| T4. Automatización y depuración | 14 | T2 y T3 parcial |
| T5. Ejecución e incidentes | 14 | T2–T4 |
| T6. Retest y regresión | 6 | T5 |
| T7. Revisión documental | 6 | T3 y T5 |
| T8. Informe y sustentación | 8 | T6 y T7 |
| Total | 72 | 3 personas × 8 h/semana × 3 semanas |

La estimación representa capacidad planificada. Las reparaciones del proveedor quedan fuera. Las horas estimadas no representan duración medida de las solicitudes HTTP ni certificación de horas efectivamente trabajadas.

## 7. Personal y responsabilidades

### 7.1 Roles y responsabilidades de prueba

Miguel Ángel Noreña Cano: alcance, adaptación y riesgos, casos 1–8. Marlon Maldonado: condiciones, datos y trazabilidad, casos 9–16. Aldair Estiven Novoa: automatización y evidencias, casos 17–24. La revisión cruzada prevista asigna los casos 1–8 a Marlon, 9–16 a Aldair y 17–24 a Miguel.

La ejecución de los seis casos automatizados utiliza aserciones en el script. Los 18 diseños manuales fueron ejecutados mediante inspección HTTP asistida por herramientas y un conductor de solicitudes. La responsabilidad académica y la revisión independiente se distinguen de esa ejecución técnica. La revisión independiente no está registrada como completada. Sí consta una coevaluación previa de la Actividad 2 por el equipo revisor 2: se reconocen la identificación de funcionalidades y los criterios verificables, y se solicitan exclusiones explícitas, precisión de actores y códigos HTTP. Estos aspectos se desarrollan en 2.3, 3.2–3.4 y en los oráculos de los casos. Esa revisión del alcance inicial no sustituye la revisión independiente del expediente final (Actividad de clase 2, 2026; Coevaluación de la Actividad 2, s. f.).

## 8. Cronograma

### 8.1 Hitos y fechas de ejecución

La Tabla 6 presenta la distribución del trabajo por semana.

Tabla 6

Cronograma de tres semanas

| Semana | Actividades | Carga e hito |
| --- | --- | --- |
| 1 / días 1–7 | T1 6 h + T2 4 h + T3 14 h | 24 h; alcance y diseño |
| 2 / días 8–14 | T4 14 h + T5 10 h | 24 h; scripts y primera ejecución |
| 3 / días 15–21 | T5 4 h + T6 6 h + T7 6 h + T8 8 h | 24 h; retest e informe |

La Tabla 6 organiza las actividades en un ciclo planificado de tres semanas. Fechas documentadas: ejecución y retest, 9 de noviembre de 2026; publicación inicial en GitHub, 10 de noviembre de 2026; consolidación y revisión documental, 18 de noviembre de 2026. La sustentación está programada para el 19 de noviembre de 2026, según confirmación del equipo. La fecha oficial de inicio del ciclo no está acreditada; las semanas relativas expresan planificación y no demuestran por sí mismas tres semanas efectivamente trabajadas. El taller del 24 de septiembre de 2026 es un antecedente formativo documentado; no se lo identifica como fecha oficial de inicio del ciclo final de tres semanas.

## 9. Resultados y discusión

La Tabla 7 presenta los indicadores del ciclo ejecutado.

Tabla 7

Resultados del ciclo de pruebas

| Indicador | Valor |
| --- | --- |
| Planificados / ejecutados | 24 / 24 |
| Aprobados / fallidos / bloqueados | 23 / 1 / 0 |
| Aprobación | 95,83 % |
| P1 aprobados | 6 de 7 |
| Riesgos altos/críticos con ejecución | 5 de 5 |
| Riesgos altos/críticos con todos sus casos aprobados | 4 de 5 |
| Incidencia abierta | INC-001 |

La interpretación combina estado HTTP y contenido. 200 indica una respuesta satisfactoria; 201, creación; 401, falta de autenticación válida; 403, acceso rechazado; 404, recurso no encontrado; 500, error interno del servidor. Un código satisfactorio no basta si los datos incumplen la condición.

Un caso negativo aprueba cuando devuelve el rechazo esperado: por ejemplo, un acceso sin token debe fallar para el consumidor y aprobar como prueba si se observa 401/403 sin perfil. Aprobado significa coincidencia con el oráculo del caso, no ausencia de errores en todo el servicio. Fallido significa discrepancia; bloqueado significa que el entorno o una dependencia impidió evaluar el caso.

Las escrituras simuladas cumplieron el criterio de respuesta y consulta posterior. Login válido, ausencia y expiración de tokens, renovación, paginación, búsqueda y categorías conservaron los resultados registrados en sus casos.

INC-001, CT-R03-03: al alterar la firma del accessToken se esperaba 401 o 403 sin perfil. Se observaron dos respuestas HTTP 500 con el mensaje invalid signature y sin acceso al perfil. Severidad propuesta: media. Prioridad: alta por corresponder a un caso P1. El proveedor de DummyJSON controla la reparación.

El ejecutor inicial clasificó la primera respuesta 500 como bloqueo. Se ajustó la clasificación local y se repitió el caso manteniendo el mismo oráculo. El retest volvió a responder 500 y quedó fallido. Se conserva la primera respuesta en su registro original. La corrección del cliente de pruebas no equivale a una corrección de la API.

La ejecución documental está completa con un hallazgo abierto. El cierre satisfactorio definido no se alcanza porque falla un P1 y no consta revisión independiente. La evaluación académica del informe se distingue de la aceptación del comportamiento del servicio.

## 10. Conclusiones

La relación entre riesgo, condición, técnica, caso y evidencia permite justificar la selección y el resultado de cada prueba. El contraste mediante lecturas independientes confirma el carácter simulado de las escrituras de DummyJSON. La validación de las herramientas de prueba resulta necesaria para clasificar correctamente los hallazgos. Los resultados respaldan 23 casos aprobados y un fallo abierto, con conclusiones limitadas a los recursos, datos y condiciones evaluados.

Como trabajo posterior corresponde verificar la respuesta a firmas inválidas tras una eventual corrección del proveedor, conservar nuevas evidencias y registrar la revisión cruzada del equipo. Las pruebas de carga, internas y de seguridad profunda requieren otro alcance.

## Referencias

Actividad de clase 2: Identificación del objeto de prueba (Test items) [Taller diligenciado y coevaluación]. (2026, 24 de septiembre).

Casos de pruebas: Ingeniería de pruebas, especificación y diseño formal [Diapositivas de clase]. (s. f.).

Coevaluación de la Actividad 2 [Observaciones manuscritas del equipo revisor]. (s. f.).

DummyJSON. (s. f.-a). Auth. [https://dummyjson.com/docs/auth](https://dummyjson.com/docs/auth)

DummyJSON. (s. f.-b). Products. [https://dummyjson.com/docs/products](https://dummyjson.com/docs/products)

Fundamentos de testing: Ciclo de vida del software [Diapositivas de clase]. (s. f.).

International Organization for Standardization. (2021). Software and systems engineering—Software testing—Part 3: Test documentation (ISO/IEC/IEEE 29119-3:2021). [https://www.iso.org/standard/79429.html](https://www.iso.org/standard/79429.html)

Plan de pruebas de software: Guía de estructura y gestión [Guía de la asignatura Pruebas de Software]. (s. f.).

## Apéndice A

## Material complementario y evidencias

[Repositorio de código, casos y evidencias](https://github.com/drakcore12/proyecto-final-de-pruebas-de-software-)

[Casos y trazabilidad en Markdown](https://github.com/drakcore12/proyecto-final-de-pruebas-de-software-/blob/main/docs/casos-y-trazabilidad.md)

[Registro consolidado por caso](https://github.com/drakcore12/proyecto-final-de-pruebas-de-software-/blob/main/evidencias/resultados-consolidados.json)

[INC-001: seguimiento del hallazgo](https://github.com/drakcore12/proyecto-final-de-pruebas-de-software-/issues/1)

