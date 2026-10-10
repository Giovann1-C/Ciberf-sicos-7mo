# Banco de pruebas de tolerancias — rueda mecanum

Fecha: 2026-10-06 · CAD en `Mecanum_wheel\Banco_tolerancias\` (`.SLDPRT` + `.STL`)

## 1. Holguras aplicadas al CAD (V6)

| Ajuste | Pieza real | Antes | Ahora | Holgura | Dónde se cambia |
|---|---|---|---|---|---|
| Hexágono del hub ↔ flecha hex 1/2 in (12.7 entre caras) | Hub | 12.75 | **13.0** entre caras | +0.30 | `D5@Sketch1` del hub (pieza virtual) |
| Barrenos M5 de paso | Hub y cubiertas | 5.3 | **5.5** | +0.5 sobre 5.0 | Hub: `D3@Sketch1` · cubiertas: variable `D_barreno_M5` |
| Centro de la cubierta ↔ cuello del hub Ø25.4 | Cubiertas | 25.4 (sin holgura) | **25.8** | +0.4 | Variable `D_centro_hub` |
| Alojamiento del eje 1/4 in (6.35) en la cubierta, fijo | Cubiertas | 6.55 | 6.55 (sin cambio) | +0.2 | Variable `D_alojamiento` |
| Buje PETG gira sobre el eje 1/4 in | `bearing_mecanum` | 6.75 | sin cambio | +0.4 | — |
| Buje Ø10.35 en el rodillo TPU | `rodilla_mecanum` | 10.75 | sin cambio | +0.4 | Definir con el cupón TPU |

- Los cambios están en `cubierta_mecanum`, `cubierta_mecanum_counter` y en el hub dentro de `Mecanum_wheel_V6.SLDASM`.
- El ensamble reconstruye con 0 errores.
- Respaldo previo: `_archivo\V6_respaldo_8_antes_de_tolerancias.zip`.
- **Pendiente:** el rodillo y el buje no se modificaron, porque los rodillos ya se estaban imprimiendo. Ajustarlos con el resultado del cupón TPU.

## 2. Banco PETG (`banco_tolerancias_PETG`)

**Pieza:**
- Placa de 112 × 122 × 5 mm.
- Cuña a 45° con 6 alojamientos de 6 mm de profundidad. Copian la inclinación de los brazos de la cubierta.
- Tapón suelto Ø25.4 × 10, que es el cuello del hub impreso.
- ~80 cm³, unos 100 g de PETG.

**Cómo imprimirlo:** igual que las piezas reales. Mismo material, boquilla, perfil y orientación: placa sobre la cama, como el hub y las cubiertas.

**Cómo leerlo:** los **puntos grabados** debajo de cada agujero dan su posición en la fila: 1 punto es la primera medida, 2 puntos la segunda, etc.

| Fila (de abajo hacia arriba, mirando la placa por arriba) | Qué se prueba | Medidas (1 → n puntos) |
|---|---|---|
| Hexágonos | Flecha hex 1/2 in | 12.8 · 12.9 · **13.0** · 13.1 · 13.2 entre caras |
| Agujeros grandes | Tapón Ø25.4 impreso (cuello del hub) | 25.6 · **25.8** · 26.0 |
| Fila de 5 chicos (arriba de los grandes) | Tornillo M5 de paso | 5.3 · 5.4 · **5.5** · 5.6 · 5.7 |
| Fila de 5 medianos | Eje 1/4 in que **gira** (buje) | 6.45 · 6.55 · 6.65 · **6.75** · 6.85 |
| Fila de 3 | Machuelo M5 (rosca en plástico) | 4.0 · 4.2 · 4.4 |
| Cuña 45° (arriba) | Eje 1/4 in **fijo** en la cubierta | 6.40 · 6.45 · 6.50 · **6.55** · 6.60 · 6.65 |

En **negritas**, el valor que tiene hoy el CAD.

**Criterio para elegir:**
- **Hexágono:** entra la flecha sin forzar y no tiene juego al girar. Si varios cumplen, el más chico.
- **Centro del hub:** el tapón entra con la mano.
- **M5 de paso:** el tornillo pasa libre.
- **Machuelo:** se puede roscar a mano con machuelo sin que se raje.
- **Eje que gira:** gira libre sin cabeceo.
- **Eje fijo (cuña):** entra a presión con la mano o con golpe suave, y no se cae solo.

## 3. Cupón TPU (`banco_tolerancias_TPU`)

**Pieza:** bloque de 84 × 30 × 10 mm. Tiene 5 contraalojamientos de 3.4 mm de profundidad y barreno pasado de Ø6.75 en todos.

**Cómo imprimirlo:** en CR-TPU, con el mismo perfil que los rodillos.

**Medidas del contraalojamiento (1 → 5 puntos):** 10.25 · 10.35 · 10.45 · 10.55 · **10.75**

**Criterio:**
- Si el buje debe quedar fijo en el rodillo (gira sobre el eje): el más chico donde entra a presión con la mano.
- Si el rodillo gira sobre el buje: el más chico donde gira libre.

## 4. Después de probar

Se cambia el valor en la variable correspondiente de las **Ecuaciones** de cada cubierta (`D_barreno_M5`, `D_centro_hub`, `D_alojamiento`) o en la cota del hub, y se reconstruye.
