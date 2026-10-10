# Rueda mecanum — memoria de cargas y Estudio 1 (estático rodillo/pin)

Fecha: 2026-09-09 (rev. B — diametro corregido a 6 in) · Autor: Rodrigo Herrera
Subsistema: AGV mecanum · Reto MR3005C.601

## 1. Datos de entrada

| Parámetro | Valor | Origen |
|---|---|---|
| Masa total AGV (incluye brazo) | 35 kg | estimada, **por confirmar** |
| Diámetro de rueda | 6 in = 152.4 mm | diseño |
| Radio | 76.2 mm | — |
| Número de rodillos | 10 | diseño |
| Largo de rodillo | 65 mm | diseño |
| Ángulo de rodillo | 45° | estándar mecanum |
| Velocidad máxima | 1 m/s | requisito |
| Material | PETG impreso (todo) | diseño |

## 2. Cargas derivadas

Peso total: $W = 35 \times 9.81 = 343.4$ N
Carga estática por rueda: $343.4/4 = 85.8$ N

**Carga de diseño en el peor rodillo** (un solo rodillo en contacto):

$$F_{rod} = \frac{(m)g}{4}\cdot K_d \cdot K_r = 85.8 \times 2.0 \times 1.33 = 228\ \text{N}$$

- $K_d = 2.0$ factor dinamico (aceleracion + bache)
- $K_r = 1.33$ reparto desigual, piso no plano

> Con la cobertura de 96% (seccion 3) el golpeteo es marginal: $K_d = 2.0$ se sostiene. Solo si se deja el rodillo en 65 mm, subir a 2.5 → $F_{rod} = 285$ N.

**Cinematica:**
- RPM a 1 m/s: $n = 125$ rpm
- Frecuencia de paso de rodillos: $f_p = 20.9$ Hz → el modal (Estudio 4) debe dar $f_1 > 63$ Hz

**Par:**
- Nominal estimado por rueda: ~1.3 N·m
- Limite por patinado ($\mu = 0.4$ PETG/concreto): $T = 0.4 \times 85.8 \times 0.0762 = 2.62$ N·m
- **Par de diseno estructural: 3.0 N·m** → $F_{trac} = 39$ N
- Fuerza lateral (45°): $F_{lat} = F_{trac} = 39$ N

> $F_{trac}$ NO depende del radio: esta limitada por friccion ($\mu N$). El radio
> solo cambia el par necesario para producirla. Por eso 228 N y 39 N no cambiaron.

Motor a especificar: gearmotor 24 V, ~180 rpm vacio, 2.5-3.5 N·m, ~100 W por rueda.

## 3. Hallazgo A — traslape marginal (mejoro al pasar a 6 in)

Paso angular con 10 rodillos: 36°
Arco cubierto por rodillo:

$$\theta = \frac{L \sin 45°}{r} = \frac{65 \times 0.707}{76.2} = 34.55°$$

34.55° < 36° → cobertura del 96%, deficit de 1.45°. Traslape negativo pero marginal.

$$L_{min} = \frac{2\pi r}{n \cos 45°} = 67.7\ \text{mm}$$

**Accion:** subir el rodillo de 65 a **70 mm** -> $\theta = 37.2°$, traslape positivo.
Ancho de rueda: 46 -> 49.5 mm. No hace falta ir a 12 rodillos.

> Con el diametro anterior de 7 in la cobertura era 82% y exigia rodillos de 79 mm.
> Reducir a 6 in resolvio casi por completo este hallazgo.

## 4. Hallazgo B — el pin no puede ser de PETG

Pin Ø6 mm, luz entre orejas 67 mm, carga al centro:

$$M = \frac{FL}{4} = 3.82\ \text{N·m} \qquad \sigma = \frac{M}{Z} = 180\ \text{MPa} \qquad \delta = 11.2\ \text{mm}$$

PETG $\sigma_y = 35$ MPa → **FS = 0.19**. Falla inmediata.

Si los rodamientos van pegados a las orejas ($a \approx 6$ mm) la carga deja de ser central:
$M = (F/2)a = 0.685$ N·m → $\sigma = 32.3$ MPa → FS = 1.08. Sigue sin margen y PETG fluye en frio.

**Accion: pin de acero Ø8 mm** (varilla calibrada o tornillo M8 clase 8.8).
Resultado: $\sigma = 76$ MPa, FS = 4.1, $\delta = 0.107$ mm.

## 5. Hallazgo C — presion de contacto al limite

Hertz cilindro-plano, $E^* = 2212$ MPa (PETG vs concreto):
$p_{max} \approx 29$ MPa vs $\sigma_y = 35$ MPa → FS = 1.19, huella 0.66 mm.

**Accion:** banda de TPU 3-4 mm shore 90-95A sobre el rodillo.
Beneficios: baja presion ~10x, sube $\mu$ de 0.4 a 0.7, amortigua el golpeteo del hallazgo A.

## 6. Material para SolidWorks (personalizado, NO el de biblioteca)

| Propiedad | Valor |
|---|---|
| Modulo elastico E | 1800 MPa |
| Coef. de Poisson | 0.40 |
| Densidad | 1270 kg/m³ |
| Limite elastico (XY) | 35 MPa |
| Limite elastico (Z, interlaminar) | **20 MPa** |
| Resistencia ultima | 45 MPa |

Si el plano de maximo esfuerzo coincide con las capas de impresion, usar 20 MPa.

## 7. Estudio 1 — procedimiento

Modelo reducido: 1 rodillo + pin + soporte + sector de hub. No mallar la rueda completa.

1. Estudio estatico nuevo, suprimir todo menos el sector
2. `Fixed Geometry` o simetria en las caras de corte del hub
3. `Split Line` en la generatriz del rodillo, franja de 6 mm (carga puntual = singularidad)
4. Fuerza **228 N** normal al piso + **39 N** axial al rodillo (componente lateral)
5. Contactos: `No Penetration` rodillo-pin · `Bonded` el resto
6. Malla curvature-based + `Mesh Control` en filetes de la oreja, min 3 elementos por filete
7. Correr con malla normal / fina / extrafina y verificar convergencia del von Mises

### Criterios de aceptacion

- Pin de acero: FS ≥ 3
- Aplastamiento en oreja: $\sigma_b = F/(d\,t) \le 35$ MPa → con Ø8, $t \ge 0.82$ mm por resistencia, **$t \ge 4$ mm por creep**
- Deflexion del rodillo < 0.5 mm
- Error de energia (ERR) < 5%

### Trampas

- Pico de von Mises que no converge al refinar = singularidad de esquina viva, no dato real. Poner filete o leer a 1-2 espesores del pico.
- No fijar el hub completo: sobrerrigidiza y subestima la deflexion.

## 8. Pendientes

- [ ] Confirmar masa real del AGV (35 kg es estimacion)
- [ ] Definir diametro del pin y posicion de rodamientos (cambia el momento por factor 5.6)
- [ ] Alargar rodillo de 65 a 70 mm (traslape positivo)
- [ ] Cotizar varilla de acero Ø8 y TPU para banda
- [ ] Estudios 2 (hub carga lateral), 3 (torsion cople), 4 (modal), 5 (fatiga)

## Supuestos usados (verificar contra el CAD real)

- Pin Ø6 mm — no confirmado por Rodrigo
- Diametro de rueda 6 in confirmado por Rodrigo 2026-09-09 (antes 7 in)
- Luz entre orejas 67 mm — estimada de largo de rodillo + holguras
- Diametro de rodillo al centro ~25 mm — para el calculo de Hertz
- $\mu$ PETG/concreto = 0.4
