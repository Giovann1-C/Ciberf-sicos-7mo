# Documentación del Reto

| Archivo | Qué es | Para quién |
|---|---|---|
| `../01-planeacion/pmi-plan-direccion-proyecto.md` | **Plan de dirección PMBOK completo** — 13 secciones, de acta de constitución a diseño técnico por subsistema | Rodrigo y los docentes |
| `../01-planeacion/plan-de-trabajo.md` | Fases, ruta crítica y riesgos en versión corta | Todos |
| `diagrama-celda.html` | Página con los 5 diagramas. **Publicada como Artifact:** https://claude.ai/code/artifact/a16da71d-e2ac-409e-bad1-41566dfaaa90 | Equipo, por link |
| `reto-celda-ciberfisica.pptx` | Presentación de 17 diapositivas | Equipo y socio formador |

## Regenerar

```
python sistema/generar-presentacion.py "proyecto-reto/06-documentacion/reto-celda-ciberfisica.pptx"
```

El diagrama se actualiza republicando `diagrama-celda.html` como Artifact — conserva
el mismo link, así que el equipo no tiene que volver a guardarlo.

## Los 5 diagramas
1. Cronograma con los dos escenarios de compra
2. Arquitectura física de la celda y capas de red
3. Tres capas de cómputo y canal de seguridad
4. Máquina de estados del ciclo
5. Flujo de trabajo del equipo con Claude
