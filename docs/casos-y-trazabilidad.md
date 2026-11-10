# Casos y trazabilidad de DummyJSON

Resultado de ejecución: **23 Aprobados y 1 Fallido**. Consultar [registro con evidencias](registro-ejecucion.md). Se conserva el oráculo definido antes de ejecutar; se informa además el código exacto observado. El equipo debe revisar la especificación antes de su aprobación académica. Un 5xx o 429 no demuestra que una validación funcional sea correcta.

| N.º | Caso | Riesgo | Condición | Modalidad | Prioridad | Responsable propuesto |
|---:|---|---|---|---|---|---|
| 1 | [CT-R07-01](#ct-r07-01) | R07 | C07-01 | Auto | P1 | Miguel Ángel Noreña Cano |
| 2 | [CT-R07-02](#ct-r07-02) | R07 | C07-02 | Auto | P1 | Miguel Ángel Noreña Cano |
| 3 | [CT-R07-03](#ct-r07-03) | R07 | C07-03 | Auto | P1 | Miguel Ángel Noreña Cano |
| 4 | [CT-R03-01](#ct-r03-01) | R03 | C03-01 | Auto | P1 | Miguel Ángel Noreña Cano |
| 5 | [CT-R03-02](#ct-r03-02) | R03 | C03-02 | Auto | P1 | Miguel Ángel Noreña Cano |
| 6 | [CT-R03-03](#ct-r03-03) | R03 | C03-03 | Auto | P1 | Miguel Ángel Noreña Cano |
| 7 | [CT-R03-04](#ct-r03-04) | R03 | C03-04 | Manual | P1 | Miguel Ángel Noreña Cano |
| 8 | [CT-R17-01](#ct-r17-01) | R17* | C17-01 | Manual | P3 | Miguel Ángel Noreña Cano |
| 9 | [CT-R17-02](#ct-r17-02) | R17* | C17-02 | Manual | P3 | Marlon Maldonado |
| 10 | [CT-F01-01](#ct-f01-01) | F-R01 | CF01-1 | Manual | P2 | Marlon Maldonado |
| 11 | [CT-F01-02](#ct-f01-02) | F-R01 | CF01-2 | Manual | P2 | Marlon Maldonado |
| 12 | [CT-F01-03](#ct-f01-03) | F-R01 | CF01-3 | Manual | P2 | Marlon Maldonado |
| 13 | [CT-F01-04](#ct-f01-04) | F-R01 | CF01-4 | Manual | P2 | Marlon Maldonado |
| 14 | [CT-F02-01](#ct-f02-01) | F-R02 | CF02-1 | Manual | P2 | Marlon Maldonado |
| 15 | [CT-F02-02](#ct-f02-02) | F-R02 | CF02-2 | Manual | P2 | Marlon Maldonado |
| 16 | [CT-F02-03](#ct-f02-03) | F-R02 | CF02-3 | Manual | P2 | Marlon Maldonado |
| 17 | [CT-F03-01](#ct-f03-01) | F-R03 | CF03-1 | Manual | P2 | Aldair Estiven Novoa |
| 18 | [CT-F03-02](#ct-f03-02) | F-R03 | CF03-2 | Manual | P2 | Aldair Estiven Novoa |
| 19 | [CT-F03-03](#ct-f03-03) | F-R03 | CF03-3 | Manual | P2 | Aldair Estiven Novoa |
| 20 | [CT-F03-04](#ct-f03-04) | F-R03 | CF03-4 | Manual | P2 | Aldair Estiven Novoa |
| 21 | [CT-F04-01](#ct-f04-01) | F-R04 | CF04-1 | Manual | P2 | Aldair Estiven Novoa |
| 22 | [CT-F04-02](#ct-f04-02) | F-R04 | CF04-2 | Manual | P2 | Aldair Estiven Novoa |
| 23 | [CT-F05-01](#ct-f05-01) | F-R05 | CF05-1 | Manual | P2 | Aldair Estiven Novoa |
| 24 | [CT-F05-02](#ct-f05-02) | F-R05 | CF05-2 | Manual | P2 | Aldair Estiven Novoa |

## Índice inverso por riesgo

- **R07:** [CT-R07-01](#ct-r07-01), [CT-R07-02](#ct-r07-02), [CT-R07-03](#ct-r07-03)
- **R03:** [CT-R03-01](#ct-r03-01), [CT-R03-02](#ct-r03-02), [CT-R03-03](#ct-r03-03), [CT-R03-04](#ct-r03-04)
- **R17*:** [CT-R17-01](#ct-r17-01), [CT-R17-02](#ct-r17-02)
- **F-R01:** [CT-F01-01](#ct-f01-01), [CT-F01-02](#ct-f01-02), [CT-F01-03](#ct-f01-03), [CT-F01-04](#ct-f01-04)
- **F-R02:** [CT-F02-01](#ct-f02-01), [CT-F02-02](#ct-f02-02), [CT-F02-03](#ct-f02-03)
- **F-R03:** [CT-F03-01](#ct-f03-01), [CT-F03-02](#ct-f03-02), [CT-F03-03](#ct-f03-03), [CT-F03-04](#ct-f03-04)
- **F-R04:** [CT-F04-01](#ct-f04-01), [CT-F04-02](#ct-f04-02)
- **F-R05:** [CT-F05-01](#ct-f05-01), [CT-F05-02](#ct-f05-02)

## CT-R07-01

**Alta simulada sin persistencia**

- Riesgo: R07; condición: C07-01.
- Técnica y derivación: Transición de estados + tabla de decisión D1.
- Datos: Título único generado por UUID.
- Precondiciones: Producto de prueba no existente.
- Resultado esperado: La respuesta refleja el alta; una lectura independiente no encuentra el recurso creado.
- Implementación ejecutable: [CT-R07-01](../tests/pruebas_api.py#L84). Buscar el ID en CASES; el código es la fuente de los pasos.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-R07-02

**Modificación simulada sin persistencia**

- Riesgo: R07; condición: C07-02.
- Técnica y derivación: Transición de estados + tabla de decisión D2.
- Datos: Producto 1 y título único.
- Precondiciones: Lectura de línea base del producto 1.
- Resultado esperado: PATCH refleja el cambio y GET posterior conserva el título inicial.
- Implementación ejecutable: [CT-R07-02](../tests/pruebas_api.py#L99). Buscar el ID en CASES; el código es la fuente de los pasos.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-R07-03

**Eliminación simulada sin persistencia**

- Riesgo: R07; condición: C07-03.
- Técnica y derivación: Transición de estados + tabla de decisión D3.
- Datos: Producto 1.
- Precondiciones: GET inicial satisfactorio.
- Resultado esperado: DELETE informa isDeleted=true y deletedOn; GET posterior conserva el recurso.
- Implementación ejecutable: [CT-R07-03](../tests/pruebas_api.py#L110). Buscar el ID en CASES; el código es la fuente de los pasos.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-R03-01

**Acceso con sesión válida**

- Riesgo: R03; condición: C03-01.
- Técnica y derivación: Partición de equivalencia: token válido.
- Datos: Credenciales públicas de demostración y token recién emitido.
- Precondiciones: Cliente sin almacén de cookies.
- Resultado esperado: El perfil autenticado coincide con el usuario que inició sesión.
- Implementación ejecutable: [CT-R03-01](../tests/pruebas_api.py#L122). Buscar el ID en CASES; el código es la fuente de los pasos.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-R03-02

**Rechazo sin token**

- Riesgo: R03; condición: C03-02.
- Técnica y derivación: Partición de equivalencia: token ausente.
- Datos: Sin Authorization y sin cookies.
- Precondiciones: Cliente limpio.
- Resultado esperado: Se rechaza /auth/me y no se devuelve un perfil de usuario.
- Implementación ejecutable: [CT-R03-02](../tests/pruebas_api.py#L130). Buscar el ID en CASES; el código es la fuente de los pasos.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-R03-03

**Rechazo de token alterado**

- Riesgo: R03; condición: C03-03.
- Técnica y derivación: Partición de equivalencia: firma inválida.
- Datos: JWT válido con primer carácter de firma cambiado.
- Precondiciones: Token original válido; sin cookies.
- Resultado esperado: El token alterado es rechazado; no se devuelve un perfil.
- Implementación ejecutable: [CT-R03-03](../tests/pruebas_api.py#L137). Buscar el ID en CASES; el código es la fuente de los pasos.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Fallido, INC-001. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-R03-04

**Rechazo de token expirado**

- Riesgo: R03; condición: C03-04.
- Técnica y derivación: Transición de estados: válido a expirado; límite temporal.
- Datos: Token firmado obtenido con expiresInMins=1; instantes t<exp y t>exp+5 s.
- Precondiciones: Credenciales de demostración; reloj sincronizado; sin cookies.
- Resultado esperado: El control previo permite acceso y la consulta posterior devuelve 401 o 403 sin perfil. Si no se puede demostrar expiración real, marcar Bloqueado.

Pasos:

1. Obtener token de un minuto.
2. Consultar /auth/me antes de exp y guardar control positivo.
3. Leer exp del JWT solo para planificar la espera, sin modificarlo.
4. Esperar hasta superar exp en cinco segundos.
5. Repetir GET /auth/me con el mismo token.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-R17-01

**Estructura del catálogo de categorías**

- Riesgo: R17*; condición: C17-01.
- Técnica y derivación: Partición de equivalencia: campos requeridos de tipo cadena.
- Datos: Respuesta completa de /products/categories.
- Precondiciones: Servicio disponible.
- Resultado esperado: HTTP 200; arreglo no vacío; cada campo requerido es cadena no vacía.

Pasos:

1. GET /products/categories.
2. Recorrer todos los elementos.
3. Verificar slug, name y url.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-R17-02

**Unicidad y correspondencia de categorías**

- Riesgo: R17*; condición: C17-02.
- Técnica y derivación: Partición de equivalencia: slug único y ruta coherente.
- Datos: Todos los slugs y URLs del catálogo.
- Precondiciones: CT-R17-01 aprobado.
- Resultado esperado: Sin slugs duplicados; cada ruta corresponde al slug. No exigir capitalización estética no documentada.

Pasos:

1. Obtener catálogo.
2. Comparar número de slugs con número de valores distintos.
3. Analizar cada URL y comparar su ruta con /products/category/{slug}.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F01-01

**Login válido**

- Riesgo: F-R01; condición: CF01-1.
- Técnica y derivación: Partición de equivalencia; variación aislada respecto al control válido.
- Datos: username='emilys'; password='emilyspass'.
- Precondiciones: Cliente sin cookies; JSON válido.
- Resultado esperado: HTTP 200; accessToken y refreshToken no vacíos; username=emilys.

Pasos:

1. POST /auth/login con los datos del caso.
2. Registrar estado HTTP y cuerpo con tokens censurados.
3. Comparar con el resultado esperado.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F01-02

**Contraseña incorrecta**

- Riesgo: F-R01; condición: CF01-2.
- Técnica y derivación: Partición de equivalencia; variación aislada respecto al control válido.
- Datos: username='emilys'; password='qa_clave_incorrecta'.
- Precondiciones: Cliente sin cookies; JSON válido.
- Resultado esperado: HTTP 400 o 401; sin accessToken ni refreshToken.

Pasos:

1. POST /auth/login con los datos del caso.
2. Registrar estado HTTP y cuerpo con tokens censurados.
3. Comparar con el resultado esperado.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F01-03

**Usuario inexistente**

- Riesgo: F-R01; condición: CF01-3.
- Técnica y derivación: Partición de equivalencia; variación aislada respecto al control válido.
- Datos: username='qa_usuario_inexistente_9f73'; password='emilyspass'.
- Precondiciones: Cliente sin cookies; JSON válido.
- Resultado esperado: HTTP 400 o 401; sin tokens.

Pasos:

1. POST /auth/login con los datos del caso.
2. Registrar estado HTTP y cuerpo con tokens censurados.
3. Comparar con el resultado esperado.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F01-04

**Credenciales vacías**

- Riesgo: F-R01; condición: CF01-4.
- Técnica y derivación: Partición de equivalencia; variación aislada respecto al control válido.
- Datos: username=''; password=''.
- Precondiciones: Cliente sin cookies; JSON válido.
- Resultado esperado: HTTP 400 o 401; error de validación; sin tokens.

Pasos:

1. POST /auth/login con los datos del caso.
2. Registrar estado HTTP y cuerpo con tokens censurados.
3. Comparar con el resultado esperado.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F02-01

**Refresh válido**

- Riesgo: F-R02; condición: CF02-1.
- Técnica y derivación: Partición de equivalencia + transición de sesión.
- Datos: refreshToken recién emitido y expiresInMins=1
- Precondiciones: Login válido previo cuando aplique; sin cookies; no editar payload del JWT.
- Resultado esperado: HTTP 200; nuevo accessToken utilizable en /auth/me para el mismo usuario. No exigir que dos tokens emitidos en el mismo segundo sean diferentes.

Pasos:

1. Preparar el dato indicado.
2. POST /auth/refresh.
3. Registrar respuesta censurada.
4. Si hay accessToken en el caso positivo, verificar identidad mediante /auth/me.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F02-02

**Refresh ausente**

- Riesgo: F-R02; condición: CF02-2.
- Técnica y derivación: Partición de equivalencia + transición de sesión.
- Datos: JSON {} sin cookies
- Precondiciones: Login válido previo cuando aplique; sin cookies; no editar payload del JWT.
- Resultado esperado: HTTP 400, 401 o 403; sin emisión de tokens utilizables.

Pasos:

1. Preparar el dato indicado.
2. POST /auth/refresh.
3. Registrar respuesta censurada.
4. Si hay accessToken en el caso positivo, verificar identidad mediante /auth/me.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F02-03

**Refresh alterado**

- Riesgo: F-R02; condición: CF02-3.
- Técnica y derivación: Partición de equivalencia + transición de sesión.
- Datos: refreshToken con primer carácter de firma cambiado
- Precondiciones: Login válido previo cuando aplique; sin cookies; no editar payload del JWT.
- Resultado esperado: HTTP 400, 401 o 403; sin emisión de tokens utilizables.

Pasos:

1. Preparar el dato indicado.
2. POST /auth/refresh.
3. Registrar respuesta censurada.
4. Si hay accessToken en el caso positivo, verificar identidad mediante /auth/me.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F03-01

**Primer elemento**

- Riesgo: F-R03; condición: CF03-1.
- Técnica y derivación: Valores límite sobre desplazamiento [0,N-1]; limit=0 es clase especial.
- Datos: limit=1&skip=0
- Precondiciones: Obtener línea base GET /products?limit=0&skip=0; N=total, N>=1. Guardar orden e IDs; si cambia el conjunto, repetir la base.
- Resultado esperado: HTTP 200; exactamente un elemento si N>=1; su ID coincide con el primero de la línea base.

Pasos:

1. Sustituir N por el total observado.
2. Ejecutar GET /products?limit=1&skip=0.
3. Comparar IDs, tamaño y total con la línea base.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F03-02

**Último elemento**

- Riesgo: F-R03; condición: CF03-2.
- Técnica y derivación: Valores límite sobre desplazamiento [0,N-1]; limit=0 es clase especial.
- Datos: limit=1&skip=N-1
- Precondiciones: Obtener línea base GET /products?limit=0&skip=0; N=total, N>=1. Guardar orden e IDs; si cambia el conjunto, repetir la base.
- Resultado esperado: HTTP 200; exactamente el último elemento de la línea base.

Pasos:

1. Sustituir N por el total observado.
2. Ejecutar GET /products?limit=1&skip=N-1.
3. Comparar IDs, tamaño y total con la línea base.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F03-03

**Después del último elemento**

- Riesgo: F-R03; condición: CF03-3.
- Técnica y derivación: Valores límite sobre desplazamiento [0,N-1]; limit=0 es clase especial.
- Datos: limit=1&skip=N
- Precondiciones: Obtener línea base GET /products?limit=0&skip=0; N=total, N>=1. Guardar orden e IDs; si cambia el conjunto, repetir la base.
- Resultado esperado: HTTP 200; products=[]; total=N.

Pasos:

1. Sustituir N por el total observado.
2. Ejecutar GET /products?limit=1&skip=N.
3. Comparar IDs, tamaño y total con la línea base.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F03-04

**Límite cero documentado**

- Riesgo: F-R03; condición: CF03-4.
- Técnica y derivación: Valores límite sobre desplazamiento [0,N-1]; limit=0 es clase especial.
- Datos: limit=0&skip=0
- Precondiciones: Obtener línea base GET /products?limit=0&skip=0; N=total, N>=1. Guardar orden e IDs; si cambia el conjunto, repetir la base.
- Resultado esperado: HTTP 200; longitud de products=N; sin IDs duplicados.

Pasos:

1. Sustituir N por el total observado.
2. Ejecutar GET /products?limit=0&skip=0.
3. Comparar IDs, tamaño y total con la línea base.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F04-01

**ID existente**

- Riesgo: F-R04; condición: CF04-1.
- Técnica y derivación: Partición de equivalencia: identificador existente / inexistente.
- Datos: 1
- Precondiciones: Línea base de IDs capturada; confirmar ausencia del ID negativo.
- Resultado esperado: HTTP 200; objeto con id=1 y título de tipo cadena no vacío.

Pasos:

1. Determinar el ID del caso.
2. GET /products/{id}.
3. Comparar estado y estructura JSON.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F04-02

**ID inexistente**

- Riesgo: F-R04; condición: CF04-2.
- Técnica y derivación: Partición de equivalencia: identificador existente / inexistente.
- Datos: max(ID de línea base)+100000
- Precondiciones: Línea base de IDs capturada; confirmar ausencia del ID negativo.
- Resultado esperado: HTTP 404; cuerpo de error sin objeto de producto válido.

Pasos:

1. Determinar el ID del caso.
2. GET /products/{id}.
3. Comparar estado y estructura JSON.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F05-01

**Búsqueda con coincidencia conocida**

- Riesgo: F-R05; condición: CF05-1.
- Técnica y derivación: Partición de equivalencia: consulta con / sin coincidencias.
- Datos: Título completo del producto 1, codificado como parámetro q
- Precondiciones: Línea base actual disponible.
- Resultado esperado: HTTP 200; el producto 1 aparece en products; la respuesta es JSON con total coherente.

Pasos:

1. Preparar el texto de consulta del caso.
2. Codificar q en URL.
3. GET /products/search?q={q}&limit=0.
4. Comparar con el resultado esperado.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.

## CT-F05-02

**Búsqueda sin coincidencias**

- Riesgo: F-R05; condición: CF05-2.
- Técnica y derivación: Partición de equivalencia: consulta con / sin coincidencias.
- Datos: qa_sin_coincidencias_ + UUID
- Precondiciones: Línea base actual disponible.
- Resultado esperado: HTTP 200; products=[] y total=0. Confirmar antes que el marcador no figure en títulos ni descripciones de la línea base.

Pasos:

1. Preparar el texto de consulta del caso.
2. Codificar q en URL.
3. GET /products/search?q={q}&limit=0.
4. Comparar con el resultado esperado.

Evidencia y fecha: [registro de ejecución](registro-ejecucion.md). Estado: Aprobado. Postcondición: cerrar sesión local y eliminar tokens temporales cuando corresponda; no intentar restaurar una base externa.
