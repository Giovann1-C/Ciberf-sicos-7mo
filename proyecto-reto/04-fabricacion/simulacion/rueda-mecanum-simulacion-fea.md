# Rueda mecanum V6 — simulación FEA (SolidWorks Simulation)

Fecha: 2026-10-01 · Autor: Rodrigo Herrera (montada y corrida con Claude)
Archivos: `Documents\solid\7° semestre\Mecanum_wheel\Simulacion_rueda_V6\`
- `Sim_A_actual.SLDASM`: el par entra directo por las caras del hexágono del hub.
- `Sim_B_cople_hex.SLDASM`: el par entra por un cople de acero hexagonal de 12 mm × 25 mm, con barreno de Ø8 (`cople_hex_12x25.SLDPRT`).
- Cada ensamble tiene 3 estudios estáticos: `1_Estatica_peso`, `2_Torsion_motor` y `3_Combinada`.
- Imágenes comparativas: `imagenes\comparacion_estudio_1..3.png`.

## Configuración

| Concepto | Valor |
|---|---|
| Materiales | Rodillos de **TPU 95A**: E = 26 MPa, ν = 0.45, σy = 8.6 MPa. Hub, cubiertas, brida y bujes de **PETG**: E = 1.8 GPa, ν = 0.40, σy = 35 MPa (20 MPa entre capas). Ejes y cople de **AISI 1020**: σy = 351 MPa. |
| Contacto | Unión global "bonded" con holgura de 0.35 mm, para cerrar los ajustes de 0.1–0.2 mm. |
| Sujeción | **A:** las 6 caras del hexágono del hub, como si el cople fuera rígido y de largo completo. **B:** el barreno de Ø8 del cople, es decir, la flecha del motor. |
| Carga | Carga remota en la superficie del rodillo inferior (rodillo 4), aplicada en el punto de contacto con el piso. |
| Estudio 1 | Fy = **482 N**. Es la carga de diseño: robot de 34 kg con el brazo extendido y 5 kg de pieza, × $K_d$ 2.0 × $K_r$ 1.33. |
| Estudio 2 | Par de bloqueo de **10 N·m** (100 kg·cm), transmitido como fuerza a lo largo del eje del rodillo: Fx = Fz = 134 N. |
| Estudio 3 | Las dos cargas juntas. |
| Modelo | Hub, cubiertas y brida completos, más los rodillos 3, 4 y 5. Los otros 9 rodillos no reciben carga y se suprimieron. La malla es de curvatura, con ~318 000 nodos. |
| Validación | La reacción en el estudio A1 suma Fy = −481.99 N, que coincide con la carga aplicada. |

## Resultados: von Mises en MPa

El primer valor es el percentil 99.9 de cada pieza, que filtra las singularidades de esquina. Entre paréntesis va el máximo nodal.

| Pieza | A1 peso | A2 torsión | A3 comb. | B1 peso | B2 torsión | B3 comb. | Límite |
|---|---|---|---|---|---|---|---|
| Cubierta (raíz de la oreja del rodillo 4) | 34.2 (57) | 27.4 (54) | **42.6** (69) | 35.0 (59) | 27.2 (54) | **45.1** (72) | 35 |
| Contraparte (raíz de la oreja) | 33.5 (55) | 28.1 (49) | **48.1** (81) | 34.7 (56) | 27.7 (49) | **47.6** (79) | 35 |
| Hub PETG junto al hexágono (r < 9.5) | 0.7 | 1.5 | 2.1 | 4.3 | 5.4 | **9.0** | 35 |
| Brida Part4 | 1.6 | 1.9 | 2.8 | 1.6 | 2.0 | 3.7 | 35 |
| Cople de acero | — | — | — | 10.9 | 16.6 | 27.3 | 351 |
| Eje de acero del rodillo 4 | **203** | 57 | **216** | 83 | 26 | 87 | 351 |
| Buje PETG del rodillo 4 | 10.3 | 4.0 | 11.5 | **94** | 33 | **102** | 35 |
| Rodillo TPU 4 | 0.9 | 0.4 | 1.0 | **16.1** | 5.1 | **16.8** | 8.6 |
| Desplazamiento máximo (mm) | 1.02 | 1.15 | 1.65 | 0.56 | — | 1.31 | — |

Los valores de diseño ya incluyen un factor de 2.66 sobre la carga real. **En operación normal** (181 N en la rueda más cargada), los estudios 1 y 3 hay que dividirlos entre ~2.66.

## Interpretación

1. **El cople de 25 mm concentra más el par que el caso ideal, pero va sobrado.** El PETG junto al hexágono sube de 2 MPa (caso A) a 9 MPa (caso B), con el pico en la punta del cople (z = −15 mm). Su factor de seguridad es de **3.9 a carga de diseño** y de más de 6 en operación. **El modelo B es el realista y pasa.** El cople de acero trabaja a 27 MPa, con FS de 13.
2. **El punto crítico del sistema es la raíz de la oreja de las cubiertas.** Es la esquina donde la oreja de 45° se une a la placa, del lado del rodillo. Pasa lo mismo en A y en B, porque no depende del cople.
   - **A carga de diseño:** con peso y par juntos llega a 43–48 MPa (p99.9), por encima de los 35 MPa.
   - **En operación normal:** ~17 MPa. Da FS de 2 en XY, pero solo **~1.2 entre capas**.
   - **Corrección:** redondeo de R2–R3 en esa esquina y oreja de 5 mm, o imprimir la cubierta con las capas paralelas a la oreja.
3. **El camino de carga del rodillo define si fallan los bujes.** El barreno del rodillo y el de los bujes tienen la misma holgura, 0.2 mm, y la malla los resolvió distinto en cada modelo. Eso da **los dos extremos**:
   - **A, el rodillo apoya en el eje a todo lo largo:** el eje trabaja a flexión a 203–216 MPa (FS de 1.6 a carga de diseño y de ~4.3 en operación) y los bujes casi no cargan.
   - **B, el rodillo solo apoya en las puntas:** el buje de PETG llega a ~100 MPa y el cuello de TPU a ~17 MPa. **Los dos fallan aun en operación normal** (buje ≈ 38 MPa).
   - La realidad queda entre los dos. Para no depender de eso: **cambiar los bujes por rodamientos R4A-ZZ (6.35 × 12.7 × 4.76)** o hacer el barreno del rodillo con la medida justa (Ø6.45) para que apoye en el eje.
4. **El hub y la brida tienen un margen enorme** (≤ 9 MPa cerca del hexágono). Los picos de 40–67 MPa en el borde exterior del hub son singularidades en la arista de contacto con la cubierta y desaparecen al refinar la malla.
5. **El rodillo de TPU no falla en el cuerpo** (1 MPa), pero el cuello de 1 mm de pared es débil si carga solo. Ese caso lo resuelve el mismo cambio a rodamientos.

## Iteración 2 — redondeo en la raíz de las orejas (2026-10-01)

**Causa del pico:** el anillo de Ø14 que alarga el alojamiento del eje sobresalía ~1 mm más allá de la raíz de la oreja. Eso dejaba una muesca viva entre el costado R7 del anillo, la cara de la oreja y el doblez R0.737.

**Cambio:**
- Se agregó `Fillet1` R1 en las 24 aristas de esa muesca, en las dos cubiertas: +170 mm³ cada una.
- 0 interferencias.
- En `Mecanum_wheel_V6.SLDASM` también se volvió a aplicar `Coincident6` y se guardó el ensamble.
- Respaldo previo en `Mecanum_wheel_V6_respaldo_4_antes_de_redondeo`.

**Estudio nuevo `4_Combinada_redondeo`:** mismas cargas que el estudio 3 (482 N + 10 N·m). Valores en p99.9, y entre paréntesis el máximo:

| Pieza | A antes → después | B antes → después |
|---|---|---|
| Cubierta | 42.6 → **34.1** (68.6) | 45.1 → **35.8** (59.0) |
| Contraparte | 48.1 → **38.1** (63.5) | 47.6 → **37.1** (62.2) |
| PETG del hub junto al hexágono | 2.1 → 2.1 | 9.0 → 8.9 |

- **La muesca se resolvió:** baja ~21 %. El máximo de la cubierta se movió a la esquina del fondo del alojamiento del eje (−24.6, −66, −2.9). En la contraparte, el máximo pasó a la cara exterior de la placa sobre el borde del hub (r ≈ 52 mm): la placa de 4 mm se flexiona sobre el canto del hub de R49.5.
- **Con la carga de diseño sigue en el límite** (FS ≈ 1.0 contra 35 MPa). **En operación normal** (÷2.66) queda en ~14 MPa: FS 2.5 en XY y 1.4 entre capas.
- **Siguiente mejora, si hace falta:**
  - Subir la placa de las cubiertas de 4 a 5 mm (por el lado exterior, sin tocar los rodillos).
  - Un chaflán de 0.5 mm en las puntas de los ejes, con el radio de R0.5 correspondiente en el fondo del alojamiento.
- **Nota de malla:** el modelo con redondeo tiene ~395 000 nodos contra 318 000. Parte de la mejora puede venir de una malla más fina en esa zona.

## Contacto con el piso: ¿tocan los rodillos o la cubierta? (2026-10-01)

**Método:** se calculó, para cada ángulo de giro (cada 0.25°), cuánto se alarga cada pieza hacia el piso. Se usó la teselación de los cuerpos del ensamble V6.

**Hallazgo:** ya venía del diseño original. Las puntas R7 de las orejas y el relleno de la cuña llegaban a **r = 75.76 mm**, contra **74.69 mm** de los rodillos. **La cubierta tocaba el piso antes que los rodillos**, en el peor ángulo por 1.27 mm.

**Corrección:**
- Se agregó el corte `Recorte_R72.6_piso` en las dos cubiertas: un anillo R72.6–R100 pasante. Quita 3.7 cm³ por cubierta.
- Los alojamientos del eje quedan completos, con al menos 1.54 mm de pared hacia el borde recortado. Ese es el lado que no carga, porque el piso empuja el rodillo hacia el centro.

| Pieza | Radio máximo | Alcance mínimo y máximo hacia el piso |
|---|---|---|
| Rodillos | 74.69 | 74.17 – 74.69 |
| Cubiertas (después del corte) | 72.60 | 72.43 – 72.60 |
| Bujes | 72.28 | 70.70 – 72.28 |
| Ejes | 70.95 | — |
| Hub | 49.50 | — |

- **Holgura mínima de la cubierta al piso: 1.57 mm.** Está en el hueco entre rodillos (cada 30°); en el resto del giro es de ~2.1 mm.
- El TPU se aplasta ~0.8 mm con la carga normal (Hertz con E = 26 MPa), así que **solo tocan los rodillos**. Con la carga de diseño (~1.5 mm) quedaría al ras únicamente en baches fuertes, justo en el hueco.
- **Ondulación de rodadura: 0.52 mm**, 12 veces por vuelta. Es el costo de acortar el rodillo a 57 mm. Si molesta en la odometría o hay vibración, lo que corrige es volver a un rodillo más largo, lo que implica regresar a los ejes de 79 mm.

## Cubierta paramétrica (2026-10-01)

Las dos cubiertas importadas, `cubierta_mecanum_12` y `_counterpart`, se reemplazaron en `Mecanum_wheel_V6.SLDASM` por **una sola pieza con cotas**: `cubierta_mecanum_param.SLDPRT`.

- **Por qué basta una pieza:** la contraparte es la misma pieza girada −30°. El ensamble usa dos instancias.
- **Geometría:** coincide con la anterior con una diferencia de volumen de 0.09 % (60 624 contra 60 572 mm³).
- **Verificación en el ensamble:** 0 errores, barrenos alineados con el hub, alojamientos coaxiales con los ejes (< 0.001 mm) y 1.57 mm de holgura al piso.
- **Respaldo:** `Mecanum_wheel_V6_respaldo_5_antes_de_cubierta_param`.

**Árbol de operaciones:**
1. `Placa`: el croquis plano original con sus 16 cotas, extruido `Esp_placa`.
2. `Quitar_pestanas_planas` y `Barrenos_y_ventanas`.
3. **Brazo semilla del rodillo 1:**
   - `Croquis_perfil_brazo`, completamente definido, extruido a plano medio en `Plano_rodillo_1`.
   - `Redondeo_punta`.
   - `Anillo` y `Alojamiento_eje`, que perforan una línea constructiva del eje del rodillo.
   - `Redondeo_base_anillo`.
4. `Patron_brazos` ×12 alrededor de `Eje_rueda`.
5. `Recorte_piso`.

**Variables globales** (Herramientas → Ecuaciones):

| Variable | Valor | Qué controla | ¿Se puede editar? |
|---|---|---|---|
| `Esp_placa` | 4 | Espesor de la placa y de la parte superior del brazo | Sí: subirla refuerza la flexión de la placa sobre el hub |
| `Ancho_brazo` | 15 | Ancho radial del brazo | Sí: más ancho es más fuerte; revisar el choque con el rodillo vecino |
| `S_cara_brazo` | 33.8 | Distancia del centro del rodillo a la cara de apoyo del brazo, medida sobre el eje | Con cuidado: bajarla engrosa el brazo; el anillo se ajusta solo |
| `Largo_brazo`, `Punta_brazo` | 32.007 / 7.464 | Muro y punta de la cuña | Sí |
| `D_anillo` | 14 | Diámetro del anillo que soporta el eje | Sí |
| `R_redondeo_anillo`, `R_punta` | 1 / 6 | Redondeos | Sí: subir el R de la base del anillo baja el esfuerzo |
| `D_alojamiento` | 6.55 | Ajuste del eje de 1/4 in | Solo si cambia el ajuste o la impresora |
| `R_recorte` | 72.6 | Radio máximo de la cubierta, para que no toque el piso | Mantener ≤ 72.6 |
| `R_rodillo`, `Z_rodillo`, `Angulo_brazo`, `S_tope_buje`, `Fondo_alojamiento`, `N_rodillos` | 63 / 28.96 / 45 / 29.8 / 35.8 / 12 | Geometría del rodillo y del eje | **No**: vienen del rodillo y el eje |

`Alt_anillo` y `Prof_alojamiento` se calculan solos para que el buje siempre apoye en el anillo y el eje siempre llegue al fondo.

**Pendiente:** el redondeo de la punta es un R6 vertical. El original era R7 en el plano de la oreja; la diferencia es de 0.09 % del volumen.

## Recomendaciones (por prioridad)

1. Redondeo R2–R3 en la raíz de las orejas de las dos cubiertas y, si se puede, oreja de 5 mm.
2. Rodamientos R4A-ZZ en lugar de los bujes de PETG, o barreno del rodillo a Ø6.45.
3. Usar el cople de 12 × 25 mm: queda validado.
4. Repetir los estudios con contactos explícitos ("sin penetración" entre rodillo y eje) para resolver el reparto real de carga del punto 3.

## Cómo revisarlo en SolidWorks

1. Abre `Sim_A_actual.SLDASM` o `Sim_B_cople_hex.SLDASM`. Las pestañas de estudio están abajo a la izquierda.
2. En cada estudio, abre **Resultados → Tensión1 (von Mises)** y ajusta el rango a 0–35 MPa en *Opciones de gráfico*.
3. Para ver solo una pieza, en el gráfico usa clic derecho → *Mostrar selección*. Usa **Sondeo** en la raíz de la oreja (cerca del punto x = ±19, y = −65 en relación al centro de la rueda).
