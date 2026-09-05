# Carta Proyecto

## Celda Ciberfísica de Alimentación Robótica para Centro de Maquinado CNC Haas

**Documento:** Acta de Constitución del Proyecto (Project Charter) · PMBOK 7ª edición
**Versión:** 1.0 · **Fecha de emisión:** 2026-09-04
**Curso:** MR3005C.601 — Sistemas Ciber-Físicos · Módulo 3, Administración de Proyectos
**Institución:** Tecnológico de Monterrey, Campus Guadalajara

> ⬜ **Campos por confirmar con el Socio Formador.** Los recuadros marcados así
> requieren el dato directo del socio y no deben inventarse. Ver
> `preguntas-socio-formador.md` para el guion de la reunión.

---

# 1. Participantes del Proyecto

## 1.1 Patrocinador / Socio Formador

| Campo | Dato |
|---|---|
| Organización | ⬜ _por confirmar_ |
| Representante | ⬜ _por confirmar_ |
| Cargo | ⬜ _por confirmar_ |
| Correo / teléfono | ⬜ _por confirmar_ |
| Rol en el proyecto | Define los requisitos industriales, facilita el acceso al CNC Haas y al área de la celda, y **evalúa la Evidencia 2 — Exposición Demostrativa** |

## 1.2 Cliente

El área de manufactura del Socio Formador, como usuario final de la celda
automatizada de alimentación del centro de maquinado.

## 1.3 Interesados

| Interesado | Interés | Influencia | Estrategia de gestión |
|---|---|---|---|
| Socio Formador | Solución transferible a un entorno industrial real | Alta | Gestionar de cerca; preparar entregables con criterio industrial, no escolar |
| Equipo docente (Oscar Carbajal, Abdiel) | Aprendizaje demostrable y trazabilidad | Alta | Reporte por evidencia; consulta ante cualquier cambio de alcance |
| Profesor de Administración de Proyectos (Dani) | Aplicación correcta del estándar PMBOK | Media | El Reto se usa como caso de estudio en cada entrega del módulo |
| Laboratorio de manufactura | Uso seguro del CNC y del espacio físico | Alta | Reserva anticipada de ventanas de máquina; cumplimiento de protocolos |
| Equipo del proyecto | Carga equilibrada, aprendizaje, acreditación | Alta | Matriz RACI explícita y tablero público en Notion |

## 1.4 Proveedores y contratistas

| Proveedor | Suministro | Estado |
|---|---|---|
| NXP | Microcontroladores S32K312 y kits FRDM-S32K344 | OC-2026-003 emitida |
| Slamtec (distribuidor MX) | LiDAR 2D 360° | Cancelada — el equipo docente lo aporta |
| ⬜ _por definir_ | Batería LiFePO4 24 V 20 Ah | Por cotizar · **lead 5 semanas** |
| ⬜ _por definir_ | Cómputo supervisor clase Jetson Orin Nano | Por cotizar · **lead 5 semanas** |
| Fabricación interna | Fixture indexado y pallet de 5 posiciones | Por diseñar |

---

# 2. Equipo del Proyecto y Director

| Rol | Nombre | Responsabilidad principal |
|---|---|---|
| **Director de proyecto** | Rodrigo Herrera Baños (A01738608) | Planeación, control de alcance, emisión de PO, integración y comunicación con interesados |
| Integrante | Osmar | ⬜ _paquete de trabajo por confirmar_ |
| Integrante | Samuel | ⬜ _paquete de trabajo por confirmar_ |
| Integrante | Giovanni | ⬜ _paquete de trabajo por confirmar_ |
| Integrante | Perla | ⬜ _paquete de trabajo por confirmar_ |

**Dedicación comprometida:** mínimo 12 h/semana por integrante.
**Matriz RACI completa:** `pmi-plan-direccion-proyecto.md`, sección 7.

---

# 3. Descripción del Proyecto

## 3.1 Declaración de la meta

Diseñar, construir y validar una **celda ciberfísica capaz de alimentar de forma
autónoma un centro de maquinado CNC Haas**, integrando un vehículo autoguiado de
ruedas mecanum, un brazo manipulador sobre riel lineal y un sistema de visión
industrial, coordinados mediante comunicación bidireccional con el control de la
máquina — todo ello demostrado en operación continua antes del 6 de diciembre de 2026.

## 3.2 Descripción y antecedentes

La alimentación manual de un centro de maquinado obliga a un operador a
permanecer disponible durante todo el ciclo, aunque el trabajo efectivo de carga
y descarga represente una fracción menor del tiempo. Esto limita la utilización
de la máquina, introduce variabilidad en el posicionamiento de la pieza y expone
al operador a un entorno con viruta, refrigerante y elementos móviles.

El proyecto automatiza ese ciclo mediante tres subsistemas coordinados:

- **AGV de tracción omnidireccional** que transporta pallets indexados entre el
  almacén de materia prima y la estación de transferencia.
- **Manipulador sobre riel lineal de 2.5 m** que ejecuta la carga y descarga en
  el husillo, actuando el riel como séptimo eje externo.
- **Visión industrial** que verifica el asentamiento de la pieza en el fixture y
  emite un dictamen de aceptación o rechazo antes de autorizar el arranque.

La coordinación con el CNC se realiza por tres canales complementarios:
**MTConnect** para leer el estado de la máquina, **SMB** para la transferencia de
programas, y una **interfaz discreta de códigos M** para el enlace determinista
de arranque y paro.

## 3.3 Objetivos

| # | Objetivo | Criterio de éxito medible |
|---|---|---|
| O1 | Navegación autónoma del AGV | SLAM operativo y llegada a la estación de transferencia sin intervención |
| O2 | Repetibilidad del acoplamiento | Docking por AprilTag con repetibilidad **≤ ±10 mm** |
| O3 | Control de lazo cerrado | Lazos **PI, PD y PID** implementados en el NXP S32K312 con sintonía documentada |
| O4 | Integración con el CNC | Lectura de estado por MTConnect y handshake discreto por códigos M funcionando |
| O5 | Inspección automática | Dictamen de aceptación/rechazo por visión con calibración ChArUco documentada |
| O6 | Seguridad operativa | Frenado ante obstáculo a 2 m en **menos de 0.5 s** |
| O7 | Trazabilidad documental | Expediente completo: BOM, órdenes de compra, órdenes de fabricación y hojas viajeras firmadas |

## 3.4 Alcance

**Dentro del alcance**

- Diseño mecánico, eléctrico y de control del AGV de ruedas mecanum
- Firmware de control sobre NXP S32K312 con lazos PI, PD y PID
- Cómputo supervisor con ROS 2 Humble, SLAM y navegación autónoma
- Integración del manipulador sobre riel lineal
- Sistema de visión para verificación de asentamiento de pieza
- Cliente MTConnect, transferencia de programas por SMB y handshake por códigos M
- Fixture indexado y pallet de cinco posiciones (fabricación interna)
- Documentación de ingeniería, expediente de compras y manual de operación

**Fuera del alcance**

- Modificación del programa de maquinado o de los parámetros de corte del Haas
- Certificación formal de seguridad ante organismo externo
- Producción en volumen: el entregable es un prototipo funcional demostrable
- Mantenimiento del sistema después del 6 de diciembre de 2026
- ⬜ _Fabricación de brazo propio vs. integración de cobot comercial: **decisión de alcance pendiente**, ver sección 7_

## 3.5 Entregables

| # | Entregable | Fecha comprometida |
|---|---|---|
| E1 | Anteproyecto (Evidencia 1) | 2026-09-06 |
| E2 | Diseño congelado y simulación en FlexSim | 2026-09-27 |
| E3 | AGV operativo con control PI/PD/PID | 2026-10-25 |
| E4 | Exposición Demostrativa (Evidencia 2) — *evalúa el Socio Formador* | 2026-11-08 |
| E5 | Exposición Argumentativa (Evidencia 3) | 2026-11-22 |
| E6 | Reporte Integrador (Evidencia 4) | 2026-12-06 |

---

# 4. Calendario

| Concepto | Valor |
|---|---|
| Fecha de inicio | 2026-08-10 |
| Fecha de cierre | 2026-12-06 |
| Duración | 16 semanas |
| Reporte de avance | Semanal al equipo docente; tablero Kanban actualizado de forma continua |
| Revisión con el Socio Formador | ⬜ _frecuencia por acordar_ |

## Fases

| Fase | Semanas | Periodo | Hito de cierre |
|---|---|---|---|
| F0 · Arranque | 1–2 | 10–23 ago | ✅ Cerrada |
| F1 · Definición y anteproyecto | 3–4 | 24 ago – 6 sep | H1: Órdenes de compra críticas emitidas |
| F2 · Diseño de detalle | 5–7 | 7–27 sep | H2: Diseño congelado y simulación validada |
| F3 · Fabricación y subensambles | 8–11 | 28 sep – 25 oct | H3: AGV rodando con control cerrado |
| F4 · Navegación e integración | 12–13 | 26 oct – 8 nov | H4: Navegación y acoplamiento validados |
| F5 · Celda completa | 14–15 | 9–22 nov | H5: Ciclo completo coordinado con el Haas |
| F6 · Cierre | 16 | 23 nov – 6 dic | H6: Reporte integrador entregado |

---

# 5. Estimación de Costos

Valores en pesos mexicanos, tomados del catálogo de materiales del sistema ERP
del proyecto (`02-proveeduria/catalogo-materiales.csv`).

| Concepto | Monto (MXN) |
|---|---|
| Material aportado por el equipo docente (préstamo o donación) | $67,650.00 |
| Material por adquirir | $46,487.15 |
| **Valor total del proyecto** | **$114,137.15** |

## Desglose del material por adquirir

| Concepto | Cant. | Monto | Lead time |
|---|---|---|---|
| Cómputo supervisor clase Jetson Orin Nano | 1 | $12,000.00 | **5 semanas** |
| Batería LiFePO4 24 V 20 Ah con BMS | 1 | $9,500.00 | **5 semanas** |
| Ruedas mecanum 100 mm | 4 | $7,200.00 | 3 semanas |
| Kits de desarrollo FRDM-S32K344 | 5 | $5,537.15 | 1 semana |
| Perfil estructural de aluminio 40×40 | 8 m | $3,360.00 | 2 semanas |
| Sensores inductivos M12 | 4 | $2,600.00 | 2 semanas |
| Cargador de batería 24 V | 1 | $2,100.00 | 3 semanas |
| Botones de paro de emergencia | 2 | $1,780.00 | 2 semanas |
| Convertidores DC-DC 24 V → 5 V | 2 | $1,560.00 | 2 semanas |
| Unidad inercial de 9 GDL | 1 | $850.00 | 3 semanas |

**Aportación del Socio Formador:** ⬜ _por confirmar qué partidas cubre y cuál es
el techo presupuestal._

> **Nota de gestión.** Los dos artículos de mayor lead time —cómputo supervisor y
> batería— determinan la ruta crítica del proyecto. Deben cotizarse y emitirse
> **antes del 29 de septiembre de 2026** para llegar a la fase de integración.

---

# 6. Hitos del Proyecto

| Hito | Descripción | Fecha |
|---|---|---|
| H1 | Órdenes de compra de partidas críticas emitidas | 2026-09-06 |
| H2 | Diseño de detalle congelado y simulación validada | 2026-09-27 |
| H3 | AGV rodando con lazos de control sintonizados | 2026-10-25 |
| H4 | Navegación autónoma y acoplamiento con repetibilidad ≤ ±10 mm | 2026-11-08 |
| H5 | Ciclo completo de alimentación coordinado con el CNC Haas | 2026-11-22 |
| H6 | Reporte integrador y entrega de expediente documental | 2026-12-06 |

---

# 7. Supuestos, Restricciones, Dependencias e Impactos

## 7.1 Supuestos

1. El equipo docente entrega el riel lineal, el LiDAR, el módulo de E/S Ethernet, el balero de rodillos cruzados y el motorreductor en tiempo para la fase de fabricación.
2. Cada integrante dedica al menos 12 h/semana al proyecto.
3. El CNC Haas cuenta con la opción de red habilitada y el agente MTConnect operativo.
4. El área de la celda dispone de piso plano y continuo, apto para tracción omnidireccional.
5. Los precios del catálogo se mantienen dentro de un margen del 15 % al momento de cotizar.

## 7.2 Restricciones

| Tipo | Restricción |
|---|---|
| Tiempo | 16 semanas improrrogables; el calendario académico no admite extensión |
| Presupuesto | Limitado a lo aportado por el equipo docente más lo autorizado por el Socio Formador |
| Técnica | El NXP S32K312 **no puede ejecutar ROS 2**; se requiere una SBC con Linux como cómputo supervisor |
| Acceso | La disponibilidad del CNC Haas depende de la programación del laboratorio y no es controlada por el equipo |
| Normativa | La operación con personas en proximidad debe cumplir la normativa de seguridad aplicable ⬜ _por confirmar cuál_ |

## 7.3 Dependencias

- La fabricación del chasis depende de la recepción del perfil de aluminio y de las ruedas mecanum.
- La navegación autónoma depende de la recepción del cómputo supervisor y del LiDAR.
- La integración de la celda depende del acceso al CNC Haas y de la disponibilidad de la interfaz de códigos M.
- El diseño del fixture y del gripper depende de conocer la **pieza real** a maquinar. ⬜ _por confirmar_

## 7.4 Riesgos principales

| # | Riesgo | Prob. | Impacto | Respuesta |
|---|---|---|---|---|
| R1 | La batería LiFePO4 se detiene en aduana | Media | Alto | Comprar a distribuidor nacional; alternativa: banco de LiPo con BMS propio |
| R2 | El cómputo supervisor no llega a tiempo | Media | Crítico | Emitir la orden antes del 29-sep; desarrollar navegación en simulación mientras llega |
| R3 | **Sin acceso al CNC Haas en noviembre** | Media | Alto | Reservar la ventana de máquina de inmediato; contingencia: agente MTConnect simulado |
| R4 | **El CNC no cuenta con tarjeta de interfaz de códigos M** | ⬜ por confirmar | Crítico | Sin ella no existe el enlace discreto; la coordinación se degrada a sondeo por MTConnect |
| R5 | Fabricar un brazo propio consume el semestre completo | Alta | Crítico | **Evitar:** decidir cobot comercial vs. propio con el Socio Formador de inmediato |
| R6 | El S32K312 no sostiene el lazo de los cuatro motores | Media | Medio | Validar la frecuencia de lazo en fase temprana; contingencia: segundo MCU dedicado |
| R7 | Carga desigual entre integrantes | Media | Medio | Matriz RACI explícita y revisión semanal en el tablero |

---

# 8. Autorización

Los abajo firmantes coinciden en que este es un proyecto viable y autorizan el
inicio de la etapa de planeación detallada.

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Director de proyecto | Rodrigo Herrera Baños | | |
| Socio Formador | ⬜ _por confirmar_ | | |
| Profesor titular del Reto | Oscar Carbajal | | |
| Profesor de Administración de Proyectos | Dani | | |

---

## Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-09-04 | Emisión inicial para la Actividad 5 del Módulo 3 |

**Documentos relacionados**
`pmi-plan-direccion-proyecto.md` · `plan-de-trabajo.md` · `preguntas-socio-formador.md` · `02-proveeduria/catalogo-materiales.csv`
