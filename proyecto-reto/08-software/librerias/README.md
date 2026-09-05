# Librerías

## Alcance
Código reutilizable compartido por los demás módulos: cinemática mecanum, filtros, utilidades de matemáticas y tipos comunes.

## Regla de diseño
Sin dependencias hacia los otros módulos. Si una librería necesita importar de `comunicacion/` o `control/`, no es una librería.

## Tecnología
C / C++ para el MCU · Python para el supervisor

## Responsable
⬜ _por asignar_

## Estado
Carpeta creada el 2026-09-04. Sin código aún.

## Convenciones
- Nombres de archivo en `kebab-case`, sin acentos ni espacios.
- Cada entrega de código incluye su prueba mínima y una nota de cómo ejecutarla.
- Las dependencias externas se declaran en el README de este módulo, no se asumen.
