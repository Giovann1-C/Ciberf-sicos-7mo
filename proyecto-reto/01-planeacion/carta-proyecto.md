# Carta Proyecto

## Sistema de Automatización para Talleres de CNC

**Documento:** Acta de Constitución del Proyecto (Project Charter) · PMBOK 7ª edición
**Versión:** 2.0 · **Fecha de emisión:** 2026-09-04
**Curso:** MR3005C.601 — Sistemas Ciber-Físicos · Módulo 3, Administración de Proyectos
**Institución:** Tecnológico de Monterrey, Campus Guadalajara

> ⬜ **Campos por confirmar con el Socio Formador.** Los recuadros marcados así
> requieren el dato directo del socio y no deben inventarse. Guion de la reunión
> en `preguntas-socio-formador.md`.

---

# 1. Participantes del Proyecto

## 1.1 Patrocinador / Socio Formador

| Campo | Dato |
|---|---|
| Organización | ⬜ _por confirmar_ |
| Representante | ⬜ _por confirmar_ |
| Cargo | ⬜ _por confirmar_ |
| Correo / teléfono | ⬜ _por confirmar_ |
| Rol | Define los requisitos industriales, facilita el acceso al taller y a la máquina CNC, y **evalúa la Evidencia 2 — Exposición Demostrativa** |

## 1.2 Cliente

Talleres de manufactura con máquinas CNC que hoy dependen de un operador para la
carga y descarga de piezas, y para los que las soluciones comerciales de
automatización resultan económicamente inaccesibles.

## 1.3 Interesados

| Interesado | Interés | Influencia | Estrategia de gestión |
|---|---|---|---|
| Socio Formador | Solución transferible y de bajo costo | Alta | Gestionar de cerca; entregables con criterio industrial, no escolar |
| Equipo docente (Oscar Carbajal, Abdiel) | Aprendizaje demostrable y trazabilidad | Alta | Reporte por evidencia; consulta ante cambios de alcance |
| Profesor de Administración de Proyectos (Dani) | Aplicación correcta del estándar PMBOK | Media | El Reto se usa como caso de estudio en cada entrega del módulo |
| Laboratorio de manufactura | Uso seguro de la máquina y del espacio | Alta | Reserva anticipada de ventanas; cumplimiento de protocolos |
| Equipo del proyecto | Carga equilibrada, aprendizaje, acreditación | Alta | Matriz RACI explícita y tablero Kanban público |

## 1.4 Proveedores y contratistas

| Proveedor | Suministro | Estado |
|---|---|---|
| NXP | Microcontroladores S32K312 y kits FRDM-S32K344 | OC-2026-003 emitida |
| Equipo docente | Riel lineal, LiDAR, módulo E/S Ethernet, balero de rodillos cruzados, motorreductor | Préstamo o donación comprometida |
| ⬜ _por definir_ | Batería LiFePO4 24 V 20 Ah | Por cotizar · **lead 5 semanas** |
| ⬜ _por definir_ | Cómputo supervisor clase Jetson Orin Nano | Por cotizar · **lead 5 semanas** |
| ⬜ _por definir_ | Cobot industrial para el riel lineal | **Disponibilidad y modelo por confirmar** |
| Fabricación interna | Chasis del AGV, manipulador de 4 GDL, estación de entrega, fixture y pallet | Por diseñar |

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

## 3.1 Problemática

En los talleres de manufactura, la carga y descarga de piezas en máquinas CNC
requiere normalmente la intervención de un operador. Esto genera tiempos
improductivos, aumenta la dependencia del trabajo manual y limita la
automatización del proceso.

Las soluciones comerciales basadas en AGV y robots industriales existen, pero su
costo las vuelve inaccesibles para el taller promedio. **El proyecto ataca ese
hueco:** una celda automatizada de bajo costo capaz de transportar, cargar,
verificar y retirar piezas de una posición determinada.

## 3.2 Objetivo general

Diseñar, integrar y validar una **celda ciberfísica de manufactura** que
automatice el traslado, la manipulación y la inspección de material previamente
cortado, desde el área de preparación hasta una máquina CNC, mediante un **MoMa
con manipulador de 4 grados de libertad**, un **cobot industrial sobre riel
lineal**, sistemas de visión e integración digital.

## 3.3 Objetivos específicos

| # | Objetivo | Criterio de éxito medible |
|---|---|---|
| OE1 | Diseñar y fabricar un AGV capaz de transportar las piezas dentro del taller o laboratorio | AGV desplazándose con carga nominal ⬜ _kg por definir_ |
| OE2 | Implementar navegación autónoma utilizando LiDAR | Recorrido completo del trayecto sin intervención del operador |
| OE3 | Integrar un manipulador de 4 GDL sobre el chasis del AGV, constituyendo el MoMa | Ciclo de toma y colocación ejecutado desde la plataforma móvil |
| OE4 | Implementar un sistema de visión que determine si la pieza está correctamente colocada | Dictamen de aceptación o rechazo emitido antes de autorizar el maquinado |
| OE5 | Validar el funcionamiento completo de la celda | Pruebas de carga, descarga y validación documentadas y repetibles |

## 3.4 Alcance

**Dentro del alcance**

- Diseño e integración de un **MoMa**: plataforma móvil con navegación inteligente y manipulador robótico a bordo
- Diseño e implementación de un **manipulador robótico de 4 GDL** integrado en la plataforma móvil
- Transporte del material desde el área de preparación hasta la zona de la CNC
- Integración de un **cobot industrial sobre riel lineal** para transferir piezas entre el MoMa y la CNC
- Sistema de visión e instrumentación para inspección, localización o verificación de piezas
- Comunicación digital entre los elementos de la celda
- Adquisición y procesamiento de datos del sistema
- **Seguridad industrial y ciberseguridad**
- Documentación de arquitectura, diseño, integración, administración, pruebas y resultados

**Fuera del alcance**

- Modificación del programa de maquinado o de los parámetros de corte de la CNC
- Certificación formal de seguridad ante organismo externo
- Producción en volumen: el entregable es un prototipo funcional demostrable
- Mantenimiento del sistema después de la fecha de cierre
- Operación desatendida sin supervisión humana presente

> **Nota de alcance — dos manipuladores.** El proyecto contempla un manipulador
> de 4 GDL de fabricación propia montado sobre el AGV, **y además** un cobot
> industrial comercial sobre el riel lineal. Son elementos distintos con
> proveeduría, control y calendario distintos. Confirmar esta lectura antes de
> congelar el diseño: si se trata de un solo manipulador, el alcance y el
> presupuesto cambian de manera sustancial.

## 3.5 Entregables

| # | Entregable | Fase |
|---|---|---|
| E1 | AGV funcional | F3 |
| E2 | Sistema de navegación autónoma | F4 |
| E3 | Estación de entrega de piezas | F3 |
| E4 | Manipulador de 4 GDL integrado al AGV (MoMa) | F4 |
| E5 | Cobot integrado sobre el riel lineal | F5 |
| E6 | Comunicación entre el supervisor y las máquinas | F5 |
| E7 | Sistema de visión | F5 |
| E8 | Integración de la celda completa | F5 |
| E9 | Pruebas de funcionamiento | F6 |
| E10 | Documentación técnica del proyecto | F6 |
| E11 | Demostración final | F6 |

---

# 4. Calendario

| Concepto | Valor |
|---|---|
| Fecha de inicio | 2026-08-10 |
| Fecha de cierre | 2026-12-06 |
| Duración | 18 semanas |
| Reporte de avance | Semanal al equipo docente; tablero Kanban de actualización continua |
| Revisión con el Socio Formador | ⬜ _frecuencia por acordar_ |

> **Ajuste de calendario.** Dieciocho semanas contadas desde el 10 de agosto
> terminan el 14 de diciembre, después de la entrega del Reporte Integrador del
> 6 de diciembre. El cronograma siguiente comprime las últimas semanas para
> cerrar el 6 de diciembre. Si el proyecto arrancó antes del 10 de agosto,
> corregir la fecha de inicio.

## Cronograma por semana

| Sem. | Periodo | Actividad | Entregable de la semana |
|---|---|---|---|
| 1 | 10–16 ago | Análisis del proceso actual de carga y descarga | Diagrama SIPOC y de causa-efecto |
| 2 | 17–23 ago | Levantamiento de requisitos y trazabilidad | Matriz de trazabilidad de requisitos |
| 3 | 24–30 ago | Arquitectura de la celda y desglose del trabajo | WBS y matriz RACI |
| 4 | 31 ago–6 sep | **Selección de sensores y cierre del BOM** | BOM congelado · **PO críticas emitidas** |
| 5 | 7–13 sep | Diseño mecánico del chasis y del manipulador de 4 GDL | Cinemática directa e inversa resueltas |
| 6 | 14–20 sep | Diseño eléctrico, potencia y arnés | Diagrama unifilar y de conexiones |
| 7 | 21–27 sep | Arquitectura de software y simulación del proceso | **Diseño congelado** · simulación validada |
| 8 | 28 sep–4 oct | Fabricación del chasis y montaje de tracción | Chasis ensamblado |
| 9 | 5–11 oct | Fabricación y ensamble del manipulador de 4 GDL | Manipulador armado |
| 10 | 12–18 oct | Firmware de control: lazos PI, PD y PID | Sintonía documentada con gráficas |
| 11 | 19–25 oct | Estación de entrega, fixture y pallet indexado | **AGV rodando con control cerrado** |
| 12 | 26 oct–1 nov | Navegación autónoma con LiDAR | SLAM y planeación operativos |
| 13 | 2–8 nov | Integración del manipulador al AGV — MoMa completo | **Navegación y toma de pieza validadas** |
| 14 | 9–15 nov | Integración del cobot sobre el riel lineal | Transferencia MoMa ↔ CNC |
| 15 | 16–22 nov | Sistema de visión y comunicación con el supervisor | **Ciclo completo de la celda** |
| 16 | 23–29 nov | Pruebas de carga, descarga y validación | Protocolo de pruebas ejecutado |
| 17 | 30 nov–6 dic | Seguridad industrial y ciberseguridad · documentación | **Documentación técnica entregada** |
| 18 | 7–13 dic | Demostración final y cierre | Demostración ante el Socio Formador |

---

# 5. Estimación de Costos

Valores en pesos mexicanos, del catálogo del sistema ERP del proyecto
(`02-proveeduria/catalogo-materiales.csv`).

| Concepto | Monto (MXN) |
|---|---|
| Material aportado por el equipo docente (préstamo o donación) | $67,650.00 |
| Material por adquirir | $46,487.15 |
| **Subtotal cubierto por el BOM vigente** | **$114,137.15** |
| Manipulador de 4 GDL (actuadores, reductores, estructura) | ⬜ _por cotizar_ |
| Cobot industrial para el riel lineal | ⬜ _por confirmar si se presta o se adquiere_ |

## Partidas por adquirir con mayor impacto en calendario

| Concepto | Cant. | Monto | Lead time |
|---|---|---|---|
| Cómputo supervisor clase Jetson Orin Nano | 1 | $12,000.00 | **5 semanas** |
| Batería LiFePO4 24 V 20 Ah con BMS | 1 | $9,500.00 | **5 semanas** |
| Ruedas de tracción | 4 | $7,200.00 | 3 semanas |
| Kits de desarrollo FRDM-S32K344 | 5 | $5,537.15 | 1 semana |
| Perfil estructural de aluminio 40×40 | 8 m | $3,360.00 | 2 semanas |
| Sensores inductivos M12 | 4 | $2,600.00 | 2 semanas |
| Cargador de batería 24 V | 1 | $2,100.00 | 3 semanas |
| Botones de paro de emergencia | 2 | $1,780.00 | 2 semanas |
| Convertidores DC-DC 24 V → 5 V | 2 | $1,560.00 | 2 semanas |
| Unidad inercial de 9 GDL | 1 | $850.00 | 3 semanas |

> **Nota de gestión.** La restricción de bajo costo es un requisito del proyecto,
> no una consecuencia. Cada selección de material debe justificarse contra una
> alternativa comercial más cara, y esa comparación es parte de la documentación
> técnica.
>
> **Los dos artículos de lead time más largo determinan la ruta crítica.** Deben
> cotizarse y emitirse **antes del 29 de septiembre de 2026**.

---

# 6. Hitos del Proyecto

| Hito | Descripción | Semana | Fecha |
|---|---|---|---|
| H1 | BOM congelado y órdenes de compra críticas emitidas | 4 | 2026-09-06 |
| H2 | Diseño de detalle congelado y simulación validada | 7 | 2026-09-27 |
| H3 | AGV rodando con lazos de control sintonizados | 11 | 2026-10-25 |
| H4 | MoMa completo: navegación autónoma y manipulación validadas | 13 | 2026-11-08 |
| H5 | Celda integrada: cobot, visión y comunicación operando en ciclo | 15 | 2026-11-22 |
| H6 | Pruebas de validación concluidas y documentación entregada | 17 | 2026-12-06 |

---

# 7. Restricciones

| # | Restricción | Implicación |
|---|---|---|
| RE1 | **Costo de manufactura bajo** | Materiales y procesos funcionales y accesibles; cada selección se justifica contra la alternativa comercial |
| RE2 | **Precisión de posicionamiento del AGV** en la estación final | ⬜ _tolerancia por definir_ — determina si basta la odometría o se requiere referencia visual en el acoplamiento |
| RE3 | **Verificación por visión antes del maquinado** | Ninguna pieza avanza sin dictamen de colocación correcta |
| RE4 | Duración de 18 semanas improrrogables | El calendario académico no admite extensión |
| RE5 | El NXP S32K312 no ejecuta ROS 2 | Se requiere una SBC con Linux como cómputo supervisor |
| RE6 | Acceso a la máquina CNC sujeto a la programación del laboratorio | No está bajo control del equipo |
| RE7 | Normativa de seguridad aplicable | ⬜ _por confirmar cuál_ |

---

# 8. Supuestos y Dependencias

## 8.1 Supuestos

1. El equipo docente entrega el riel lineal, el LiDAR, el módulo de E/S Ethernet, el balero de rodillos cruzados y el motorreductor en tiempo para la fase de fabricación.
2. Cada integrante dedica al menos 12 h/semana al proyecto.
3. Se dispone de un cobot industrial para montar sobre el riel lineal, ya sea en préstamo o por adquisición.
4. El área de operación tiene piso plano y continuo, apto para la tracción del AGV.
5. Los precios del catálogo se mantienen dentro de un margen del 15 % al cotizar.
6. Existe acceso a taller y herramienta para fabricar el chasis y el manipulador de 4 GDL.

## 8.2 Dependencias

- La fabricación del chasis depende de la recepción del perfil de aluminio y de las ruedas.
- La navegación autónoma depende del cómputo supervisor y del LiDAR.
- El diseño del efector y del fixture depende de conocer la **pieza real** a manipular. ⬜ _por confirmar_
- La integración de la celda depende del acceso a la máquina CNC y del cobot sobre el riel.
- El manipulador de 4 GDL depende del presupuesto de actuadores, todavía sin cotizar.

---

# 9. Riesgos

Escala de probabilidad e impacto: Baja / Media / Alta.

| # | Riesgo | Prob. | Impacto | Exposición | Respuesta |
|---|---|---|---|---|---|
| R1 | **Fabricar el manipulador de 4 GDL consume el semestre.** Diseñar, maquinar, ensamblar y controlar un brazo propio es un proyecto completo por sí mismo | Alta | Crítico | **Muy alta** | **Mitigar:** congelar el diseño del brazo en la semana 7 sin excepción. **Contingencia:** reducir a 3 GDL o adquirir un brazo educativo comercial |
| R2 | **El cobot del riel no está disponible** cuando toca la fase 5 | Media | Crítico | Alta | **Mitigar:** confirmar modelo y fecha con el Socio Formador de inmediato. **Contingencia:** demostrar la transferencia con el manipulador del MoMa |
| R3 | **El cómputo supervisor o la batería no llegan** — 5 semanas de lead time | Media | Crítico | Alta | **Mitigar:** emitir órdenes antes del 29-sep. **Contingencia:** desarrollar navegación en simulación mientras llegan |
| R4 | **Sin acceso a la máquina CNC** en la ventana de integración | Media | Alto | Alta | **Mitigar:** reservar la ventana desde ahora. **Contingencia:** integrar contra una máquina simulada |
| R5 | **El peso del manipulador desestabiliza el AGV.** Montar un brazo sobre la plataforma sube el centro de gravedad y el par de vuelco al extender | Media | Alto | Alta | **Mitigar:** análisis de estabilidad antes de fabricar; limitar velocidad con el brazo extendido. **Contingencia:** contrapeso o ampliación de la base |
| R6 | **La precisión de posicionamiento del AGV no basta** para que el manipulador tome la pieza | Media | Alto | Alta | **Mitigar:** definir la tolerancia en la semana 2 y diseñar hacia ella. **Contingencia:** corrección fina por visión en el acoplamiento |
| R7 | **La restricción de bajo costo choca con la precisión requerida.** Los componentes accesibles tienen más juego mecánico y menos repetibilidad | Media | Alto | Media | **Mitigar:** compensar en software con realimentación visual antes que con hardware más caro |
| R8 | **El consumo del manipulador reduce la autonomía** del AGV por debajo de lo necesario para un ciclo completo | Media | Medio | Media | **Mitigar:** presupuesto energético en el diseño eléctrico. **Contingencia:** ciclo con recarga intermedia |
| R9 | **El S32K312 no sostiene el lazo** de tracción y del manipulador a la vez | Media | Medio | Media | **Mitigar:** medir la frecuencia de lazo en fase temprana. **Contingencia:** segundo MCU dedicado al brazo |
| R10 | **Ciberseguridad tratada como accesorio** y descubierta en la última semana | Alta | Medio | Alta | **Mitigar:** incluirla desde el diseño de la arquitectura de comunicación, no al final |
| R11 | **La iluminación del taller degrada el sistema de visión** — viruta, refrigerante y sombras cambiantes | Media | Medio | Media | **Mitigar:** iluminación propia controlada en la estación de inspección |
| R12 | **Carga desigual entre integrantes** | Media | Medio | Media | **Mitigar:** matriz RACI explícita y revisión semanal en el tablero Kanban |
| R13 | **El alcance del manipulador se malinterpreta** — uno o dos brazos, según la sección del documento que se lea | Alta | Crítico | **Muy alta** | **Evitar:** cerrarlo por escrito con el Socio Formador antes de la semana 5 |

> **Los tres riesgos de exposición muy alta —R1, R13 y el par R2/R3— comparten
> una causa: decisiones de alcance y de compra que siguen abiertas.** Ninguno se
> resuelve con más trabajo técnico; se resuelven con una decisión y una firma.

---

# 10. Autorización

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
| 1.0 | 2026-09-04 | Emisión inicial |
| 2.0 | 2026-09-04 | Se adopta la definición oficial del proyecto: nombre, problemática, objetivos, alcance de MoMa con manipulador de 4 GDL más cobot sobre riel, entregables y restricciones. Se desarrolla el cronograma a 18 semanas y se agrega la matriz de riesgos |

**Documentos relacionados**
`pmi-plan-direccion-proyecto.md` · `plan-de-trabajo.md` · `preguntas-socio-formador.md` · `02-proveeduria/catalogo-materiales.csv`
