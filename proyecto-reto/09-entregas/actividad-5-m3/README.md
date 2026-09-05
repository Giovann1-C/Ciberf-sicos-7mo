# Actividad 5 — Módulo 3, Administración de Proyectos

**Proyecto:** Sistema de automatización para talleres de CNC
**Curso:** MR3005C.601 — Sistemas Ciber-Físicos · Ago–Dic 2026

**Equipo:** 
Rodrigo Herrera Baños A01738608 · 
Osmar Artemio Gonzalez Alatorre A01645216 ·
Samuel Sebastian Vázquez Gasca A01639337 · 
Diego Giovanni Castellanos García A01639992 · 
Perla Cecilia Rentería Rodríguez A01645074
**Fecha de entrega:** 2026-09-04

Índice de los ocho entregables de la actividad. Cada enlace va al archivo real
dentro de este mismo repositorio; aquí no hay copias, para que no existan dos
versiones del mismo documento.

---

## 1 · Carta Proyecto con datos del socio formador

- 📄 **[Ver en pantalla (Markdown)](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/01-planeacion/carta-proyecto.md)** ← recomendado, GitHub lo renderiza
- 📎 [Descargar en Word](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/01-planeacion/Carta-Proyecto-Automatizacion-CNC.docx)

Incluye problemática, objetivo general y específicos, alcance, entregables,
restricciones, cronograma de 18 semanas y matriz de 13 riesgos.

> Los campos del socio formador (organización, representante, contacto) están
> marcados como pendientes: se completan tras la reunión de definición.

## 2 · Sistema ERP

- 🔧 **[Código del ERP](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/herramientas/erp.py)** — alta de materiales, emisión de PO y OF, recepción y estado
- 📁 [Carpeta de proveeduría](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/02-proveeduria)
- 📊 [Catálogo de materiales](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/02-proveeduria/catalogo-materiales.csv) — 21 partidas con costo, lead time, proveedor y estado

Uso: `python herramientas/erp.py {estado|material|po|of|recibir|actualizar}`

## 3 · Órdenes de fabricación (OF)

- 📁 **[Carpeta de fabricación](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/04-fabricacion)**
- 📋 [Registro de OF](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/04-fabricacion/ordenes-fabricacion/registro-of.csv)
- 📄 [Hoja viajera OF-2026-AGV-001](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/04-fabricacion/hojas-viajeras/OF-2026-AGV-001_hoja-viajera.xlsx)

## 4 · Órdenes de compra (PO)

- 📁 **[Carpeta de compras](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/03-compras)**
- 📋 [Registro de PO](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/03-compras/registro-po.csv) — tres órdenes emitidas
- 📁 [Órdenes emitidas](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/03-compras/ordenes)
- 📖 [Procedimiento de emisión](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/03-compras/como-emitir-una-orden.md)

## 5 · Repositorios mapeados por área

- 📁 **[Mapa de módulos de software](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/08-software)**

Siete áreas funcionales, cada una con alcance, regla de diseño y responsable:

| Área | Alcance |
|---|---|
| [Librerías](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/08-software/librerias) | Código reutilizable: cinemática, filtros, utilidades |
| [Comunicación](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/08-software/comunicacion) | Enlace con la CNC, MQTT, serie MCU↔supervisor |
| [Control](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/08-software/control) | Lazos PI, PD y PID sobre el S32K312 |
| [Navegación](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/08-software/navegacion) | SLAM, planeación de trayectorias, acoplamiento |
| [Visión](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/08-software/vision) | Calibración y verificación de pieza |
| [Diagnóstico](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/08-software/diagnostico) | Registro de eventos, telemetría, autoprueba |
| [Seguridad](https://github.com/Giovann1-C/Ciberf-sicos-7mo/tree/main/proyecto-reto/08-software/seguridad) | Paro de emergencia, parada segura, ciberseguridad |

El módulo de seguridad **no depende de ningún otro**: un fallo en cualquier parte
del sistema no debe impedir que el paro de emergencia funcione.

## 6 · Arquitectura del proyecto

- 🖼️ **[Diagrama interactivo](https://claude.ai/code/artifact/a16da71d-e2ac-409e-bad1-41566dfaaa90)**
- 📄 [Fuente del diagrama](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/06-documentacion/diagrama-celda.html)

## 7 · Diagrama de flujo con actividades del socio formador

⏳ **Pendiente.** Requiere la definición de actividades por parte del socio
formador. El guion de la reunión está preparado en
[preguntas-socio-formador.md](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/01-planeacion/preguntas-socio-formador.md).

## 8 · Tablero Kanban

- 📋 **[Tablero de avance del Reto](https://claude.ai/code/artifact/60424a47-dd4a-4886-b8c6-f7c64939065b)**

---

## Documentos de respaldo

No forman parte de los ocho entregables, pero sustentan lo anterior:

- [Plan de dirección del proyecto (PMBOK)](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/01-planeacion/pmi-plan-direccion-proyecto.md) — alcance, WBS, RACI, riesgos, comunicaciones
- [Plan de trabajo por fases](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/01-planeacion/plan-de-trabajo.md)
- [Cómo trabaja el equipo](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/07-equipo/como-trabaja-el-equipo.md)
- [Bitácora de evidencias](https://github.com/Giovann1-C/Ciberf-sicos-7mo/blob/main/proyecto-reto/05-calidad/bitacora-evidencias.md)

## Estado de la entrega

| # | Entregable | Estado |
|---|---|---|
| 1 | Carta Proyecto | ✅ Entregado |
| 2 | Sistema ERP | ✅ Entregado |
| 3 | Órdenes de fabricación | ✅ Entregado |
| 4 | Órdenes de compra | ✅ Entregado |
| 5 | Repositorios por área | ✅ Entregado |
| 6 | Arquitectura | ✅ Entregado |
| 7 | Diagrama de flujo del socio formador | ⏳ Pendiente de la reunión |
| 8 | Tablero Kanban | ✅ Entregado |
