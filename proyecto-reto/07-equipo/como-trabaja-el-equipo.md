# Cómo trabaja el equipo

## El reparto

```
   EQUIPO (todos)            RODRIGO              CLAUDE (solo Rodrigo)
   ─────────────             ────────             ─────────────────────
   Notion  ──── escribe ───► lee/valida ────────► lee Notion
   Teams   ──── platica ───►                      genera PO, OF, planes,
   Canvas  ──── entrega ───►                 ◄──  documentos, análisis
                             publica ◄──────────
```

**Nadie necesita cuenta de Claude.** El equipo trabaja en Notion; yo leo de ahí,
genero los documentos y los devuelvo a Notion y a Teams.

## Notion — la fuente de verdad del equipo

Página: **Reto — Celda Ciberfísica AGV + Cobot + Visión**
- **Tareas del Equipo** — WBS con responsable, fase, estado, fecha y qué bloquea
- **BOM y Compras** — 20 materiales con código ERP, proveedor, lead time y estado

**Para dar acceso:** en la página, botón *Share* → *Invite* → correo de cada
integrante. En el plan gratuito de Notion caben hasta 10 personas con permiso de
edición. Dales acceso a la página del Reto, **no** a `Sistema Académico` (ahí
están tus calificaciones y entregas personales).

### Reglas de captura
1. Cada quien actualiza **su** fila. No edites la de otro sin avisar.
2. Si algo te bloquea, ponlo en `Bloqueado` y escribe por qué en Notas. Una
   tarea bloqueada en silencio es la que hunde el proyecto.
3. Cotizaciones: actualiza `Proveedor`, `Costo unitario` y `Lead time` en BOM.
   Cuando los tres estén, ya se puede emitir la PO.
4. `Bloquea a` no es decorativo: define la ruta crítica.

## Teams — la conversación y los archivos pesados

- **Pestaña de Notion en Teams:** en el canal del equipo, `+` → busca *Notion* →
  pega la URL de la página del Reto. Queda embebida y nadie tiene que cambiar de
  app.
- **Archivos pesados (CAD, STEP, SolidWorks)** viven en la pestaña Archivos del
  canal (SharePoint), **no** en Notion. Notion es para datos, no para 40 MB de
  CAD.
- **Reuniones:** graba las de decisión. Las decisiones que solo existen en la
  memoria de alguien se pierden.

## Canvas — lo oficial
Las evidencias y actividades se entregan **solo** ahí. Notion y Teams son
herramientas de trabajo, no de entrega.

## Cómo pido documentos generados

Yo (Rodrigo) le digo a Claude:

| Le digo | Qué hace |
|---|---|
| `estado del reto` | Lee el catálogo y las PO, dice qué está en riesgo |
| `emite la PO del LiDAR a <proveedor>` | Genera el .xlsx en el formato del profe y lo registra |
| `libera la OF del AGV` | Orden de fabricación + hoja viajera con las 7 estaciones |
| `agrega material <lo que sea>` | Código ERP autogenerado + ficha de proveeduría |
| `baja Notion al sistema` | Sincroniza lo que capturó el equipo con los archivos |

Los archivos generados se suben a Teams para que todos los vean.

## Lo que NO hay que hacer
- **No dupliques el BOM** en Excel suelto. Si vive en dos lados, uno está mal.
- **No hagas compras sin PO registrada.** El profe evalúa la trazabilidad, no
  solo que el AGV camine.
