# Comunicación

## Alcance
Cliente MTConnect contra el Haas, transferencia de programas por SMB, handshake discreto por códigos M, publicación MQTT del estado del AGV y enlace serie MCU↔SBC.

## Regla de diseño
Todo mensaje entrante se valida antes de usarse. Ningún módulo habla directo con la máquina: pasan por aquí.

## Tecnología
Python (SBC) · C (MCU)

## Responsable
⬜ _por asignar_

## Estado
Carpeta creada el 2026-09-04. Sin código aún.

## Convenciones
- Nombres de archivo en `kebab-case`, sin acentos ni espacios.
- Cada entrega de código incluye su prueba mínima y una nota de cómo ejecutarla.
- Las dependencias externas se declaran en el README de este módulo, no se asumen.
