# Proyecto final de Pruebas de Software

**Evaluación de la API DummyJSON mediante pruebas basadas en riesgos.**

Miguel Ángel Noreña Cano, Marlon Maldonado y Aldair Estiven Novoa  
Institución Universitaria Pascual Bravo  
Docente: Roberto José Calderón Bermejo  
Fecha: 19 de noviembre de 2026

## Documentos de entrega

- **[Informe final](https://docs.google.com/document/d/14eZrwDed-F5Lf6CiXBdScSnbSLmlF25YsoXzNlJ_lUc/edit)**
- **[Presentación en Canva](https://canva.link/nu7c94jstfmkzp2)**

## Qué es DummyJSON y qué evaluamos

[DummyJSON](https://dummyjson.com/) es una API REST pública de práctica con datos ficticios. Una API permite que un programa solicite datos u operaciones a un servicio. Un endpoint es su ruta concreta; por ejemplo, `GET /products/1` consulta un producto.

HTTP transporta las solicitudes y respuestas. GET consulta, POST envía datos, PATCH modifica parcialmente y DELETE solicita una eliminación. JSON es el formato de los datos intercambiados.

El objeto del proyecto es comprobar autenticación, consultas de productos y escrituras simuladas. DummyJSON refleja las escrituras en su respuesta y conserva el estado original en una lectura posterior. Las expectativas se contrastan con su [documentación](https://dummyjson.com/docs/products).

## De dónde salieron los 24 casos

Se diseñaron usando la guía de la asignatura, la documentación de DummyJSON y la matriz de riesgos. La guía pide de 20 a 24 casos; el expediente contiene 24.

1. Identificar y priorizar un riesgo.
2. Traducirlo en una condición observable.
3. Aplicar equivalencia, valores límite o transición de estados para elegir las entradas.
4. Documentar el caso y su resultado esperado, ejecutarlo y conservar evidencia.

En **CT-R07-02**, nuestra convención significa:

| Parte | Significado |
|---|---|
| CT | Caso de prueba |
| R07 | Riesgo de falsa persistencia |
| 02 | Segundo caso asociado a ese riesgo |

C07-02 identifica la condición correspondiente. En CT-F01-01, F01 identifica el grupo funcional de login, vinculado con F-R01. Los identificadores relacionan documentación, código y evidencia.

## Cómo usamos Python

El script usa la biblioteca estándar: `urllib.request` envía solicitudes, `json` interpreta respuestas y `require` comprueba el estado HTTP y los campos esperados.

**Seis casos tienen ejecución automatizada en Python. Los otros 18 son diseños manuales ejecutados mediante inspección HTTP asistida.** Los registros conservan las solicitudes y respuestas con datos sensibles censurados.

Una consulta obtiene datos; una prueba compara el resultado observado con un criterio definido previamente.

## Cómo interpretar los resultados

Un caso negativo puede aprobar al recibir el rechazo esperado: consultar un perfil sin token debe devolver 401/403 sin datos del perfil. Un HTTP 200 tampoco basta si el contenido es incorrecto.

Resultado histórico del **9 de noviembre de 2026: 24 ejecutados, 23 aprobados y 1 fallido**. [INC-001](https://github.com/drakcore12/proyecto-final-de-pruebas-de-software-/issues/1): una firma JWT alterada produjo HTTP 500 dos veces frente a 401/403 esperado, sin acceso al perfil. El hallazgo sigue abierto.

## Ejecución de las pruebas

Con Python 3.10 o posterior, descarga o clona el repositorio y abre una terminal en su carpeta raíz. Para ejecutar los seis automatizados:

```bash
python tests/pruebas_api.py
```

Para ejecutar únicamente el ejemplo de modificación simulada:

```bash
python tests/pruebas_api.py CT-R07-02
```

El ejemplo obtiene T0 mediante GET, recibe T1 mediante PATCH y confirma T0 con un GET independiente. Cada ejecución guarda un registro nuevo en `evidencias/`. Los datos del servicio pueden cambiar; los registros históricos conservan su fecha y procedencia.

## Anexos técnicos

- [Plan completo en Markdown](docs/plan-de-pruebas.md).
- [24 casos, condiciones y trazabilidad](docs/casos-y-trazabilidad.md).
- [Script de seis pruebas](tests/pruebas_api.py).
- [Resultados consolidados por caso](evidencias/resultados-consolidados.json).
- [Evidencias originales y capturas](evidencias).

