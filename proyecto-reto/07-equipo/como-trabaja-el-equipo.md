# Cómo trabaja el equipo

> Actualizado 2026-08-25. Sustituye la versión anterior, que se escribió antes de
> que existieran el repositorio de GitHub y el tablero de avance.

## El reparto

```
   EQUIPO (todos)                RODRIGO              CLAUDE (solo Rodrigo)
   ─────────────                 ────────             ─────────────────────
   GitHub  ──── sube ──────────► lee/valida ────────► lee el repo, indexa
   Notion  ──── captura ───────►                      y detecta avance
   Tablero ──── tacha ─────────►                 ◄──  genera PO, OF, documentos
   Teams   ──── platica ───────► publica ◄──────────
   Canvas  ──── entrega
```

**Nadie necesita cuenta de Claude.** El equipo trabaja en GitHub, Notion y el
tablero; Claude lee de ahí, genera los documentos y los devuelve al repositorio.

---

## Los cuatro lugares

| Herramienta | Qué vive ahí | Link |
|---|---|---|
| **GitHub** | Documentación, códigos, planos en PDF, cotizaciones. La fuente de verdad. | https://github.com/Giovann1-C/Ciberf-sicos-7mo |
| **Tablero** | Avance visual de las 54 tareas y los 6 hitos. | https://claude.ai/code/artifact/60424a47-dd4a-4886-b8c6-f7c64939065b |
| **Notion** | Tareas del día a día, BOM y compras. | https://app.notion.com/p/3c763d9e84498109aed6f0ff6afd4849 |
| **Canvas** | Entregas oficiales. Lo único que se califica. | https://experiencia21.tec.mx/courses/707419 |
| **Diagramas** | Arquitectura de la celda, para entender qué hace tu parte. | https://claude.ai/code/artifact/a16da71d-e2ac-409e-bad1-41566dfaaa90 |
| **Teams** | Conversación diaria y archivos pesados de CAD. | (canal del equipo) |

---

## La regla que hace que todo funcione

**Nombra los archivos con la palabra que declara su estado.**

| Subes… | El tablero marca… |
|---|---|
| `chasis-agv.pdf` | **En curso** — hubo trabajo, no consta que esté cerrado |
| `chasis-agv-final.pdf` | **Hecha** y tachada |

Palabras que cierran una tarea:
`final` · `aprobado` · `firmado` · `liberado` · `validado` · `entregado` · `terminado`

Es la única cosa que cambia respecto a como veníamos trabajando. Con eso, el
tablero se actualiza con el trabajo real en lugar de con recordatorios.

**Nombra en kebab-case, sin acentos ni espacios:** `qa-dinamico-validado.pdf`,
no `QA Dinámico (final) v3 FINAL.pdf`.

---

## Qué va y qué no va a GitHub

**Sí:** documentación, códigos (ROS 2, firmware NXP, scripts), planos en PDF,
cotizaciones, órdenes de compra, protocolos y resultados de pruebas.

**No:** CAD pesado, ZIP, STEP y video → van a Teams. Material de clase con
derechos de los profesores. Contraseñas o tokens de cualquier tipo. Datos
personales de cualquiera de nosotros.

> ⚠️ **El repositorio es público.** Cualquiera en internet lo ve y el historial de
> git es permanente: borrar un archivo después no lo quita del historial. Antes de
> subir algo, pregúntate si te incomodaría que lo viera un desconocido.

El `.gitignore` ya bloquea binarios pesados y credenciales, pero no sustituye al
criterio de cada quien.

---

## Reglas de captura en Notion

1. Cada quien actualiza **su** fila. No edites la de otro sin avisar.
2. Si algo te bloquea, ponlo en `Bloqueado` y escribe por qué en Notas.
   **Una tarea bloqueada en silencio es la que hunde el proyecto.**
3. Cotizaciones: actualiza `Proveedor`, `Costo unitario` y `Lead time` en la base
   **BOM y Compras**. Cuando los tres estén, ya se puede emitir la orden.
4. `Bloquea a` no es decorativo: define la ruta crítica.

---

## El ritmo de la semana

| Cuándo | Qué pasa | Quién |
|---|---|---|
| Lunes | Junta de avance. Actualizamos Notion con lo hecho y lo atorado | Todos |
| Al terminar algo | Subes el archivo a GitHub con el nombre correcto | Quien lo hizo |
| Al cotizar | Actualizas proveedor, costo y lead time en el BOM | Quien cotiza |
| Cuando haya que comprar | Se emite la orden y queda registrada | Rodrigo |
| Viernes | Revisión de riesgos y avance contra el plan | Todos |

---

## Cómo se convierte el trabajo en avance

Cuando alguien sube algo a GitHub:

1. Rodrigo corre `python sistema/avance.py` (o le pide a Claude *"revisa el avance"*)
2. El sistema baja el repo, cruza los archivos contra el mapa de evidencias
   y propone qué tareas mover
3. Se aplica, queda **bitácora** de qué archivo movió qué tarea
   (`05-calidad/bitacora-evidencias.md` — eso es trazabilidad para el profe)
4. Se republica el tablero y todos ven el cambio

**Un archivo prueba que hubo trabajo, no que la tarea esté cerrada.** Por eso la
promoción a "hecha" exige la palabra de cierre en el nombre, o que una persona lo
confirme. El sistema no adivina.

Si subiste algo que obviamente demuestra una tarea y el tablero no se movió, el
problema es el patrón, no tu archivo: dile a Rodrigo y se agrega a
`sistema/evidencias.json`.

---

## Órdenes de compra automáticas

Se generan en el formato exacto de las plantillas del profesor:

```bash
python herramientas/erp.py estado
python herramientas/erp.py po --proveedor "Nexus" --items "MEC-RUE-MECANUM-100:4"
python herramientas/erp.py of --parte "AGV Mecanum" --cantidad 1 --entrega 2026-10-18
```

**Ninguna compra sin orden registrada.** Es lo que nos van a pedir demostrar.

---

## Lo que NO hay que hacer

- **No compartir la cuenta de Claude.** Ni la contraseña, ni la sesión.
- **No duplicar el BOM** en un Excel suelto. Si vive en dos lados, uno está mal.
- **No comprar sin PO registrada.**
- **No subir archivos pesados a GitHub.** Se vuelve lento para todos.
- **No dejar una tarea bloqueada sin avisar.**
