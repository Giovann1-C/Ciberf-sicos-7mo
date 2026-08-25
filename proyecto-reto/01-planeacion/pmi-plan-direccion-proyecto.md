# Plan para la Dirección del Proyecto (PMI / PMBOK)

**Proyecto:** Celda ciberfísica de alimentación robotizada para CNC Haas
**Código:** RETO-MR3005C-601-2026
**Curso:** Sistemas ciber-físicos · MR3005C.601 · Tec de Monterrey Guadalajara
**Director de proyecto:** Rodrigo Herrera Baños (A01738608)
**Periodo:** 10 ago 2026 – 6 dic 2026 (16 semanas)
**Versión:** 1.0 · 2026-08-25

---

# 1. Acta de Constitución (Project Charter)

## 1.1 Justificación del negocio
En talleres de manufactura pequeños y medianos, alimentar una máquina CNC es una
tarea manual que consume **15–30 min por cambio de pieza** y es uno de los
mayores componentes del tiempo improductivo del husillo. Los AGV comerciales que
resuelven esto (MiR 100/250, Bosch Rexroth ActiveShuttle, Otto Motors) cuestan
**25,000–120,000 USD por unidad**, prohibitivo para el segmento de manufactura
por contrato mexicana.

**La pregunta correcta no es cuánto cuesta el AMR, sino cuánto cuesta no
tenerlo.** Los cinco dolores de planta que justifican la inversión:

| Dolor | Costo de no resolverlo |
|---|---|
| Rigidez | Cambiar de modelo obliga a modificar la planta |
| Mano de obra | Escasez estructural de operadores de montacargas |
| Seguridad | Accidentes con montacargas y personal |
| Trazabilidad | El movimiento manual de material es un hueco de datos |
| Desperdicio | Husillo parado, retrabajo, scrap |

## 1.2 Objetivo del proyecto
Diseñar, fabricar, integrar y validar una **celda ciberfísica prototipo** que
automatice el ciclo de carga y descarga de un CNC Haas, compuesta por un AGV
omnidireccional de fabricación propia, un brazo robótico colaborativo sobre riel
lineal, y un sistema de visión industrial de verificación, coordinados sobre
Ethernet mediante MTConnect, SMB y handshake discreto por M-códigos.

**Meta de costo de materiales del AGV:** < 55,000 MXN.

## 1.3 Criterios de éxito medibles

| # | Criterio | Métrica | Umbral |
|---|---|---|---|
| C1 | El AGV navega autónomamente | Misión punto a punto completada | ≥ 9 de 10 intentos |
| C2 | Docking repetible | Error de posición en handoff | ≤ ±10 mm |
| C3 | Control de motores estable | Sobreimpulso en escalón de velocidad | ≤ 10 % |
| C4 | Parada segura | Tiempo de freno ante obstáculo a 2 m | < 0.5 s |
| C5 | El brazo transfiere la pieza | Ciclo completo pallet → fixture | ≥ 9 de 10 |
| C6 | Visión detecta mal asentamiento | Tasa de detección de pieza mal puesta | ≥ 95 % |
| C7 | Coordinación con el CNC | Handshake completo sin intervención | ≥ 5 ciclos seguidos |
| C8 | Trazabilidad documental | PO, OF y hojas viajeras completas | 100 % |

## 1.4 Supuestos
- El laboratorio otorga acceso al CNC Haas durante noviembre.
- El control Haas es **NGC** y tiene el agente MTConnect habilitado (puerto 8082).
- Existe presupuesto o financiamiento aprobado para ~84,000 MXN de materiales.
- El equipo dispone de al menos 12 h/semana por integrante.
- La pieza de trabajo es un **billet rectangular de aluminio de geometría fija**.

## 1.5 Restricciones
- **Calendario inamovible:** 16 semanas, sin posibilidad de extensión.
- **Lead times de importación:** hasta 6 semanas en componentes críticos.
- Acceso al CNC limitado a las ventanas que asigne el laboratorio.
- La celda debe operar sin modificar permanentemente la máquina Haas.

## 1.6 Exclusiones explícitas (lo que NO se hace)
- No se implementa visión-guiada para la prehensión: las trayectorias del brazo
  son **enseñadas** sobre geometría conocida.
- La visión **no** escribe variables macro ni corrige el origen del CNC: opera
  estrictamente en modo verificación pass/fail.
- No se desarrolla un fleet manager multi-robot: una sola unidad.
- No se certifica el sistema bajo norma de seguridad; se documenta el diseño de
  seguridad, no se certifica.

---

# 2. Gestión del Alcance

## 2.1 EDT / WBS

```
1. CELDA CIBERFÍSICA (RETO-MR3005C)
│
├── 1.1 GESTIÓN DEL PROYECTO
│   ├── 1.1.1 Acta de constitución y plan de dirección
│   ├── 1.1.2 Cronograma y control de avance
│   ├── 1.1.3 Gestión de adquisiciones (PO, importación)
│   ├── 1.1.4 Gestión de riesgos y plan de contingencia
│   ├── 1.1.5 Trazabilidad documental (OF, hojas viajeras)
│   └── 1.1.6 Evidencias del curso (4 individuales)
│
├── 1.2 AGV OMNIDIRECCIONAL
│   ├── 1.2.1 Estructura
│   │   ├── 1.2.1.1 Chasis de perfil de aluminio 40x40
│   │   ├── 1.2.1.2 Montajes de motor y suspensión
│   │   └── 1.2.1.3 Plataforma de carga del pallet
│   ├── 1.2.2 Tracción
│   │   ├── 1.2.2.1 4 ruedas mecanum + 4 motorreductores
│   │   ├── 1.2.2.2 Modelo cinemático omnidireccional
│   │   └── 1.2.2.3 Driver de 4 canales
│   ├── 1.2.3 Potencia
│   │   ├── 1.2.3.1 Batería LiFePO4 24 V + BMS
│   │   ├── 1.2.3.2 Distribución 24 V / 5 V
│   │   └── 1.2.3.3 Circuito de paro de emergencia
│   ├── 1.2.4 Control de bajo nivel (NXP S32K312)
│   │   ├── 1.2.4.1 Lectura de encoders en cuadratura
│   │   ├── 1.2.4.2 Lazos PI / PD / PID por rueda
│   │   ├── 1.2.4.3 Watchdog y modo seguro
│   │   └── 1.2.4.4 Interfaz con el cómputo supervisor
│   ├── 1.2.5 Percepción
│   │   ├── 1.2.5.1 LiDAR 2D 360°
│   │   ├── 1.2.5.2 IMU 9 DOF
│   │   └── 1.2.5.3 Cámara frontal (AprilTag)
│   ├── 1.2.6 Navegación (ROS 2 sobre SBC)
│   │   ├── 1.2.6.1 SLAM (slam_toolbox)
│   │   ├── 1.2.6.2 Localización (AMCL)
│   │   ├── 1.2.6.3 Planeación (Nav2)
│   │   └── 1.2.6.4 Acción de docking por AprilTag
│   └── 1.2.7 Conectividad MQTT/TLS con el supervisor
│
├── 1.3 BRAZO ROBÓTICO / COBOT
│   ├── 1.3.1 Definición de plataforma (⚠ decisión pendiente)
│   ├── 1.3.2 Riel lineal 2.5 m (séptimo eje)
│   ├── 1.3.3 Efector final (gripper)
│   ├── 1.3.4 Programación de trayectorias enseñadas
│   └── 1.3.5 Seguridad colaborativa (ISO/TS 15066)
│
├── 1.4 SISTEMA DE VISIÓN
│   ├── 1.4.1 Montaje de cámara RGB-D sobre la mesa
│   ├── 1.4.2 Calibración cámara–fixture (ChArUco)
│   ├── 1.4.3 Algoritmo de verificación (4 criterios)
│   └── 1.4.4 Publicación del veredicto por MQTT
│
├── 1.5 INTEGRACIÓN DE CELDA
│   ├── 1.5.1 Supervisor y máquina de estados
│   ├── 1.5.2 Cliente MTConnect (Haas :8082)
│   ├── 1.5.3 Transferencia de programas por SMB
│   ├── 1.5.4 Handshake discreto por M-códigos e I/O
│   ├── 1.5.5 Fixture indexado y pallet de 5 posiciones
│   └── 1.5.6 Dashboard de OEE y trazabilidad
│
└── 1.6 VALIDACIÓN Y DOCUMENTACIÓN
    ├── 1.6.1 QA eléctrico (continuidad, aislamiento)
    ├── 1.6.2 QA mecánico (torque 45 Nm)
    ├── 1.6.3 QA dinámico (freno < 0.5 s)
    ├── 1.6.4 Pruebas de ciclo completo
    ├── 1.6.5 Manuales de ingeniería de aplicaciones
    └── 1.6.6 Simulación en FlexSim
```

## 2.2 Diccionario de la EDT (paquetes críticos)

| ID | Paquete | Entregable verificable | Criterio de aceptación |
|---|---|---|---|
| 1.2.2 | Tracción mecanum | AGV que se desplaza en X, Y y gira | Movimiento omnidireccional sin deriva > 5 % |
| 1.2.4 | Control NXP | Firmware con 4 lazos cerrados | Sobreimpulso ≤ 10 %, error permanente ≈ 0 |
| 1.2.6 | Navegación | Mapa del laboratorio + misiones Nav2 | 9/10 misiones completadas |
| 1.3.2 | Riel lineal | Carrera de 2.5 m con repetibilidad | ±1 mm en posiciones enseñadas |
| 1.5.2 | Cliente MTConnect | Estado del Haas en el bus MQTT | Latencia ≤ 250 ms, sin pérdida de eventos |
| 1.5.4 | Handshake | Ciclo carga–maquinado–descarga | 5 ciclos seguidos sin intervención |

## 2.3 Control de cambios
Todo cambio de alcance se registra en la base **Tareas del Equipo** de Notion
con el prefijo `CC-`. Aprueba el director de proyecto tras evaluar impacto en
cronograma, costo y riesgo. **Ningún cambio se implementa sin registro.**

---

# 3. Gestión del Cronograma

## 3.1 Fases y fechas

| Fase | Semanas | Fechas | Hito |
|---|---|---|---|
| F0 Arranque | 1–2 | 10–23 ago | ✅ Cerrada |
| **F1 Definición y compras críticas** | 3–4 | **24 ago – 6 sep** | H1: PO críticas emitidas |
| F2 Diseño de detalle | 5–7 | 7–27 sep | H2: Diseño congelado + FlexSim |
| F3 Fabricación | 8–11 | 28 sep – 25 oct | H3: AGV rodando con control |
| F4 Navegación | 12–13 | 26 oct – 8 nov | H4: Navegación + docking OK |
| F5 Celda completa | 14–15 | 9–22 nov | H5: Ciclo completo con el Haas |
| F6 Cierre | 16 | 23 nov – 6 dic | H6: Reporte integrador |

## 3.2 Ruta crítica

```
Cerrar BOM (1 sep)
  → Cotizar (2 sep)
    → EMITIR PO (6 sep)
      → Tránsito 6 semanas
        → Recepción (18 oct)
          → Subensamble (25 oct)
            → Firmware PI/PD/PID (1 nov)
              → SLAM + Nav2 (8 nov)
                → Docking (15 nov)
                  → Coordinación Haas (22 nov)
                    → Validación y reporte (6 dic)
```

**Holgura total: 0 días.** Cualquier retraso en las compras se traslada íntegro
al final. Por eso la fecha de emisión de PO es un hito duro, no una meta suave.

## 3.3 Trabajo paralelizable (no está en la ruta crítica)
Mientras el material viaja, avanza sin bloqueo:
- CAD completo y planos de fabricación
- Nav2 y SLAM en **Gazebo o CoppeliaSim** con modelo del AGV
- Cliente MTConnect probado contra un **agente simulado**
- Algoritmo de visión con fotos del fixture
- Simulación FlexSim de estaciones y tiempos
- Documentación y borradores de evidencias

> Regla: si una semana el equipo no puede tocar hardware, **debe** estar
> avanzando en esta lista. No hay excusa de "estamos esperando material".

---

# 4. Gestión de los Costos

## 4.1 Presupuesto por subsistema

| Subsistema | Materiales | Monto (MXN) |
|---|---|---|
| AGV | 15 | ~39,340 |
| Cobot / riel | 1 | ~28,000 |
| Celda / integración | 2 | ~6,500 |
| Visión | 1 | ~7,800 |
| Brazo (balero) | 1 | ~2,400 |
| **Subtotal materiales** | **20** | **~84,040** |
| Reserva de contingencia (15 %) | | ~12,600 |
| **Total con reserva** | | **~96,640** |

## 4.2 Alerta de presupuesto
La meta de la propuesta era **< 55,000 MXN** para el AGV. El AGV solo va en
~39,340, dentro de meta. **El desbordamiento viene del riel lineal (28,000) y la
visión (7,800)**, que no son parte del AGV. Si hay que recortar, el riel es el
candidato: reducir la carrera de 2.5 m a 1.5 m y reubicar la estación de handoff.

## 4.3 Control de costos
Toda erogación pasa por una **PO registrada** en `03-compras/registro-po.csv`.
Sin PO no hay compra. El comando `python sistema/erp.py estado` da el
consolidado en cualquier momento.

---

# 5. Gestión de la Calidad

## 5.1 Plan de aseguramiento

| Estación | Verificación | Criterio | Registro |
|---|---|---|---|
| 10 Kitting | Surtido de BOM completo e inspección visual | 100 % de piezas | Hoja viajera |
| 20 Mecánico | Torque con llave dinamométrica | **45 Nm ±5 %** | Hoja viajera |
| 30 Electrónico | Ruteo de arnés y paros de emergencia | Continuidad OK | Hoja viajera |
| 40 Control | Firmware cargado, encoders calibrados | Sobreimpulso ≤ 10 % | Bitácora de sintonía |
| 50 QA eléctrico | Continuidad y aislamiento 24 V | Sin fugas | Protocolo QA |
| 60 QA dinámico | Freno ante obstáculo a 2 m | **< 0.5 s** | Video + log |
| 70 Liberación | Firma de calidad | Todas las anteriores OK | Hoja viajera |

## 5.2 Métricas de calidad del producto
- Repetibilidad de docking: **≤ ±10 mm** (medida sobre 20 aproximaciones)
- Error permanente de velocidad de rueda: **≤ 2 %**
- Tasa de falsos negativos de visión: **≤ 5 %**
- Disponibilidad de la celda en pruebas: **≥ 80 %**

## 5.3 Auditoría documental
Antes de cada evidencia, verificar que existan: PO de todo lo comprado, OF
liberada, hoja viajera firmada por estación, y bitácora de sintonía de control.
**El profe evalúa la trazabilidad, no solo que el AGV camine.**

---

# 6. Gestión de los Recursos

## 6.1 Matriz RACI

> Llenar con los nombres reales del equipo. R = responsable ejecuta ·
> A = aprueba · C = consultado · I = informado.

| Paquete | Rodrigo | Integrante 2 | Integrante 3 | Integrante 4 | Docentes |
|---|---|---|---|---|---|
| 1.1 Gestión del proyecto | **A/R** | C | C | C | I |
| 1.2 AGV — estructura y tracción | C | **R** | C | | I |
| 1.2.4 Control NXP (PI/PD/PID) | **R** | C | | | I |
| 1.2.6 Navegación ROS 2 | C | | **R** | C | I |
| 1.3 Brazo / cobot y riel | C | C | | **R** | I |
| 1.4 Visión | | | **R** | C | I |
| 1.5 Integración de celda | **R** | C | C | C | C |
| 1.6 Validación y documentación | **A** | R | R | R | **A** |
| Evidencias individuales | **R** | R | R | R | **A** |

## 6.2 Recursos físicos requeridos
- Laboratorio de manufactura con **CNC Haas NGC** (ventana a reservar)
- Impresora 3D y taller mecánico (corte de perfil, barrenado)
- Estaciones de trabajo con SolidWorks, MATLAB/Simulink, FlexSim
- Máquina con **Ubuntu 22.04** para ROS 2 Humble
- Red del laboratorio con acceso al puerto 8082 del Haas

## 6.3 Competencias a desarrollar
ROS 2 y Nav2 · Programación de MCU NXP en S32 Design Studio · Sintonía de
controladores PI/PD/PID · Visión con OpenCV · Protocolos industriales
(MTConnect, MQTT, SMB) · Gestión de proyectos PMBOK.

---

# 7. Gestión de las Comunicaciones

## 7.1 Matriz de comunicaciones

| Qué | Quién | Canal | Frecuencia |
|---|---|---|---|
| Estado de tareas | Todo el equipo | Notion | Continuo |
| Coordinación diaria | Todo el equipo | Teams | Diario |
| Junta de avance | Todo el equipo | Teams (grabada) | Semanal, lunes |
| Reporte de avance | Rodrigo → docentes | Canvas | Por evidencia |
| Alertas de riesgo | Quien detecta → Rodrigo | Teams, inmediato | Al ocurrir |
| Documentos generados | Claude → Rodrigo → Teams | Archivos del canal | Al generar |
| Estado del proyecto | Claude → Rodrigo | Brief diario 7:03 am | Diario |

## 7.2 Repositorios de información

| Contenido | Dónde vive | Por qué ahí |
|---|---|---|
| Tareas, BOM, compras | **Notion** | Todo el equipo edita, sin cuentas de Claude |
| Conversación | **Teams** | Ya lo usan |
| Archivos pesados (CAD, STEP) | **Teams / SharePoint** | Notion no es para 40 MB |
| Documentación técnica, PO, OF | **Sistema local de Rodrigo** | Generado y versionado por Claude |
| Entregas oficiales | **Canvas** | Es lo que se califica |
| Código | **Repositorio Git** | Lo exige el profe (Área 3 de la Actividad 2) |

---

# 8. Gestión de los Riesgos

## 8.1 Registro de riesgos

| ID | Riesgo | Prob. | Impacto | Exposición | Respuesta | Dueño |
|---|---|---|---|---|---|---|
| R1 | LiDAR se retrasa 4+ semanas en importación | Alta | Crítico | **Muy alta** | **Mitigar:** comprar antes del 6 sep; preferir distribuidor nacional aunque cueste más. **Contingencia:** desarrollar Nav2 en Gazebo hasta que llegue | Compras |
| R2 | Riel lineal no llega o no cumple carrera | Media | Crítico | Alta | **Mitigar:** cotizar 2 proveedores. **Contingencia:** reducir carrera a 1.5 m y reubicar handoff | Compras |
| R3 | Batería LiFePO4 detenida en aduana | Media | Alto | Media | **Mitigar:** distribuidor nacional. **Contingencia:** banco de LiPo con BMS propio | Compras |
| R4 | Sin acceso al CNC Haas en noviembre | Media | Alto | Alta | **Mitigar:** reservar ventana **ya**. **Contingencia:** agente MTConnect simulado para demostrar la lógica | Rodrigo |
| R5 | El S32K312 no da ancho de banda para 4 lazos | Media | Medio | Media | **Mitigar:** medir frecuencia de lazo en F3 temprano. **Contingencia:** segundo MCU dedicado | Control |
| R6 | El equipo no cierra el BOM a tiempo | Alta | Crítico | **Muy alta** | **Mitigar:** fecha límite dura 1 sep; revisión diaria en Notion | Rodrigo |
| R7 | Fabricar el brazo consume el semestre | Alta | Crítico | **Muy alta** | **Evitar:** decidir cobot comercial vs propio antes del 28 ago | Rodrigo |
| R8 | Integrantes con carga desigual | Media | Medio | Media | **Mitigar:** RACI explícito y revisión semanal | Rodrigo |
| R9 | Pérdida de trabajo por no versionar | Media | Alto | Media | **Mitigar:** Git desde el día 1, respaldo en Teams | Software |
| R10 | Falla de seguridad en pruebas con el cobot | Baja | Crítico | Media | **Mitigar:** canal de seguridad separado, paro de emergencia probado antes de cualquier prueba con personas | Todos |

## 8.2 Reserva de contingencia
**15 % del presupuesto (~12,600 MXN)** y **1 semana de holgura** que solo puede
liberar el director de proyecto.

## 8.3 Disparadores de contingencia

| Si pasa esto... | ...se activa |
|---|---|
| PO no emitida al 6 sep | Escalar a docentes; evaluar componentes alternos disponibles localmente |
| Material sin llegar al 18 oct | Activar plan B de ese componente; congelar alcance del subsistema |
| Frecuencia de lazo < 200 Hz en F3 | Segundo MCU |
| Sin acceso al Haas al 1 nov | Demostrar con agente MTConnect simulado |

---

# 9. Gestión de las Adquisiciones

## 9.1 Proceso (automatizado)

```
Necesidad → alta en catálogo → cotización (2 proveedores) → PO → tránsito
   → recepción e inspección → alta de stock → kitting
```

| Paso | Herramienta | Comando |
|---|---|---|
| Alta de material | ERP local | `python sistema/erp.py material ...` |
| Consulta de estado | ERP local | `python sistema/erp.py estado` |
| Emisión de PO | ERP local | `python sistema/erp.py po ...` |
| Seguimiento | Notion "BOM y Compras" | Manual del equipo |

Cada material genera automáticamente su **carpeta de proveeduría** en
`02-proveeduria/fichas/<CÓDIGO>/` con ficha técnica, contacto y cotizaciones.

## 9.2 Codificación ERP
`<PREFIJO>-<TIPO>-<PARTE>` — ej. `INS-LID-2D-360`

| Categoría | Prefijo |
|---|---|
| POTENCIA | POT |
| INSTRUMENTACION | INS |
| MECANICA | MEC |
| INTERFACES | INT |
| REFACCIONES | REF |
| OTRO | OTR |

## 9.3 Compras críticas (emisión antes del 6 sep)

| Código | Material | Lead | Monto |
|---|---|---|---|
| MEC-RIE-LIN-2500 | Riel lineal 2.5 m | 6 sem | 28,000 |
| INS-LID-2D-360 | LiDAR 2D 360° | 6 sem | 4,500 |
| POT-BAT-LIFEPO4 | Batería LiFePO4 24 V | 5 sem | 9,500 |
| INT-MOD-IO-ETH | Módulo I/O Ethernet | 5 sem | 6,500 |
| INT-COM-SBC-ROS2 | SBC Linux para ROS 2 | 5 sem | 12,000 |
| | | | **60,500** |

---

# 10. Gestión de los Interesados

| Interesado | Interés | Influencia | Estrategia |
|---|---|---|---|
| **Equipo docente** (Carbajal, Abdiel) | Aprendizaje demostrable y trazabilidad | **Alta** | Gestionar de cerca: reportes por evidencia, consultas ante cambios de alcance |
| **Socio formador** | Solución transferible a industria | **Alta** | Evalúa la Evidencia Demostrativa: preparar con criterio industrial, no escolar |
| **Profe Dani (M3)** | Aplicación correcta de PMBOK | Media | Usar el Reto como caso de estudio en cada entrega del módulo |
| **Laboratorio de manufactura** | Uso seguro del CNC y del espacio | **Alta** | Reservar ventanas con anticipación, cumplir protocolos |
| **Equipo del proyecto** | Carga justa, aprender, aprobar | Alta | RACI explícito, Notion transparente |
| **Rodrigo** | Calificación y aprendizaje | Alta | Es el director de proyecto |

---

# 11. Diseño técnico por subsistema

## 11.1 AGV — Cinemática omnidireccional

Con 4 ruedas mecanum a 45°, semiancho $l_x$ y semilargo $l_y$, radio de rueda
$R$, y velocidad del cuerpo $(v_x, v_y, \omega_z)$, la **cinemática inversa** es:

$$
\begin{aligned}
\omega_1 &= \tfrac{1}{R}\left(v_x - v_y - (l_x + l_y)\,\omega_z\right) \\
\omega_2 &= \tfrac{1}{R}\left(v_x + v_y + (l_x + l_y)\,\omega_z\right) \\
\omega_3 &= \tfrac{1}{R}\left(v_x + v_y - (l_x + l_y)\,\omega_z\right) \\
\omega_4 &= \tfrac{1}{R}\left(v_x - v_y + (l_x + l_y)\,\omega_z\right)
\end{aligned}
$$

(numeración: 1 = frontal izquierda, 2 = frontal derecha, 3 = trasera izquierda,
4 = trasera derecha. **Verificar el signo contra el sentido real de los rodillos
antes de energizar** — un signo invertido hace que el AGV se mueva en diagonal
cuando se le pide avanzar.)

La **cinemática directa** (odometría) se obtiene invirtiendo:

$$
v_x = \tfrac{R}{4}(\omega_1+\omega_2+\omega_3+\omega_4), \quad
v_y = \tfrac{R}{4}(-\omega_1+\omega_2+\omega_3-\omega_4)
$$
$$
\omega_z = \tfrac{R}{4(l_x+l_y)}(-\omega_1+\omega_2-\omega_3+\omega_4)
$$

> **Advertencia de diseño:** las mecanum patinan por naturaleza. La odometría
> por encoders **acumula error rápido** y por eso la fusión con IMU y la
> corrección por LiDAR no son opcionales.

## 11.2 Control PI / PD / PID en el NXP

Lazo de velocidad por rueda, discreto con periodo $T$:

$$u[k] = K_p\,e[k] + K_i T \sum_{j=0}^{k} e[j] + K_d\,\frac{e[k]-e[k-1]}{T}$$

| Variante | Uso previsto | Por qué |
|---|---|---|
| **PI** | Velocidad de rueda | Elimina error permanente; sin D porque el encoder mete ruido en la derivada |
| **PD** | Posición del riel / orientación | Amortigua sin agregar error de estado estacionario |
| **PID** | Posición del AGV en docking | Necesita precisión y amortiguamiento simultáneos |

**Requisitos de implementación:**
- Frecuencia de lazo objetivo: **≥ 200 Hz por rueda** (4 lazos → verificar carga del MCU en F3, riesgo R5)
- **Anti-windup** obligatorio en el término integral (saturación del PWM)
- Filtro pasa-bajas en el término derivativo
- **Watchdog**: si no llega comando del supervisor en 200 ms → rampa a cero
- Rampa de aceleración para no derrapar los rodillos

**Método de sintonía:** partir de Ziegler-Nichols en lazo cerrado, refinar a
mano y **documentar cada juego de ganancias en bitácora** (lo pide QA).

## 11.3 Arquitectura de cómputo en 3 capas

| Capa | Hardware | Responsabilidad | Tiempo |
|---|---|---|---|
| **Bajo nivel** | NXP S32K312 | PWM, encoders, IMU, lazos PI/PD/PID, watchdog, paro seguro | Tiempo real duro (≥200 Hz) |
| **Supervisor a bordo** | SBC Linux | ROS 2 Humble, SLAM, Nav2, docking, cliente MQTT | Tiempo real suave |
| **Supervisor de celda** | PC industrial / PLC | Máquina de estados, MTConnect, SMB, handshake I/O | Orquestación |

> **El canal de seguridad va separado de la navegación.** El paro de emergencia
> es cableado y actúa sobre la etapa de potencia directamente — no pasa por el
> software del NXP ni de la SBC.

## 11.4 Navegación (ROS 2)

| Capa | Componente | Configuración |
|---|---|---|
| Mapeo | `slam_toolbox` | Modo online async; fusión LiDAR + odometría + IMU |
| Localización | AMCL o slam_toolbox en localization | Re-localización automática ante pérdida de pose |
| Planeación global | NavFn o SmacPlanner | SmacPlanner si se aprovecha holonomía |
| Planeación local | DWB o MPPI | **MPPI** aprovecha mejor el movimiento omnidireccional |
| Costmaps | Capa de obstáculos dinámicos | Inflación según envolvente del AGV con pallet |
| Recovery | Comportamientos de Nav2 | Rotación, retroceso, limpieza de costmap |
| **Docking** | Acción dedicada, **fuera de Nav2** | AprilTag + servo visual + conos de autoalineación + sensor inductivo |

## 11.5 Coordinación con el CNC Haas — 3 capas

| Capa | Protocolo | Dirección | Función |
|---|---|---|---|
| **Observación** | MTConnect HTTP `:8082/current` | Solo lectura | Polling 250 ms: Execution, ControllerMode, Availability, Program, alarmas |
| **Transferencia** | Net Share (SMB) | Escritura | Depósito de programas `.nc` con hash para evitar sobreescritura |
| **Handshake** | M-códigos + I/O discreta | Bidireccional | M21/M22 y relés auxiliares ↔ entradas del cobot |

**Máquina de estados nominal:**

```
IDLE → AGV_EN_TRANSITO → AGV_EN_HANDOFF → COBOT_TOMA_PIEZA
  → COBOT_DESPLAZA_RIEL → COBOT_DEPOSITA_FIXTURE → COBOT_RETRAE_SEGURO
    → VISION_VERIFICA → [pass] CICLO_HABILITADO → CNC_MAQUINANDO
      → CNC_CYCLE_STOP → COBOT_RETIRA_PIEZA → COBOT_DEPOSITA_PALLET
        → AGV_RETORNA → IDLE

[fail de visión] → ABORTA → NOTIFICA_OPERADOR → INTERVENCION_MANUAL
```

## 11.6 Visión — criterios de verificación

| # | Criterio | Método |
|---|---|---|
| 1 | Presencia de la pieza | Segmentación sobre ROI del fixture |
| 2 | Orientación correcta | Comparación contra plantilla de calibración |
| 3 | Asentamiento uniforme | Canal de profundidad como indicador de altura sobre topes |
| 4 | Ausencia de objetos extraños | Diferencia contra fondo de referencia (viruta, herramienta) |

**Calibración:** tablero **ChArUco** atornillado a la mesa en posición conocida
respecto al fixture, una vez por instalación. Marcadores **ArUco permanentes**
para detectar drift por vibración.
**Tiempo de respuesta objetivo:** < 3 s desde el disparo del supervisor.

---

# 12. Claude como agente y project manager

## 12.1 Qué hace Claude

| Función | Cómo |
|---|---|
| **Memoria del proyecto** | Todo dato duradero se escribe en archivos; no se pierde entre sesiones |
| **Emisión de documentos** | PO, OF y hojas viajeras en el formato del profe, numeradas y registradas |
| **Vigilancia de riesgos** | Calcula fechas de llegada por lead time y avisa qué está en riesgo |
| **Brief diario** | Tarea programada lun–sáb 7:03 am: clases, entregas, alertas |
| **Consulta técnica** | Índice de 65 documentos, 773 páginas: responde citando archivo y página |
| **Digitalización de notas** | Transcribe las libretas de GoodNotes y las conecta con el proyecto |
| **Sincronización** | Notion (equipo) ↔ archivos locales ↔ Google Calendar |

## 12.2 Qué NO hace Claude
- **No decide el alcance.** Señala las divergencias; la decisión es del equipo.
- **No compra ni compromete dinero.** Genera la PO; autoriza Rodrigo.
- **No sustituye al director de proyecto.** Rodrigo aprueba y responde.
- **No lo usa el equipo directamente.** Solo Rodrigo; nadie comparte la cuenta.

## 12.3 Ciclo de trabajo semanal

| Momento | Acción | Quién |
|---|---|---|
| Lunes AM | Junta de avance, actualizar Notion | Equipo |
| Lunes AM | `planea mi semana` + `estado del reto` | Rodrigo + Claude |
| Diario 7:03 | Brief automático con alertas | Claude |
| Al cotizar | Actualizar BOM en Notion | Quien cotiza |
| Al aprobar | `emite la PO de X` | Rodrigo + Claude |
| Tras cada clase | Auto-backup de notas; `procesa mis notas` | Claude |
| Viernes | Revisión de riesgos y avance vs plan | Rodrigo + Claude |

---

# 13. Control de versiones del plan

| Versión | Fecha | Cambios | Autor |
|---|---|---|---|
| 1.0 | 2026-08-25 | Emisión inicial | Rodrigo + Claude |

**Próxima revisión obligatoria:** 2026-09-06 (hito H1, emisión de PO críticas).
