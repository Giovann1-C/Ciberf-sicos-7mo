# Plan de trabajo — Reto Celda Ciberfísica

**Proyecto:** Celda de alimentación robótica con coordinación CNC Haas vía MTConnect
**Subsistemas:** AGV mecanum · Brazo/cobot sobre riel lineal · Visión industrial
**Control:** PI / PD / PID sobre microcontrolador **NXP S32K312**
**Curso:** MR3005C.601 · **Peso:** 36 % de la calificación (4 evidencias individuales)
**Generado:** 2026-08-25

---

## 🔴 El hallazgo que define todo el proyecto

**Hoy es 25 de agosto y no ha salido ni una orden de compra.**

Cuatro componentes tienen lead time de 5–6 semanas:

| Componente | Lead | Si pides HOY llega | Si pides el 27/sep llega |
|---|---|---|---|
| Riel lineal 2.5 m | 6 sem | **6 oct** | 8 nov |
| LiDAR 2D 360° | 6 sem | **6 oct** | 8 nov |
| Batería LiFePO4 | 5 sem | **29 sep** | 1 nov |
| Módulo I/O Ethernet | 5 sem | **29 sep** | 1 nov |

Si las compras salen al final del diseño de detalle (finales de septiembre, que
es lo natural), **el material llega el 8 de noviembre y quedan 3 semanas para
integrar, validar y documentar.** Eso no alcanza.

**Decisión forzada:** las compras críticas se emiten **antes del 6 de
septiembre**, con el diseño congelado solo en lo que define la compra (interfaces
mecánicas y eléctricas), no con el CAD terminado. Es exactamente el riesgo que
el profe pidió documentar en la Actividad 2 ("si los LiDAR de Asia se retrasan
4 semanas").

---

## Fases

### F0 · Arranque — S1-2 · 10–23 ago ✅ cerrado
Entregado: INTRO, Trazabilidad del proyecto, Evidencia Fotográfica Material 1.

### F1 · Definición y anteproyecto — S3-4 · **24 ago – 6 sep** ← estamos aquí
| # | Tarea | Responsable | Estado |
|---|---|---|---|
| 1.1 | Congelar alcance y criterios de aceptación | | pendiente |
| 1.2 | WBS completo y matriz RACI del equipo | | pendiente |
| 1.3 | **BOM preliminar cerrado** (bloquea compras) | | en curso |
| 1.4 | Cotizar los 4 componentes de lead largo | | **URGENTE** |
| 1.5 | Fichas de proveeduría de los críticos | | pendiente |
| 1.6 | **Emitir PO de riel, LiDAR, batería, I/O** | | **antes del 6 sep** |
| 1.7 | **Evidencia 1 — Anteproyecto (6 %)** | Rodrigo | pendiente |
| 1.8 | Actividad 3 de M3 (vence 31 ago) | Rodrigo | pendiente |

### F2 · Diseño de detalle — S5-7 · 7–27 sep
CAD completo del chasis mecanum y del riel · Diseño eléctrico 24 V y arnés ·
Arquitectura de software (capas MCU / SBC / supervisor) · Diseño del pallet y
fixture indexado · Resto de las PO · **Simulación en FlexSim** (la pide el profe
tras aprobar la Actividad 2).

### F3 · Fabricación y subensambles — S8-11 · 28 sep – 25 oct
Corte y ensamble de chasis (torque 45 Nm) · Montaje de 4 motores mecanum ·
Ruteo de arnés y paros de emergencia · **Firmware NXP: lazos PI, PD y PID con
sintonía documentada** · Fabricación del riel lineal · OF y hoja viajera
firmadas por estación.

### F4 · Navegación e integración — S12-13 · 26 oct – 8 nov
ROS 2 Humble + slam_toolbox + Nav2 · Docking por AprilTag con repetibilidad
≤ ±10 mm · Publicación MQTT del estado del AGV · Teach de trayectorias del cobot ·
**Evidencia 2 — Exposición Demostrativa (10 %, evalúa el Socio Formador)**.

### F5 · Celda completa — S14-15 · 9–22 nov
Cliente MTConnect contra el Haas (puerto 8082, polling 250 ms) · Transferencia
de programas por SMB con hash · Handshake discreto por M-códigos · Visión RGB-D
pass/fail con calibración ChArUco · Máquina de estados del supervisor ·
**Evidencia 3 — Exposición Argumentativa (10 %)**.

### F6 · Cierre — S16 · 23 nov – 6 dic
QA eléctrico y dinámico (freno < 0.5 s ante obstáculo a 2 m) · Manuales de
ingeniería de aplicaciones · Trazabilidad completa ·
**Evidencia 4 — Reporte Integrador (10 %)**.

---

## Ruta crítica

```
BOM cerrado → cotización → PO emitida → tránsito (6 sem) → recepción
   → subensamble → firmware PI/PD/PID → SLAM/Nav2 → docking
   → coordinación con Haas → validación → Evidencia 4
```

**La ruta crítica NO pasa por la programación: pasa por las compras.** Todo lo
de software se puede adelantar con simulación (CoppeliaSim, Gazebo) mientras el
material está en tránsito. Lo que no se puede adelantar es el hardware que no
llegó.

## Riesgos (PMBOK)

| # | Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|---|
| R1 | LiDAR se retrasa 4+ semanas | Alta | **Crítico** | Comprar antes del 6 sep · Plan B: LiDAR local aunque cueste más · Desarrollar Nav2 en Gazebo mientras llega |
| R2 | Riel lineal 2.5 m no llega o no cumple | Media | Crítico | Cotizar 2 proveedores · Plan B: reducir carrera del riel y reubicar la estación de handoff |
| R3 | Batería LiFePO4 detenida en aduana | Media | Alto | Comprar en distribuidor nacional · Plan B: banco de LiPo con BMS propio |
| R4 | No hay acceso al CNC Haas cuando toca F5 | Media | Alto | Agendar la ventana de máquina **desde ahora** con el laboratorio |
| R5 | El NXP no basta para el lazo de 4 motores mecanum | Media | Medio | Validar frecuencia de lazo en F3 temprano · Plan B: segundo MCU dedicado |
| R6 | El equipo no cierra el BOM a tiempo | Alta | **Crítico** | Fecha límite dura: **1 de septiembre** |

---

## ⚠️ Divergencias entre la propuesta y lo que dijo Rodrigo

Hay que resolverlas con el equipo y los profes **esta semana**:

1. **Microcontrolador.** La propuesta dice **STM32** para el lazo de bajo nivel
   y **Jetson Orin Nano** para ROS 2. Rodrigo dice que usarán **NXP**. El
   S32K312 sí puede sustituir al STM32 (y ya lo ven en M4), pero **no puede
   correr ROS 2, SLAM ni Nav2**. Se necesita igual una SBC con Linux. Ya la
   agregué al BOM porque faltaba.
2. **Ruedas.** La propuesta no especifica mecanum; Rodrigo sí. Mecanum es
   compatible con Nav2, pero exige **4 motores con encoder controlados
   independientemente** y cinemática omnidireccional — no diferencial. Cambia
   el modelo cinemático y el driver.
3. **Brazo robótico.** La propuesta asume un **cobot comercial** (UR3e, Doosan,
   Techman) sobre riel. Rodrigo habla de un **brazo robótico propio** que además
   funcione como cobot. Fabricar el brazo es un proyecto completo por sí solo.
   **Esta es la decisión de alcance más cara del semestre: hay que cerrarla ya.**
