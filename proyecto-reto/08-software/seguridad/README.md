# Seguridad

## Alcance
Cadena de paro de emergencia, supervisión de la zona de trabajo, límites de velocidad y lógica de parada segura ante obstáculo.

## Regla de diseño
Independiente del resto: un fallo en cualquier otro módulo no debe impedir el paro. Se valida por hardware, no solo por software.

## Tecnología
C sobre S32K312 · cableado discreto

## Responsable
⬜ _por asignar_

## Estado
Carpeta creada el 2026-09-04. Sin código aún.

## Convenciones
- Nombres de archivo en `kebab-case`, sin acentos ni espacios.
- Cada entrega de código incluye su prueba mínima y una nota de cómo ejecutarla.
- Las dependencias externas se declaran en el README de este módulo, no se asumen.
