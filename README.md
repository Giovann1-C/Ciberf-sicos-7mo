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
| Documentación, ERP, código | **GitHub** (aquí) |
| Tareas, BOM, seguimiento diario | **Notion** |
| Conversación y archivos pesados de CAD | **Teams / SharePoint** |
| Entregas oficiales y evidencias | **Canvas** |

