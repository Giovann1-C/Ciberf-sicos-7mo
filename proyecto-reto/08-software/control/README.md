# Control

## Alcance
Lazos PI, PD y PID sobre el NXP S32K312, cinemática inversa de las cuatro ruedas mecanum y perfilado de velocidad.

## Regla de diseño
La frecuencia de lazo se mide y se documenta. Cada ganancia sintonizada se registra con su método y su gráfica de respuesta.

## Tecnología
C sobre S32K312 · driver **RoboClaw ST 2x45A** (×2, uno por eje del AGV)

## Responsable
⬜ _por asignar_

## Arquitectura elegida (CC-002, 2026-10-10)

```
S32K312 ──LPUART (Packet Serial, dir. 0x80)──► RoboClaw #1 ── M1, M2 (ruedas delanteras)
   │                                        └► RoboClaw #2 ── M3, M4 (ruedas traseras)
   │  PI propio en el MCU: lee qpps (cmd 18) y manda duty (cmd 32)
   └─ El encoder de cuadratura entra al RoboClaw. E-stop físico en S3 + Serial Timeout
```

- **No** se usa el PID interno del RoboClaw en la versión final. La rúbrica evalúa el PI/PID propio.
- Las protecciones del RoboClaw (corriente, voltaje y timeout) quedan activas.

## Estado

| Fecha | Qué | Evidencia |
|---|---|---|
| 2026-09-25 | Un **motor del AGV** (CHP 42GP-775 con encoder) se movió con el RoboClaw desde el S32K312. Se configuró el RoboClaw: firmware 4.4.9, límites de batería 10–16 V para la fuente de banco y sentido del encoder. | Act. 7.2 de M7 (individual, Rodrigo) |
| 2026-09-25 | Planta identificada a 12 V: 25/50/75/100 % de duty → 1042/2170/3293/4399 qpps (lineal). | Ídem |
| 2026-09-25 | Modelo FOPDT y PI por SIMC con $\tau_c$ = 0.05 s: $K_p \approx 3.0\times10^{-4}$, $K_i \approx 2.9\times10^{-3}$, lazo a 100 Hz. | Ídem |
| 2026-10-03 | **Laboratorio NXP + RoboClaw.** Comunicación y telemetría (posición, velocidad, voltaje) validadas con la batería del AGV a 23.6 V. Control de velocidad con el PID interno del RoboClaw, motor armado, consignas de 100 a 5000 qpps (máximo medido: 5050 qpps). | `ensayos/2026-10-03-laboratorio-nxp/` |

$$G(s) = \frac{4400\,e^{-0.028 s}}{0.104 s + 1}\quad[\text{qpps}/\text{duty}]$$

### Ensayos del 2026-10-03

| Archivo | Etapa | Duración | Resultado |
|---|---|---|---|
| `lectura_01/02.csv` | Telemetría, solo lectura | 55 s | Lecturas válidas, 23.6 V |
| `ensayo_01/02.csv` | Telemetría, solo lectura | 58 s | Lecturas válidas |
| `ensayo_03.csv` | Velocidad con el PID interno del RoboClaw | 600 s | Consignas 100/200/3000/5000 qpps. Posición acumulada de 362 428 conteos |

### Pendiente
- [x] PI propio en el S32K312 en lazo cerrado con **1 motor** (Act. 7.2: pruebas de lazo cerrado y ajuste de Ki, 2026-09-25).
- [ ] Ensayo del PID NXP en el banco del laboratorio (etapa 4) y después con los 4 motores. No hay registro todavía.
- [ ] Control de posición en cascada (etapa 5).
- [ ] Segundo RoboClaw y cinemática inversa mecanum de 4 ruedas en el MCU.
- [ ] Medir la frecuencia real del lazo con 4 ruedas (meta ≥ 200 Hz por rueda, riesgo R5).

## Convenciones
- Nombres de archivo en `kebab-case`, sin acentos ni espacios.
- Cada entrega de código incluye su prueba mínima y una nota de cómo ejecutarla.
- Las dependencias externas se declaran en el README de este módulo, no se asumen.
