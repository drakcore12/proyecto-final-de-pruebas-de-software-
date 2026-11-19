# Proyecto final de Pruebas de Software

**Evaluación de la API DummyJSON mediante pruebas basadas en riesgos.**

Miguel Ángel Noreña Cano, Marlon Maldonado y Aldair Estiven Novoa  
Institución Universitaria Pascual Bravo  
Docente: Roberto José Calderón Bermejo  
Sustentación: 19 de noviembre de 2026

## Documentos de entrega

- **[Informe final](https://docs.google.com/document/d/14eZrwDed-F5Lf6CiXBdScSnbSLmlF25YsoXzNlJ_lUc/edit)**
- **[Presentación en Canva](https://canva.link/nu7c94jstfmkzp2)**
- [Guion de sustentación](https://docs.google.com/document/d/1AL-onFcuFjaQSweLnWfU2dE-hFODnr8a7ICzhR0Z6kI/edit)

## Anexos técnicos

- [Plan completo en Markdown](docs/plan-de-pruebas.md).
- [24 casos y trazabilidad](docs/casos-y-trazabilidad.md).
- [Código de las seis pruebas automatizadas](tests/pruebas_api.py).
- [Resultados por caso](evidencias/resultados-consolidados.json).
- [Evidencias originales y capturas](evidencias).

El informe reúne el plan, el método, los riesgos, las reglas de decisión, la estimación, el cronograma y las conclusiones. Los anexos se conservan en GitHub para contrastar cada resultado.

## Resultado del ciclo del 9 de noviembre de 2026

**24 ejecutados, 23 aprobados y 1 fallido.** Seis casos automatizados y 18 diseños manuales con ejecución mediante inspección HTTP asistida.

[INC-001](https://github.com/drakcore12/proyecto-final-de-pruebas-de-software-/issues/1): firma JWT alterada, HTTP 500 observado dos veces frente a 401/403 esperado, sin acceso al perfil. El hallazgo permanece abierto.

## Reproducción

Con Python 3.10 o posterior, desde la raíz:

```bash
python tests/pruebas_api.py
```

Demostración de modificación simulada:

```bash
python tests/pruebas_api.py CT-R07-02
```

Cada ejecución guarda un registro nuevo en `evidencias/`. Los datos del servicio pueden cambiar. Los registros originales se conservan con su fecha y procedencia.

## Distribución de la exposición

Portada y objetivo: cualquiera. Miguel presenta las diapositivas 3–5; Marlon, 6–8; Aldair, 9–11. El guion se organiza en tres bloques consecutivos.

## Seguimiento

Los commits registran los cambios y las [Issues](https://github.com/drakcore12/proyecto-final-de-pruebas-de-software-/issues) reúnen los hallazgos y las tareas. La versión documental 3.1 conserva el informe principal en Google Docs y una versión del plan en Markdown, con los subapartados de la guía del proyecto. Los commits registran cada versión publicada en el repositorio.
