# Seguimiento y Trazabilidad — Resumen ejecutivo

**Proyecto:** Celda ciberfísica de manufactura: MoMa (AGV mecanum + brazo de 4 GDL), cobot sobre riel lineal y visión
**Curso:** Sistemas ciber-físicos · MR3005C.601 · Módulo 3, Administración de Proyectos
**Equipo:** Perla Cecilia Rentería Rodríguez · Samuel Sebastián Vázquez Gasca · Osmar Artemio González Alatorre · Rodrigo Herrera Baños · Diego Giovanni Castellanos García
**Corte de información:** 2026-10-10 · Fase F3 (Fabricación y subensambles, 28 sep – 25 oct)

---

## Estado global

| Frente | Estado | Lectura rápida |
|---|---|---|
| Programación y software | 🟡 En curso | Ya hay control de motor real con NXP + RoboClaw. Navegación, visión y brazo siguen sin código |
| Compras y materiales | 🟢 Controlado | 5 OC recibidas y 5 canceladas. Los críticos de lead largo ya los entregó el Socio Formador. **Falta la SBC** |
| Fabricación | 🟢 Avance | 6 de 7 OF fabricadas (brazo y chasis) |
| Ensambles y trazabilidad | 🔴 Atrasado | Ningún subensamble iniciado. Las piezas no tienen identificación física |
| Calidad | 🟡 Parcial | Los controles de diseño están hechos. Faltan las inspecciones dimensionales y las firmas en las hojas viajeras |

---

## 1. Avances de programación y software

**Decisión de arquitectura (CC-002).** El AGV usa **2 drivers RoboClaw ST 2x45A**, de dos canales cada uno, para los 4 motores mecanum.

- El lazo de control **PI/PID corre en el NXP S32K312**.
- La comunicación es por UART en *Packet Serial*: el MCU lee la velocidad del encoder (comando 18, qpps) y envía el duty (comando 32).
- Las protecciones del RoboClaw quedan activas: E-stop físico en S3, *Serial Timeout* y límites de voltaje y corriente.

| Fecha | Logro | Evidencia |
|---|---|---|
| 2026-09-25 | **Un motor del AGV (CHP 42GP-775) se movió en lazo cerrado** desde el S32K312 vía RoboClaw | Firmware en S32DS (HAL, driver RoboClaw, control) |
| 2026-09-25 | Identificación de la planta: respuesta lineal, 4400 qpps por unidad de duty | Escalones al 25/50/75/100 % |
| 2026-09-25 | Modelo FOPDT y PI por SIMC: $K_p \approx 3.0\times10^{-4}$, $K_i \approx 2.9\times10^{-3}$, lazo a 100 Hz | $G(s)=\dfrac{4400\,e^{-0.028s}}{0.104s+1}$ |
| 2026-10-03 | **Laboratorio NXP + RoboClaw.** Comunicación y telemetría validadas con la batería del AGV (23.6 V). Control de velocidad de 100 a 5000 qpps (máximo medido: 5050 qpps) en un ensayo de 10 min | 5 registros CSV en `08-software/control/ensayos/` |
| 2026-09-30 | Programas CNC (CAM) de las 5 piezas del brazo para el Haas VF-3, simulados con **0 colisiones** | `04-manufactura/cam-brazo/` (O01001–O01005) |
| Continuo | Herramientas de gestión: ERP en Python (OC, OF, recepción, estado), tablero de avance y sincronización con GitHub | `sistema/erp.py`, tablero web |

**Pendiente:**
- PID con los 4 motores y el segundo RoboClaw.
- Cinemática inversa mecanum en el MCU.
- Medir la frecuencia real del lazo (meta ≥ 200 Hz por rueda).
- Navegación (ROS 2/SLAM con el LiDAR), visión (calibración y pass/fail) y control del brazo. **Los tres sin avance.**

## 2. Administración del proyecto y materiales

### Órdenes de compra

| OC | Proveedor | Contenido | Monto MXN | Estado |
|---|---|---|---|---|
| OC-2026-001 | Slamtec MX | LiDAR | 5,350.00 | Cancelada: lo proporciona el Socio Formador |
| OC-2026-002 | NXP | MCU | 27,685.85 | Cancelada |
| OC-2026-003 | NXP | 5 × FRDM-S32K344 | 5,537.15 | ✅ Recibida |
| OC-2026-004 | Amazon | Insertos roscados | 271.00 | ✅ Recibida |
| OC-2026-005 | Metales MarChina | Soleras Al 6061 | 1,506.00 | Cancelada |
| OC-2026-006 | Marsa | Tubular de acero cal. 18 (chasis) | 366.00 | ✅ Recibida |
| OC-2026-007 | Amazon | Soportes de esquina | 240.00 | ✅ Recibida |
| OC-2026-008/009 | Metales MarChina | Soleras Al 6061 | 1,266.00 c/u | Canceladas |
| OC-2026-010 | Metales MarChina | Soleras Al 6061-T6 (brazo) | 1,266.00 | ✅ Recibida |

**Gasto ejercido (OC recibidas): $7,680.15 MXN.**

### Material entregado por el Socio Formador (sin OC)

- LiDAR 2D 360°.
- Riel lineal de 2.5 m.
- 4 motorreductores CHP 42GP-775 con encoder.
- 2 cámaras: frontal y RGB-D.
- Batería LiFePO4 de 24 V.
- 2 RoboClaw 2x45A.
- 5 MCU S32K312.

Esto **eliminó el riesgo de importación** que era la ruta crítica del plan original (R1, R2 y R3).

### Órdenes de fabricación

| OF | Parte | Responsable | Inicio → Fin | Estado |
|---|---|---|---|---|
| OF-2026-BRZ-001…005 | 5 piezas del brazo (Brazo_2, Brazo_3, Brazo4_1, Brazo1_1, Brazo1_2) en CNC Haas VF-3 | Osmar González | 2026-09-30 → 2026-10-07 | Fabricadas, inspección pendiente |
| OF-2026-AGV-002 | Chasis: bastidor soldado de tubular de acero cal. 18 | Rodrigo Herrera | 2026-10-05 → 2026-10-08 | Fabricado, inspección pendiente |
| OF-2026-AGV-001 | AGV Mecanum, prototipo 1 (ensamble general) | Equipo | 2026-08-25 → **2026-10-18** | Liberada, sin iniciar |
| *(por abrir)* | Ruedas mecanum impresas (PETG + TPU 95A) | Equipo | — | En validación de tolerancias |

### Cambios de alcance registrados

- **CC-001.** La integración con el CNC Haas (MTConnect, SMB, handshake por M-códigos) **sale del alcance del Reto**. El módulo I/O Ethernet ya no se necesita.
- **CC-002.** Driver de motores: RoboClaw 2x45A.
- **CC-003.** Ruedas mecanum de fabricación propia en lugar de compradas.

### Pendientes de compra

Sin proveedor todavía:
- **SBC para ROS 2 (clase Jetson).** Es la única compra crítica que queda: con 5 semanas de entrega, si se pide hoy llega ~2026-11-14, después de la Exposición Demostrativa.
- IMU.
- Sensor inductivo.
- Cargador.
- Convertidor DC-DC 24→5 V.
- Paro de emergencia.

## 3. Control de ensambles y trazabilidad

**Cadena de trazabilidad:** material → OC → OF → hoja viajera → subensamble → producto.

| Origen del material | Transformación | Responsable | Destino |
|---|---|---|---|
| OC-2026-010: Al 6061-T6 (Metales MarChina) | OF-BRZ-001…005, Haas VF-3, programas O01001–O01005 | Osmar González | Ensamble del brazo → MoMa |
| OC-2026-006: tubular de acero cal. 18 (Marsa) | OF-AGV-002, corte y soldadura | Rodrigo Herrera | OF-AGV-001 (AGV) |
| OC-2026-004/007: insertos y soportes (Amazon) | — | — | OF-AGV-001 (AGV) |
| Socio Formador: motores, RoboClaw, batería, LiDAR, cámaras, S32K312 | Recepción sin OC (préstamo) | — | OF-AGV-001 / celda |

- Cada OF cita su OC de origen y su programa CNC. Cada hoja viajera cita su OF.
- El registro completo vive en el ERP del proyecto (`registro-po.csv`, `registro-of.csv`, catálogo de 27 materiales) y en GitHub.

**Estado de los ensambles:** ningún subensamble se ha iniciado. Ni el brazo ni el chasis con motores.

**Brechas de trazabilidad:**
1. **Las piezas físicas no tienen identificación.** Hay que marcarlas con el número de OF (grabado o etiqueta) antes de ensamblar. Sin eso, la cadena se rompe en el piso.
2. Las ruedas mecanum no tienen OF todavía. Hay que abrir una OF con lote de impresión (48 rodillos + repuestos).
3. Los ensambles (OF-AGV-001 y el brazo) no tienen registro de torque ni de qué número de serie de motor y driver va en cada posición.

## 4. Calidad y seguimiento operativo

### Evaluación de las hojas viajeras

| Hoja viajera | Operador | Fechas | Cant. buena / scrap | Inspección | Firma de calidad | Dictamen |
|---|---|---|---|---|---|---|
| OF-BRZ-001…005 | ✅ Osmar | ✅ 09-30 → 10-07 | ❌ | ❌ op. 40 sin registro | ❌ | **Incompleta** |
| OF-AGV-002 | ✅ Rodrigo | ✅ 10-05 → 10-08 | ❌ | ❌ op. 50 sin registro | ❌ | **Incompleta** |
| OF-AGV-001 | — | — | — | — | — | Sin iniciar |

**Lectura:** las hojas sí registran **quién y cuándo**, pero no **cuánto salió bien ni quién lo liberó**. Las 6 se llenaron de forma posterior, no en la estación. Las 6 piezas fabricadas están **producidas pero no liberadas**.

### Controles de calidad realizados

| Control | Resultado |
|---|---|
| Simulación CAM de las 5 piezas del brazo | 0 colisiones antes de entrar al Haas |
| FEA de la rueda mecanum V6 (3 estudios) | Factor de seguridad (FS) del hub de 3.9 a carga de diseño (482 N). Punto débil identificado: unión entre capas del PETG (FS 1.2–1.4) |
| Holguras de impresión aplicadas al CAD | Ensamble reconstruye sin errores |
| **Banco de tolerancias PETG impreso** | Valida hexágono, cuello del hub, M5 y ejes de 1/4 in antes de imprimir las ruedas |
| Procedimiento de impresión de rodillos TPU | Orientación definida para no dañar la banda de rodadura |
| Prueba funcional NXP + RoboClaw con la batería del AGV | Telemetría y control de velocidad validados |

### Pendientes de calidad

- Inspección dimensional de las 5 piezas del brazo y del chasis (escuadra, diagonales, planitud).
- Registrar el resultado del banco de tolerancias.
- Cupón de TPU.
- Conteo de piezas buenas y scrap.
- Firma de liberación. Rodrigo es el responsable de calidad.

## 5. Alineación con los objetivos

| Objetivo específico (Carta Proyecto) | Avance | Estado |
|---|---|---|
| Diseñar y fabricar un AGV para transportar piezas | Chasis fabricado. Motores, drivers y batería recibidos. Un motor controlado en lazo cerrado. Ruedas en validación | 🟡 En curso |
| Navegación autónoma con LiDAR | LiDAR recibido. Sin SBC y sin software | 🔴 En riesgo |
| Integrar el brazo de 4 GDL sobre el AGV para la carga y descarga | 5 piezas maquinadas. Sin ensamble ni control | 🟡 En curso |
| Visión para verificar que la pieza esté bien colocada | Cámaras recibidas. Sin software | 🔴 No iniciado |
| Validar la celda completa (carga, descarga y validación) | Depende de lo anterior | ⚪ Pendiente |
| Comunicación con el CNC Haas | **Fuera de alcance (CC-001)** | — |

**Conclusión.** El proyecto resolvió su riesgo principal, las compras de lead largo, y avanza en fabricación según el plan de F3. La meta de costo del AGV (< $55,000 MXN) se mantiene: el gasto ejercido es de $7,680 MXN porque el hardware mayor fue proporcionado.

El nuevo cuello de botella **ya no son las compras, sino la integración y el software**. Cuatro acciones definen si se llega a la Exposición Demostrativa:

1. Comprar o conseguir la SBC esta semana.
2. Cerrar las inspecciones y firmas de las 6 OF fabricadas.
3. Iniciar el ensamble del AGV, porque la OF-AGV-001 vence el 2026-10-18.
4. Asignar responsables a navegación y visión.
