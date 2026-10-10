# Impresión de los rodillos mecanum en CR-TPU (95A)

Fecha: 2026-10-03 · Pieza: `rodilla_mecanum.SLDPRT` (V6)

## Geometría que importa para imprimir

| Dato | Valor |
|---|---|
| Largo | 57 mm |
| Diámetro máximo (centro) | Ø23.4 |
| Diámetro en las puntas | Ø15.75 |
| Perfil | Arco R108.3. La pared más inclinada está a 15° de la vertical |
| Barreno pasado | Ø6.55 para el eje de Ø6.35 |
| Contraalojamientos para bujes | Ø10.75 en ambas puntas |
| Volumen aproximado | ~17 cm³: ~21 g al 100 % · 12 por rueda, 48 + repuestos |

## Orientación: vertical, parado sobre una punta

- La sección queda redonda: no hay cara plana ni soportes sobre la superficie que rueda.
- La pared más inclinada está a 15° de la vertical, así que **no necesita soportes**.
- El barreno y los contraalojamientos salen redondos y concéntricos.
- El techo del contraalojamiento de abajo es un puente anular de ~2 mm. El TPU lo resuelve sin soporte.
- **Acostado no conviene:** queda una cara plana o una franja de soportes justo en la banda de rodadura, y la rueda golpearía en cada vuelta.

## Ajustes del laminador (punto de partida)

| Parámetro | Valor | Por qué |
|---|---|---|
| Secado | 50–55 °C, 4–6 h antes de imprimir | El TPU húmedo da hilos, burbujas y superficie rugosa |
| Boquilla / altura de capa | 0.4 mm / 0.2 mm | |
| Temperatura | 220–230 °C (confirmar en la etiqueta del rollo) | |
| Cama | 40–50 °C. PEI texturizado, o pegamento en barra como desmoldante en PEI liso o vidrio | En PEI liso el TPU se pega demasiado y puede arrancar la capa |
| Velocidad | Primera capa 15 mm/s · pared exterior 20 · resto 25–30 mm/s, o un flujo máximo de ~3–4 mm³/s | El TPU se comprime en el extrusor si se le exige velocidad |
| Retracción | Extrusor directo: 0.5–1.0 mm a 20–30 mm/s · Bowden: ≤ 2 mm o apagada | Más retracción atasca el filamento |
| Salto en Z | Apagado | Genera hilos y empuja la pieza |
| Viajes | Evitar cruzar perímetros / "combing" dentro de la pieza | Menos hilos entre rodillos |
| Ventilador | 0 % en las 2 primeras capas, luego 60–100 % | |
| Paredes | 4 (≥ 1.6 mm) | La pared toma el contacto con el piso |
| Relleno | Giroide 50–60 % | Si los rodillos se aplastan visiblemente con el peso del robot, subir a 100 % |
| Capas superior/inferior | 5 (1.0 mm) | |
| Costura | Alineada en una línea, con costura biselada ("scarf seam") si el laminador la tiene | La costura aleatoria deja granitos por toda la banda de rodadura |
| Borde (brim) | 4–5 mm | La base es de Ø15.75 para 57 mm de alto. Sin borde se tambalea arriba |
| Separación entre piezas | ≥ 10 mm | |

**Lotes:** 6–12 rodillos por placa. Con más piezas aumentan los viajes y los hilos, y si una pieza se despega arruina todo el lote.

## En la Bambu Lab X2D (impresora del equipo)

- **Usar solo la boquilla principal (izquierda).**
  - Es de extrusión directa y tiene detección de atasco.
  - La auxiliar (derecha) se alimenta por tubo Bowden. Bambu no la recomienda para TPU.
  - La doble boquilla no aporta nada en los rodillos.
- **Alimentar el CR-TPU desde un carrete externo, no desde el AMS.** El TPU 95A blando se atora en el AMS.
  - Si tienen el AMS 2 Pro, sí sirve **solo para secar** el rollo. Después se pasa al carrete externo.
- **Perfil en Bambu Studio:** partir de "Generic TPU" (velocidad volumétrica máx. ~3.5 mm³/s) y ajustar con la tabla de arriba:
  - Calidad → posición de costura **Alineada** + **Scarf joint seam**.
  - Paredes 4 · giroide al 50–60 % · 5 capas superiores/inferiores.
  - Otros → borde **solo exterior, 5 mm**.
  - Viajes → **evitar cruzar paredes**.
  - Filamento → **Z-hop 0** (en la sobrescritura del filamento).
- **Placa:** PEI texturizada a 35–45 °C.
- **Secuencia de impresión:** por capa. "Por objeto" está limitado por el espacio libre del cabezal, y los rodillos miden 57 mm.

## Antes del lote: calibrar los ajustes

En el laminador, cortar el modelo a ~12 mm de altura e imprimir solo la punta. Con ese recorte se revisa:
1. **Que el eje de Ø6.35 entre deslizando sin juego.** El TPU suele cerrar los barrenos 0.1–0.2 mm. Si aprieta, usar la compensación de agujeros del laminador o abrir el barreno en CAD.
2. **Que el buje entre en el Ø10.75.** Con rodamientos R4A-ZZ (Ø12.7), dejar el contraalojamiento en ~Ø12.6: el TPU abraza el rodamiento por elasticidad.
3. **Que el puente del contraalojamiento quede limpio.**

## Terminado

- Quitar hilos con pistola de calor a distancia, en pasadas rápidas.
- Si queda un bordo en la costura, lijarlo ligeramente con el rodillo montado en un eje y girando.
- Medir el Ø central de varios rodillos: una diferencia > 0.3 mm entre rodillos se nota como golpeteo de la rueda.
