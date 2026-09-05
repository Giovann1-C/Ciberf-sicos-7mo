# Software de la Celda Ciberfísica

Mapa de módulos del proyecto. Cada carpeta es un área funcional con un
responsable único y una frontera clara: si dos módulos necesitan lo mismo, eso
vive en `librerias/`.

## Módulos

| Carpeta | Área | Alcance | Responsable |
|---|---|---|---|
| `08-software/librerias/` | Librerías | Código reutilizable compartido por los demás módulos: cinemática mecanum, filtros, utilidades de matemáticas y tipos comunes | ⬜ _por asignar_ |
| `08-software/comunicacion/` | Comunicación | Cliente MTConnect contra el Haas, transferencia de programas por SMB, handshake discreto por códigos M, publicación MQTT del estado del AGV y enlace serie MCU↔SBC | ⬜ _por asignar_ |
| `08-software/control/` | Control | Lazos PI, PD y PID sobre el NXP S32K312, cinemática inversa de las cuatro ruedas mecanum y perfilado de velocidad | ⬜ _por asignar_ |
| `08-software/navegacion/` | Navegación | SLAM, planeación de trayectorias, acoplamiento por AprilTag y máquina de estados de misión del AGV | ⬜ _por asignar_ |
| `08-software/vision/` | Visión | Calibración ChArUco, verificación del asentamiento de la pieza en el fixture y dictamen de aceptación o rechazo | ⬜ _por asignar_ |
| `08-software/diagnostico/` | Diagnóstico | Registro de eventos, telemetría, detección de fallas, autoprueba al arranque y tablero de estado de la celda | ⬜ _por asignar_ |
| `08-software/seguridad/` | Seguridad | Cadena de paro de emergencia, supervisión de la zona de trabajo, límites de velocidad y lógica de parada segura ante obstáculo | ⬜ _por asignar_ |

## Por qué está partido así

La celda tiene tres procesadores distintos —el MCU de control, el cómputo
supervisor y el control del CNC— y tres canales de comunicación entre ellos. Sin
fronteras explícitas, el código de comunicación termina disperso en los módulos
de control y cada cambio en el protocolo obliga a tocar todo.

La separación también permite trabajo en paralelo: navegación puede desarrollarse
en simulación mientras el hardware está en tránsito, sin bloquear a control.

## Dependencias permitidas

```
seguridad      -> (ninguna)          independiente por diseño
librerias      -> (ninguna)
control        -> librerias
comunicacion   -> librerias
navegacion     -> librerias, comunicacion
vision         -> librerias
diagnostico    -> librerias
```

**`seguridad/` no depende de nada.** Un fallo en cualquier otro módulo no debe
impedir que el paro de emergencia funcione.

## Cómo contribuir

1. Trabaja solo dentro de la carpeta de tu área.
2. Actualiza el README de tu módulo con lo que agregaste y cómo se prueba.
3. Sube el cambio a GitHub; el avance se detecta desde ahí con `herramientas/avance.py`.
