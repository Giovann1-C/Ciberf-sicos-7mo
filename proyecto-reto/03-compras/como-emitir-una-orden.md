# Cómo emitir una orden de compra, paso a paso

Todos los comandos se corren desde `C:\Users\rodri\Claude enviromental`.

> **La regla que evalúa el profesor:** ninguna compra sin orden registrada.
> Si algo se compró y no tiene PO, para efectos del Reto no existe.

---

## Paso 0 — Mira qué tienes

```bash
python sistema/erp.py estado
```

Te dice tres cosas:

- **Catálogo de materiales** — qué hay y cuánto suma
- **Riesgo de entrega** — qué tarda 5+ semanas y cuándo llegaría si pides hoy
- **Sin proveedor** — los que **bloquean las compras**: sin proveedor y sin costo real no se puede emitir nada

Ese último bloque es tu lista de pendientes de cotización.

---

## Paso 1 — ¿El producto ya está en el catálogo?

Cada material tiene un **código ERP** con la forma `PREFIJO-TIPO-PARTE`,
por ejemplo `INS-LID-2D-360`. Ese código es el que usas para todo lo demás.

| Prefijo | Categoría |
|---|---|
| `POT` | POTENCIA |
| `INS` | INSTRUMENTACION |
| `MEC` | MECANICA |
| `INT` | INTERFACES |
| `REF` | REFACCIONES |
| `OTR` | OTRO |

**Si ya existe** → salta al Paso 2.

**Si no existe**, dalo de alta. El código se genera solo:

```bash
python sistema/erp.py material --categoria MECANICA --tipo Rueda --parte MEC-100 --desc "Rueda mecanum 100 mm" --marca Nexus --costo 1800 --lead 3 --sub AGV
```

| Bandera | Qué es |
|---|---|
| `--categoria` | Una de las seis de la tabla de arriba |
| `--tipo` | Rueda, Motor, Sensor, Fuente… (forma parte del código) |
| `--parte` | Número de parte del fabricante |
| `--desc` | Descripción completa (aparece en la orden de compra) |
| `--marca` | Fabricante |
| `--costo` | Precio unitario en MXN |
| `--lead` | Semanas de entrega |
| `--sub` | Subsistema: AGV, Brazo, Cobot, Vision, Celda |

Además de darlo de alta, te crea su **carpeta de proveeduría** en
`02-proveeduria/fichas/<CÓDIGO>/` para que guardes ahí la ficha técnica y las
cotizaciones.

---

## Paso 2 — Actualiza con la cotización real

El catálogo trae precios estimados. Cuando te llegue la cotización de verdad,
métela:

```bash
python sistema/erp.py actualizar --codigo MEC-RUE-MECANUM-100 --proveedor "Nexus Robot MX" --costo 1750 --lead 3 --estado cotizado
```

Te muestra qué cambió:

```
Actualizado MEC-RUE-MECANUM-100
   proveedor: POR DEFINIR -> Nexus Robot MX
   costo_unitario: 1800 -> 1750
   estado: por cotizar -> cotizado

Ya tiene proveedor y costo: se puede emitir su orden de compra.
```

**Este paso no es opcional.** Si emites la orden con el precio estimado, el total
sale mal y la trazabilidad queda inservible.

---

## Paso 3 — Emite la orden con todos sus productos

Aquí es donde metes los productos. Van en `--items`, separados por comas, con el
formato `CÓDIGO:CANTIDAD`:

```bash
python sistema/erp.py po --proveedor "Nexus Robot MX" --contacto "Ing. Ventas" --email "ventas@ejemplo.mx" --items "MEC-RUE-MECANUM-100:4,MEC-MOT-CHP42GP775:4,INS-IMU-9DOF:1"
```

Eso mete **tres productos** en una sola orden: 4 ruedas, 4 motorreductores y 1 IMU.

**Una orden por proveedor.** Si compras a tres proveedores distintos, son tres
órdenes. No mezcles.

Banderas opcionales:

| Bandera | Para qué | Por defecto |
|---|---|---|
| `--contacto` | A quién va dirigida | vacío |
| `--email` | Correo o teléfono del proveedor | vacío |
| `--direccion` | Dirección del proveedor | vacío |
| `--terminos` | Condiciones de pago | `30 dias netos` |
| `--notas` | Nota que aparece en la orden | proyecto académico |

### Qué obtienes

```
PO generada: proyecto-reto\03-compras\ordenes\OC-2026-002_Nexus-Robot-MX.xlsx
Total: $11650.00 MXN   Lead time: 3 semanas
Registrada en proyecto-reto\03-compras\registro-po.csv
```

1. Un **Excel** con el formato exacto de la plantilla del profe: datos del
   proveedor, tabla de productos con cantidad, precio unitario e importe, total,
   lead time más largo y las líneas de firma.
2. Una **fila en el registro** con número, fecha, total y **la fecha estimada de
   llegada**, calculada con el lead time más largo de la orden.

El número (`OC-2026-002`) se asigna solo, en secuencia. No lo inventes tú.

---

## Paso 4 — Cuando llegue el material

```bash
python sistema/erp.py recibir --orden OC-2026-002 --items "MEC-RUE-MECANUM-100:4,MEC-MOT-CHP42GP775:4"
```

Marca la orden como recibida y **sube el stock** de cada material. Si llegó
incompleto, usa `--estado "en transito"` y registra solo lo que sí llegó.

Estados posibles: `emitida` · `en transito` · `recibida` · `cancelada`.

---

## Preguntas que te van a salir

### ¿Puedo agregar un producto a una orden ya emitida?
**No, y es a propósito.** Una orden emitida es un documento que ya salió al
proveedor: modificarla rompe la trazabilidad. Si te faltó algo, emite otra orden
al mismo proveedor. Si te equivocaste, márcala `cancelada` y emite la corregida.

### ¿Y si necesito cambiar el precio de un producto que ya está en una orden?
Actualiza el material con `actualizar` y **emite la orden de nuevo**. La vieja se
cancela. El Excel viejo se queda en la carpeta como historial — no lo borres.

### ¿Cómo sé qué me falta cotizar?
`python sistema/erp.py estado` te lo dice al final, en el bloque
**SIN PROVEEDOR**. Esos son los que bloquean todo.

### ¿Dónde guardo la cotización que me mandó el proveedor?
En `02-proveeduria/fichas/<CÓDIGO>/`, junto a la ficha técnica. Cada material
tiene su carpeta con una tabla de cotizaciones para comparar proveedores.

### ¿Y si el material no es de ninguna categoría?
Usa `--categoria OTRO`. Vale más tenerlo registrado con la categoría imperfecta
que tenerlo fuera del sistema.

---

## Ejemplo completo: comprar las ruedas mecanum

```bash
# 1. ¿Existe? Sí: MEC-RUE-MECANUM-100
python sistema/erp.py estado

# 2. Llegó la cotización de Nexus: $1,750 c/u, 3 semanas
python sistema/erp.py actualizar --codigo MEC-RUE-MECANUM-100 --proveedor "Nexus Robot MX" --costo 1750 --lead 3 --estado cotizado

# 3. Emitir la orden por las 4 ruedas
python sistema/erp.py po --proveedor "Nexus Robot MX" --contacto "Ing. Ventas" --email "ventas@nexus.mx" --items "MEC-RUE-MECANUM-100:4"

# 4. Tres semanas después, llegaron
python sistema/erp.py recibir --orden OC-2026-002 --items "MEC-RUE-MECANUM-100:4"

# 5. Subir todo al repositorio
python sistema/sincronizar-github.py
```

Y luego `git push` desde la copia de trabajo.

---

## Si prefieres no escribir comandos

Dile a Claude en lenguaje natural:

> *«Cotizaron las ruedas mecanum en 1,750 con Nexus, 3 semanas. Emite la orden por 4.»*

Él corre los pasos 2 y 3 y te dice qué generó.
