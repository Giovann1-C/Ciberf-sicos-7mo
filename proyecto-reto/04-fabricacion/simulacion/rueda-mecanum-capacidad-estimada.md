# Rueda mecanum V6 — capacidad estimada (cálculo de ingeniería, no FEA)

Fecha: 2026-10-01 · Autor: Rodrigo Herrera (cálculo con Claude) · Material de impresión: **PETG**
Geometría medida del CAD `Mecanum_wheel_V6` (hub R49.5, 12 rodillos, eje acero Ø6.35).
Script: cálculo a mano; supuestos marcados *(sup.)*.

## 1. Masa estimada del AGV

| Concepto | kg | Base |
|---|---|---|
| Chasis PTR 3/4 in cal. 18 (1.214 mm), dos bases de 60 × 50 cm | 4.8 | 0.68 kg/m × 6.5 m (2 marcos + 1 travesaño c/u + 4 postes de 0.30 m *(sup.)*) + soldadura |
| 4 motorreductores CHP-42GP-775 | 3.0 | ~0.75 kg c/u *(sup.)* |
| 4 ruedas PETG + ejes de acero | 3.6 | 739 cm³ PETG/rueda (CAD) + 12 ejes |
| Batería LiFePO4 24 V 20 Ah | 5.5 | típico de catálogo *(sup.)* |
| Electrónica, cableado, LiDAR, driver, MCU | 2.0 | *(sup.)* |
| Placas/cubiertas de las dos bases | 3.0 | *(sup.)*, depende del material |
| Soportes de motor y tornillería | 1.0 | *(sup.)* |
| Brazo: aluminio 2.1 + balero RC70 0.4 + actuadores 3.0 + gripper 0.5 + tornillos 0.4 | 6.4 | aluminio dato de Rodrigo; resto *(sup.)* |
| **Total sin pieza** | **29.2** | |
| Con pieza de 2 kg / 5 kg | 31.2 / 34.2 | payload *(sup.)* |

La memoria de cargas usaba 35 kg: la estimación queda dentro.

## 2. Cargas por rueda

- Brazo extendido 0.75 m con la pieza, apuntando hacia una rueda; semivía 0.25 m.
- Factores de diseño: $K_d = 2.0$ (baches y aceleración) y $K_r = 1.33$ (piso no plano).
- Toda la carga la toma un solo rodillo.

| Caso | Rueda pareja | Brazo extendido (nominal) | Diseño |
|---|---|---|---|
| Pieza de 2 kg | 77 N | 130 N | 345 N |
| Pieza de 5 kg | 84 N | 181 N | 482 N |

**Vuelco.** Con 5 kg al extremo del brazo, el factor de seguridad contra vuelco es solo **1.7**. Hay que limitar el alcance o la velocidad del brazo con carga.

**Par.** El par de bloqueo del 42GP llega hasta ~10 N·m (100 kg·cm, según la relación).

## 3. Revisión por elemento

**Criterio de PETG:**
- Fluencia: 35 MPa en XY y 20 MPa entre capas.
- Creep sostenido: ~10 MPa.

| Elemento | Nominal (2 / 5 kg) | Diseño (2 / 5 kg) | Veredicto |
|---|---|---|---|
| **Alojamiento del eje en la oreja**: Ø6.35 × **2 mm** con factor 2 de borde | 10.2 / 14.3 MPa | 27 / 38 MPa | ❌ **Eslabón débil.** En estacionado está en el límite de creep (se ovaliza) y con baches fluye. |
| Mismo alojamiento con 6 mm de profundidad | 3.4 / 4.8 MPa | 9.0 / 12.6 MPa | ✅ FS ≥ 2.8 |
| Eje de acero Ø6.35, carga en los bujes (a = 6 mm) | — | 41 / 57 MPa | ✅ FS > 6 |
| Contacto Hertz rodillo PETG–concreto (fluencia a p0 ≈ 56 MPa) | 39 / 43 MPa | 54 / 60 MPa | ⚠️ OK nominal, al límite con baches. La banda de TPU lo resuelve. |
| Buje PETG sobre acero (PV a 1 m/s) | 0.32 / 0.45 MPa·m/s | — | ⚠️ Se desgasta (límite ~0.1). No se rompe. |
| Hexágono del hub 12.2 mm, par de bloqueo de 10 N·m | L = 15: 27 · L = 20: 20 · L = 30: 13 MPa | — | ⚠️ Depende del largo del hexágono del cople. Pedir L ≥ 25 mm. |
| 5 tornillos M5 en r = 35 (si el par pasa por ellos) | 57 N/perno, aplastamiento de 2.9 MPa | — | ✅ |
| Oreja de 15 × 4 mm respaldada por la cuña, hub macizo de 58 mm | — | — | ✅ Margen amplio |

## 4. Capacidad

- **Diseño actual:** soporta ~**29 kg** totales con factores de diseño, o ~**32 kg** estáticos sin creep. El robot estimado pesa 31–34 kg, así que **no alcanza**.
- **Con el alojamiento de 6 mm:** el límite pasa al contacto del rodillo, ~**36 kg** en PETG desnudo. Con la banda de TPU sube a más de 60 kg, y entonces el límite pasa a ser el hexágono por par.

## 5. Cambios recomendados (por prioridad)

1. ✅ **Alojamiento del eje de 6 mm (aplicado el 2026-10-01).** Los ejes ya estaban cortados a 71.1 mm, así que se conservaron y se acortó el rodillo:
   - **Rodillo:** 65 → **57 mm** (`D2`). El arco R108.317 queda con el mismo centro (`D4` = 3.510) y el diámetro de la rueda sigue en Ø149.38.
   - **Cubiertas:** se agregó un anillo de Ø14/Ø6.55 × 4 mm en cada oreja (`Boss-Extrude14` a `25`, en las dos cubiertas).
   - **Ensamble:** `Coincident6` se movió a la cara del anillo. Quedan 0 errores y 0 interferencias. Las holguras no cambiaron: hub 1.81, cubierta 1.30 y entre rodillos 1.29 mm.
   - **Costo:** la cobertura baja de 30.9° a 26.6° por paso de 30°. **Corrección del 2026-10-01:** primero se estimó que la rueda cabeceaba ~0.03 mm, pero medido sobre el CAD el radio de rodadura varía entre 74.17 y 74.69 mm. La rueda **sube y baja 0.52 mm**, 12 veces por vuelta.
   - Respaldo previo en `Mecanum_wheel_V6_respaldo_3_antes_de_acortar_rodillo`.
2. **Banda de TPU 95A de 2–3 mm en los rodillos.** Mejora el contacto, la tracción y el ruido.
3. **Rodamientos R4A-ZZ (6.35 × 12.7 × 4.76) en lugar de los bujes PETG.** Hay que agrandar el contraalojamiento del rodillo de Ø10.75 a Ø12.7.
4. **Cople hexagonal de 12 mm con L ≥ 25 mm,** o pasar el par por los 5 M5 con una brida de aluminio. Además, limitar la corriente del driver para que el par no pase de ~7 N·m.
5. **Software:** limitar el alcance del brazo con piezas de más de 3 kg (vuelco).

## 6. Unión atornillada cubierta–hub–cubierta (revisión del 2026-10-02)

Geometría medida en el ensamble:
- **5 tornillos M5** (barreno Ø5.3) en r = 35, a 72°.
- Además hay 5 barrenos de Ø2 en r = 20.6, que atraviesan las cubiertas y el hub.
- El tornillo pasa por la cubierta (4 mm), el hub (57.9 mm), la contraparte (4 mm) y la brida `Part4` (5 mm). El agarre es de ~71 mm.

**Cargas.** El empuje del rodillo a lo largo de su eje llega al fondo del alojamiento en r ≈ 67 mm. Su componente axial (cos 45°) tiende a despegar una cubierta del hub. Eso hace palanca sobre el borde del hub (r = 49.5): el factor de palanca es de 0.64 × F en el tornillo más cargado.

| Caso | Carga | Tornillo más cargado |
|---|---|---|
| Par de bloqueo de 10 N·m (189 N sobre el eje del rodillo) | 134 N axial | 86 N de tensión |
| Golpe lateral con μN = 0.8 × 482 N *(sup.)* | 386 N axial | 248 N de tensión |
| Par de 10 N·m como cortante | — | 57 N |
| Carga radial de diseño: 482 N repartidos en 2 cubiertas | 241 N por cubierta | se va por fricción |

**Capacidad.**
- **Precarga:** apretar a ~1.0–1.2 N·m da 1.0–1.2 kN de precarga. La fricción del apriete transmite 53 N·m y 1.5 kN de cortante, así que **los tornillos no trabajan a cortante**.
- **Separación:** el tornillo de acero (40 kN/mm) es mucho más rígido que el PETG (~8 kN/mm). Por eso solo el 17 % de la carga externa descarga la junta. Para despegar las placas harían falta ~6 kN.
- **Resistencia:** el M5 8.8 (~9 kN) no es el límite.

**El riesgo real es perder precarga por creep del PETG y por vibración, no la resistencia.**
- La rueda sube y baja 0.52 mm 12 veces por vuelta.
- Basta un creep de 0.05 mm bajo las arandelas para perder ~350 N de precarga.

**Recomendaciones:**
1. **Arandelas anchas DIN 9021** (Ø15) en ambos lados. Con la DIN 125 normal (Ø10) y 1.2 N·m, la presión bajo la arandela es de 21 MPa: el PETG se hunde. Con la Ø15 baja a 7.8 MPa, por debajo del creep (10 MPa).
2. **Apriete de 1.0–1.2 N·m.** A 2 N·m la presión es de 13 MPa, incluso con la arandela ancha.
3. **Tuerca con inserto de nylon.** Evitar fijador anaeróbico en contacto con el PETG.
4. **Reapretar** a las 24–48 h y después de las primeras pruebas.
5. **Imprimir con 100 % de relleno** o ≥ 6 perímetros alrededor de los barrenos.
6. **Pernos de Ø2** de acero o filamento en los barrenos de r = 20.6, para ubicar las piezas y como respaldo a cortante.

### 6.1 Retención axial de la rueda (decisión del 2026-10-02)

- **Se quita `Part4`.** Sus barrenos de Ø7.3 no recibían el tornillo, así que no estaba apretada y no retenía nada. Las arandelas DIN 9021 toman su lugar.
- **Hacia el motor:** la rueda se detiene sola, porque el collarín Ø20 del cople choca con la cara del hub.
  - Área de apoyo: 185 mm².
  - Con 386 N, la presión es de 2 MPa.
- **Hacia afuera:** tornillo axial en la punta del hexágono del cople, con arandela sobre la cara exterior del hub.
  - Al apretarlo, el hub queda prensado entre el collarín y la arandela, y desaparece el juego axial.
- **Condición para el tornillo axial:** el barreno de la flecha del motor en el cople tiene que ser **ciego**. Hace falta material sólido para roscar M5 × 10 en la punta del hexágono.
  - Si el barreno es pasado, una alternativa es un prisionero radial con inserto en el hub, sobre la zona del hexágono.

## Pendientes

- [ ] Pesar los componentes reales y reemplazar los *(sup.)*.
- [ ] Confirmar la relación del 42GP y el largo del hexágono del cople.
- [ ] Definir el payload real (ver `01-planeacion/preguntas-socio-formador.md`, pregunta 4).
