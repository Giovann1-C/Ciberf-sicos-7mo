# Carta Proyecto

## Nombre del proyecto

Sistema de automatización para talleres de CNC

## Socio formador

Organización: ⬜ _por confirmar_
Representante: ⬜ _por confirmar_
Cargo: ⬜ _por confirmar_
Contacto: ⬜ _por confirmar_

## Duración del proyecto

18 semanas

## Problemática

En los talleres de manufactura, la carga y descarga de piezas en máquinas CNC normalmente requiere la intervención de un operador. Esto genera tiempos improductivos, aumenta la dependencia de trabajo manual y limita la automatización del proceso. Las soluciones comerciales de automatización mediante AGV y robots industriales suelen tener costos elevados, por lo tanto se propone desarrollar una celda automatizada de bajo costo que permita transportar, cargar, verificar y retirar piezas de un lugar especificado.

## Objetivo general

Diseñar, integrar y validar una celda ciberfísica de manufactura que automatice el traslado, manipulación e inspección de material previamente cortado desde el área de preparación hasta una máquina CNC, mediante un MoMa con un manipulador de 4 GDL, un cobot industrial sobre riel lineal, sistemas de visión e integración digital.

## Objetivos específicos

- Diseñar y fabricar un AGV capaz de transportar las piezas dentro del taller o laboratorio.
- Implementar navegación autónoma utilizando LiDAR.
- Integrar un manipulador de 4 GDL sobre el chasis del AGV, el cual ayudará a realizar la carga y descarga de piezas.
- Implementar un sistema de visión que determine si la pieza está correctamente colocada.
- Validar el funcionamiento completo de la celda mediante pruebas de carga, descarga y validación.

## Alcance

Diseño e integración de un MoMa, entendido como una plataforma móvil con navegación inteligente y un manipulador robótico a bordo.

Diseño e implementación de un manipulador robótico de 4 GDL integrado en la plataforma móvil, constituyendo un MoMa.

Transportar el material desde el área de preparación hasta la zona de CNC.

Integrar un cobot industrial sobre el riel lineal para transferir piezas entre el MoMa y la CNC.

Integrar un sistema de visión e instrumentación para inspección, localización o verificación de piezas según la función que finalmente se defina.

Implementar comunicación digital entre los elementos de la celda.

Incorporar adquisición y procesamiento de datos del sistema.

Considerar seguridad industrial y ciberseguridad.

Documentar la arquitectura, diseño, integración, administración, pruebas y resultados del proyecto.

Entregar y demostrar un prototipo funcional integrado.

Consideramos la comunicación integrada entre la celda ciberfísica y la máquina CNC para coordinar el intercambio de información. Sin embargo, este último punto depende de la disponibilidad de uso y del permiso de trabajo en la CNC del Campus, por lo que, aunque el desarrollo de la comunicación forma parte del alcance, su validación contra la máquina real queda condicionada a que se otorgue dicho acceso. En caso de no obtenerlo, la comunicación se demostrará contra un entorno de simulación que reproduzca el comportamiento del control de la máquina.

## Entregables

Al finalizar el proyecto se espera obtener:

- AGV funcional
- Sistema de navegación autónoma
- Estación de entrega de piezas
- Manipulador integrado al AGV
- Comunicación entre el supervisor y las máquinas o su simulación
- Sistema de visión
- Integración de la celda completa
- Pruebas de funcionamiento
- Documentación técnica del proyecto
- Demostración final

## Restricciones

El proyecto buscará mantener un costo de manufactura bajo, seleccionando materiales y procesos que sean funcionales y accesibles. El AGV deberá alcanzar la estación final con una precisión de posicionamiento adecuada, permitiendo que la entrega de las piezas se realice correctamente. Además, el sistema de visión será utilizado para verificar que las piezas estén correctamente colocadas antes de continuar con el proceso de maquinado.

La duración de 18 semanas es improrrogable, ya que está determinada por el calendario académico.

El acceso a la máquina CNC del Campus no está bajo control del equipo y depende de la programación del laboratorio.

El microcontrolador NXP S32K312 no puede ejecutar ROS 2, por lo que se requiere una computadora con Linux como cómputo supervisor.

## Cronograma

**Semanas 1 y 2. Análisis del proceso.** Levantamiento del proceso actual de carga y descarga, identificación de tiempos improductivos y definición de los requisitos del sistema con el socio formador.

**Semanas 3 y 4. Selección de sensores y cierre de la lista de materiales.** Definición de LiDAR, cámaras, encoders e instrumentación. Cierre del BOM y emisión de las órdenes de compra de los componentes con mayor tiempo de entrega.

**Semanas 5 a 7. Diseño de detalle.** Diseño mecánico del chasis y del manipulador de 4 GDL con su cinemática directa e inversa, diseño eléctrico y de potencia, y arquitectura de software de la celda. Al cierre de la semana 7 el diseño queda congelado.

**Semanas 8 a 11. Fabricación e integración mecánica.** Fabricación del chasis, montaje del sistema de tracción, ensamble del manipulador de 4 GDL, construcción de la estación de entrega y programación de los lazos de control PI, PD y PID sobre el microcontrolador.

**Semanas 12 y 13. Navegación autónoma.** Implementación del mapeo y la localización con LiDAR, planeación de trayectorias e integración del manipulador con la plataforma móvil para completar el MoMa.

**Semanas 14 y 15. Integración de la celda.** Montaje del cobot industrial sobre el riel lineal, implementación del sistema de visión y de la comunicación digital entre el supervisor y las máquinas.

**Semanas 16 y 17. Pruebas y resultados.** Ejecución del protocolo de pruebas de carga, descarga y validación. Verificación de la seguridad industrial y de la ciberseguridad del sistema. Documentación técnica.

**Semana 18. Demostración final.** Presentación del prototipo funcional integrado ante el socio formador y entrega del expediente documental completo.

## Riesgos

**Fabricar el manipulador de 4 GDL puede consumir el semestre completo.** Diseñar, maquinar, ensamblar y controlar un brazo propio es un proyecto por sí mismo. Para evitarlo, el diseño del manipulador se congela al cierre de la semana 7 sin excepción; si para entonces no está resuelto, se reduce a 3 grados de libertad o se sustituye por un brazo educativo comercial.

**El cobot industrial para el riel lineal podría no estar disponible** cuando llegue la fase de integración. Se debe confirmar modelo y fecha de disponibilidad con el socio formador de inmediato. Si no se consigue, la transferencia de piezas se demuestra con el manipulador del propio MoMa.

**Los componentes con mayor tiempo de entrega pueden llegar tarde.** El cómputo supervisor y la batería tienen cinco semanas de plazo de entrega, por lo que sus órdenes de compra deben emitirse antes del 29 de septiembre. Mientras llegan, la navegación se desarrolla en simulación para no detener el avance.

**El acceso a la máquina CNC del Campus no está garantizado.** La ventana de trabajo debe reservarse desde ahora con el laboratorio. Si no se obtiene, la comunicación se valida contra un entorno de simulación que reproduzca el comportamiento del control.

**El peso del manipulador puede desestabilizar el AGV.** Montar un brazo sobre la plataforma eleva el centro de gravedad y genera par de vuelco cuando el brazo se extiende. Se debe realizar el análisis de estabilidad antes de fabricar el chasis y limitar la velocidad de desplazamiento con el brazo extendido; de ser necesario, se amplía la base o se agrega contrapeso.

**La precisión de posicionamiento del AGV podría no ser suficiente** para que el manipulador tome la pieza correctamente. La tolerancia debe definirse con un número concreto en las primeras semanas y diseñarse hacia ella. Si la odometría no alcanza, se corrige con realimentación visual en el momento del acoplamiento.

**La restricción de bajo costo entra en tensión con la precisión requerida.** Los componentes accesibles tienen más juego mecánico y menor repetibilidad. La estrategia es compensar en software mediante realimentación visual antes que recurrir a hardware más caro, lo cual además refuerza la propuesta de valor del proyecto.

**El consumo del manipulador puede reducir la autonomía del AGV** por debajo de lo necesario para completar un ciclo. Se debe elaborar el presupuesto energético durante el diseño eléctrico y, en caso necesario, contemplar una recarga intermedia dentro del ciclo.

**El microcontrolador podría no sostener simultáneamente el lazo de tracción y el del manipulador.** La frecuencia de lazo debe medirse en la fase temprana de firmware. Si no alcanza, se dedica un segundo microcontrolador al brazo.

**La ciberseguridad suele tratarse como un accesorio y descubrirse al final.** Debe incorporarse desde el diseño de la arquitectura de comunicación, no en la última semana.

**La iluminación del taller puede degradar el sistema de visión** por efecto de viruta, refrigerante y sombras cambiantes. La estación de inspección debe contar con iluminación propia controlada.

**La carga de trabajo puede repartirse de forma desigual entre los integrantes.** Se mitiga con una matriz de responsabilidades explícita y revisión semanal del avance en el tablero del equipo.

**El alcance del manipulador puede malinterpretarse.** El proyecto contempla un manipulador de 4 GDL de fabricación propia sobre el AGV y, además, un cobot industrial comercial sobre el riel lineal. Son elementos distintos, con proveeduría y calendario distintos. Esta interpretación debe confirmarse por escrito con el socio formador antes de la semana 5, ya que de ella dependen el presupuesto y el calendario completos.
