# Carta Proyecto

## Encargados del proyecto

- Perla Cecilia Renteria Rodriguez
- Samuel Sebastián Vázquez Gasca
- Osmar Artemio González Alatorre
- Rodrigo Herrera Baños
- Diego Giovanni Castellanos García

## Nombre del proyecto

Sistema de automatización para talleres de CNC

## Duración del proyecto

17 semanas

## Problemática

En los talleres de manufactura, la carga y descarga de piezas en máquinas CNC normalmente requiere la intervención de un operador. Esto genera tiempos improductivos, aumenta la dependencia de trabajo manual y limita la automatización del proceso, las soluciones comerciales de automatización mediante AGV y robot industriales suelen tener costos elevado, por lo tanto se propone desarrollar una celda automatizada de bajo costo que permita transportar, cargar, verificar y retirar piezas de un lugar especificado.

## Objetivo general

Diseñar, integrar y validar una celda ciberfísica de manufactura que automatice el traslado, manipulación e inspección de material previamente cortado desde el área de preparación hasta una máquina CNC, mediante un MoMa con un manipulador de 4 GDL, un cobot industrial sobre riel lineal, sistemas de visión e integración digital.

## Objetivos específicos

- Diseñar y fabricar un AGV capaz de transportar las piezas dentro del taller o laboratorio
- implementar navegación autónoma utilizando LiDAR
- Integrar un cobot sobre el chasis del AGV la cual ayudará a realizar la carga y descarga de piezas
- Implementar un sistema de visión que determine si la pieza está correctamente colocada
- Validar el funcionamiento completo de la celda mediante pruebas de carga, descarga y validación

## Alcance

Diseño e integración de un MoMa, entendido como una plataforma móvil con navegación inteligente con un manipulador robótico.

Diseño, implementación de un manipulador robótico de 4 GDL integrado en la plataforma móvil constituyendo un MoMa

Transportar el material desde el área de preparación hasta la zona de CNC.

Integrar un cobot industrial sobre el riel lineal para transferir piezas entre el MoMa y la CNC.

Integrar un sistema de visión e instrumentación para inspección, localización o verificación de piezas según la función que finalmente se defina.

Implementar comunicación digital entre los elementos de la celda.

Incorporar adquisición y procesamiento de datos del sistema.

Considerar seguridad industrial y ciberseguridad.

Documentar la arquitectura, diseño, integración, administración, pruebas y resultados del proyecto.

Entregar y demostrar un prototipo funcional integrado

Consideramos la comunicación integrada entre la celda ciber física y la máquina CNC para coordinar el intercambio de información sin embargo este último punto depende de la disponibilidad de uso y permiso de trabajo en la CNC del Campus, por lo que aunque lo consideramos dentro del alcance no aseguramos su cumplimiento.

## Entregables

Al finalizar el proyecto se esperar obtener un

- AGV funcional
- Sistema de navegación autónoma
- Estacion de entrega de piezas
- Cobot integrado al agv
- Comunicación entre el supervisor y máquinas de simulación
- Sistema de visión
- Integración de la celda completa
- Pruebas de funcionamiento
- Documentar técnica del proyecto
- Demostración final

## Restricciones

El proyecto buscará mantener un costo de manufactura bajo, seleccionando materiales y procesos que sean funcionales y accesibles. El AGV deberá alcanzar la estación final con una precisión de posicionamiento adecuada, permitiendo que la entrega de las piezas se realice correctamente. Además, el sistema de visión será utilizado para verificar que las piezas estén correctamente colocadas antes de continuar con el proceso de maquinado.

## Supuestos

La universidad proporcionará al menos un cobot industrial compatible con el proyecto

Habrá disponibilidad de un riel lineal o de los recursos necesarios para desarrollarlo e integrarlo

Será posible conseguir los sensores, cámaras, controladores y componentes mínimos necesarios para implementar el sistema.

El socio formador seguirá disponible para resolver dudas relevantes cuando sea necesario.

Los requisitos académicos y del socio formador no cambiarán drásticamente durante el semestre.

El equipo tendrá acceso a software y herramientas necesarias para desarrollo, simulación, programación y documentación.

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

- Retrasos en la planeación, manufactura de los componente
- Baja precisión en el posicionamiento de los objetos
- Fallas de sensores o cámaras integradas
- Problemas de comunicación (falta de wifi)
- Errores en la manipulación de piezas por el cobot
- Fallas en el sistema de visión
- Aumento de costos en el proyecto
- Problemas al momento de integración
- Riesgos o falla de seguridad
