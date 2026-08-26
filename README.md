# Ciberfísicos 7.º — Reto: Celda ciberfísica de alimentación robotizada

Concentración en Sistemas Ciberfísicos · **MR3005C.601** · Tec de Monterrey Guadalajara · Ago–Dic 2026

AGV omnidireccional con ruedas mecanum + brazo colaborativo sobre riel lineal + visión
industrial, coordinados con un **CNC Haas** por MTConnect. Control PI/PD/PID sobre
microcontrolador **NXP S32K312**.

**16 semanas · 36 % de la calificación (4 evidencias individuales) · 0 días de holgura.**

---

## ⚠️ Lo que manda el calendario

**La ruta crítica son las compras, no el software.** El riel lineal y el LiDAR tardan
**6 semanas** en llegar.

| Si la PO sale... | El material llega... | Semanas para integrar y validar |
|---|---|---|
| **6 de septiembre** | 18 de octubre | **7** ✅ |
| 27 de septiembre | 8 de noviembre | 3 ❌ |

Las fases no se comprimen: se recorta el final, que es donde viven las tres evidencias
que más pesan. **Hito H1 — emitir las PO críticas antes del 6 de septiembre.**

Mientras el material viaja, lo que **no** está en la ruta crítica avanza sin bloqueo:
CAD y planos, Nav2 y SLAM en Gazebo, cliente MTConnect contra agente simulado,
algoritmo de visión sobre fotos, simulación en FlexSim.

---

## Herramientas del equipo

| Herramienta | Para qué | Link |
|---|---|---|
| **Tablero de avance** | Marcar tareas y ver cómo vamos. 54 tareas, 6 hitos | [abrir](https://claude.ai/code/artifact/60424a47-dd4a-4886-b8c6-f7c64939065b) |
| **Diagramas** | Entender la celda: arquitectura, ciclo, cronograma | [abrir](https://claude.ai/code/artifact/a16da71d-e2ac-409e-bad1-41566dfaaa90) |
| **Notion** | Tareas del día a día, BOM y compras | [abrir](https://app.notion.com/p/3c763d9e84498109aed6f0ff6afd4849) |
| **Canvas** | Entregas oficiales. Lo único que se califica | [abrir](https://experiencia21.tec.mx/courses/707419) |

---

## 📌 Cómo nombrar los archivos

**El nombre del archivo es la señal de estado.** El sistema lo lee y actualiza el
tablero solo: nadie tiene que reportar avance a mano.

| Subes… | El tablero marca… |
|---|---|
| `chasis-agv.pdf` | **En curso** — hubo trabajo, no consta que esté cerrado |
| `chasis-agv-final.pdf` | **Hecha** y tachada |

Palabras que cierran una tarea:
`final` · `aprobado` · `firmado` · `liberado` · `validado` · `entregado` · `terminado`

Nombres en kebab-case, sin acentos ni espacios: `qa-dinamico-validado.pdf`,
no `QA Dinámico (final) v3 FINAL.pdf`.

> Si subiste algo que obviamente demuestra una tarea y el tablero no se movió,
> el problema es el patrón, no tu archivo: avísale a Rodrigo y se agrega a
> `herramientas/evidencias.json`.

---

## Qué hay aquí

```
proyecto-reto/
├── 01-planeacion/
│   ├── pmi-plan-direccion-proyecto.md    Plan PMBOK completo (13 secciones)
│   └── plan-de-trabajo.md                Fases, ruta crítica y riesgos
├── 02-proveeduria/
│   ├── catalogo-materiales.csv           BOM con código ERP y lead times
│   └── fichas/<CÓDIGO>/                  Ficha técnica y cotizaciones por material
├── 03-compras/
│   ├── ordenes/                          Órdenes de compra emitidas (.xlsx)
│   └── registro-po.csv                   Bitácora de PO con fecha estimada de llegada
├── 04-fabricacion/
│   ├── ordenes-fabricacion/              Registro de OF
│   └── hojas-viajeras/                   Hojas viajeras por estación (.xlsx)
├── 05-calidad/                           Protocolos y evidencia de QA
├── 06-documentacion/
│   ├── diagrama-celda.html               5 diagramas de arquitectura
│   ├── tablero-avance.html               Tablero interactivo de tareas
│   └── reto-celda-ciberfisica.pptx       Presentación del proyecto
└── 07-equipo/
    └── como-trabaja-el-equipo.md         Reglas de colaboración

herramientas/
├── erp.py                                ERP: códigos, PO, OF y hojas viajeras
└── generar-presentacion.py               Regenera la presentación
```

## Cómo usar el ERP

Genera órdenes de compra y hojas viajeras en el formato exacto de las plantillas del
profesor, numeradas y registradas automáticamente.

```bash
# Ver estado: catálogo, riesgos de entrega, PO emitidas, qué falta cotizar
python herramientas/erp.py estado

# Alta de un material (el código ERP se genera solo)
python herramientas/erp.py material --categoria MECANICA --tipo Rueda \
  --parte MEC-100 --desc "Rueda mecanum 100 mm" --marca Nexus --costo 1800 --lead 3

# Emitir una orden de compra
python herramientas/erp.py po --proveedor "Nexus Robot" --contacto "Ventas" \
  --email ventas@ejemplo.mx --items "MEC-RUE-MECANUM-100:4,INS-LID-2D-360:1"

# Liberar orden de fabricación + hoja viajera
python herramientas/erp.py of --parte "AGV Mecanum" --cantidad 1 --entrega 2026-10-18
```

Requiere `pip install openpyxl`.

## Cómo se convierte lo que suben en avance

```bash
# Baja el repo, cruza los archivos contra el mapa de evidencias y reporta
python herramientas/avance.py

# Aplica los cambios al tablero y deja bitácora
python herramientas/avance.py --aplicar --sin-pull
```

El mapa vive en `herramientas/evidencias.json`: dice qué fragmento de nombre de
archivo demuestra qué tarea. Es texto plano, se edita sin tocar código.

Dos criterios que protegen la honestidad del tablero:

1. **Coincidencia por límite de palabra.** `slam` no casa con `slamtec` — sin esto,
   una orden de compra al proveedor Slamtec marcaba SLAM como resuelto.
2. **Un archivo prueba trabajo, no cierre.** Solo sube a "hecha" si el nombre lo
   declara terminado; lo demás queda "en curso" para que lo revise una persona.

Cada corrida deja registro en `proyecto-reto/05-calidad/bitacora-evidencias.md`
de qué archivo movió qué tarea. **Eso es la trazabilidad que evalúa el profesor.**

## Reglas del repositorio

- **Los archivos pesados no van aquí.** CAD, ZIP, STEP, video y PDFs grandes viven en
  Teams/SharePoint. El `.gitignore` ya los bloquea para que el repo siga siendo rápido
  de clonar.
- **Este repositorio es público.** No subas material de clase con derechos de los
  profesores, datos personales, ni credenciales. `canvas-token.txt` y `*.env` están
  bloqueados por si acaso.
- **Nada de compras sin PO registrada.** El profesor evalúa la trazabilidad, no solo
  que el AGV camine.
- Cada quien hace commit de lo suyo con mensajes que digan **qué** cambió y **por qué**.

## Dónde vive cada cosa

| Contenido | Herramienta |
|---|---|
| Documentación, códigos, planos PDF, cotizaciones | **GitHub** (aquí) |
| Avance de las 54 tareas y los 6 hitos | **Tablero** |
| Tareas del día a día, BOM y compras | **Notion** |
| Conversación y archivos pesados de CAD | **Teams / SharePoint** |
| Entregas oficiales y evidencias | **Canvas** |

Detalle completo de cómo trabajamos:
[`proyecto-reto/07-equipo/como-trabaja-el-equipo.md`](proyecto-reto/07-equipo/como-trabaja-el-equipo.md)

