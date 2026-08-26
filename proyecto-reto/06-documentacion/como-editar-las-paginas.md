# Cómo editar las páginas publicadas

Las dos páginas del equipo son **archivos HTML normales** que viven en este repo.
Se editan como cualquier archivo y luego se republican al **mismo link**, así que
el equipo nunca tiene que volver a guardar una URL.

| Página | Archivo | Link publicado |
|---|---|---|
| Tablero de avance | `06-documentacion/tablero-avance.html` | https://claude.ai/code/artifact/60424a47-dd4a-4886-b8c6-f7c64939065b |
| Diagramas | `06-documentacion/diagrama-celda.html` | https://claude.ai/code/artifact/a16da71d-e2ac-409e-bad1-41566dfaaa90 |

---

## ⚠️ La trampa del tablero: código y estado viven en lugares distintos

El tablero **se modifica a sí mismo**. Cuando alguien marca una tarea, la página
se republica sola con el estado nuevo.

| Qué | Dónde manda | Cómo se cambia |
|---|---|---|
| **Código** — estructura, colores, textos, lógica | El archivo local | Editándolo aquí |
| **Estado** — qué tarea está marcada, quién es responsable | La **versión publicada** | Haciendo clic en la página |

**Si editas el archivo local y republicas sin más, borras los clics que el equipo
hizo mientras tanto.**

Por eso el procedimiento correcto es: editar el archivo → pedirle a Claude que
republique → **Claude baja el estado vivo, lo fusiona con tu código nuevo y
publica**. Ese paso de fusión no se puede saltar.

En la práctica: **edita y dile a Claude "republica el tablero"**. Él se encarga.

El diagrama de arquitectura no tiene este problema: no guarda estado, así que se
republica directo.

---

## Anatomía del tablero

El archivo tiene tres bloques y conviene saber cuál tocar:

```html
<style id="css">      ← apariencia: colores, tipografía, espaciados
<script id="estado">  ← DATOS: tareas, hitos, equipo, quién es responsable
<script id="app">     ← lógica: cómo se dibuja y qué pasa al hacer clic
```

### Cambiar los nombres del equipo
En `<script id="estado">`, la lista `equipo`. El primer valor (`—`) significa
«sin asignar», déjalo:

```json
"equipo": ["—", "Rodrigo", "Giovanni", "Osmar", "Int. 4"]
```

Cambia `"Int. 4"` por el nombre real y listo.

### Agregar una tarea
Dentro de la columna que le toque, en `ts`:

```json
{ "n": "Diseñar el arnés de potencia", "e": 0, "r": 0, "id": "1.2.18" }
```

- `n` — el nombre que se ve
- `e` — estado: `0` por hacer · `1` en curso · `2` hecha
- `r` — índice del responsable en la lista `equipo` (`0` = sin asignar)
- `c` — ponle `1` si es crítica para el calendario (le pinta el punto rojo)
- `id` — **debe ser único**: `<wbs>.<número>`. Es lo que conecta la tarea con el
  mapa de evidencias

**Si agregas una tarea, agrégale también su patrón** en `sistema/evidencias.json`
bajo ese mismo `id`, o nunca se marcará sola.

### Cambiar colores
En `<style id="css">`, las variables de `:root`. Están duplicadas para tema claro
y oscuro: **si cambias una, cambia su pareja** o la página se rompe en un tema.

```css
--accent:#D8491A;   /* naranja de seguridad */
--ok:#2C7A4E;       /* verde de tarea hecha */
--warn:#A8721A;     /* ámbar de en curso */
```

### Tocar `<script id="app">`
Es la lógica. Si te equivocas aquí, **la página deja de funcionar para todo el
equipo**: no renderiza nada. Pídele a Claude que valide la sintaxis antes de
republicar.

---

## Anatomía del diagrama

Es HTML plano, sin lógica. Cada hoja es una `<section>` con su código:

```html
<div class="sheet"><span class="code">SH-04</span><h2>Ciclo de operación</h2></div>
```

Los diagramas son **SVG escritos a mano**, sin librerías. Se editan cambiando
coordenadas y textos directamente. Si vas a mover cosas, cambia el `viewBox` en
la misma proporción para que no se deforme.

---

## El procedimiento, en corto

1. Edita el archivo en `06-documentacion/`
2. Dile a Claude: **«republica el tablero»** o **«republica el diagrama»**
3. Claude fusiona el estado vivo, valida y publica al mismo link
4. `python sistema/sincronizar-github.py` y `git push` para versionarlo

## Si algo se rompe

Cada publicación queda como una versión. Dile a Claude que te regrese a la
anterior. Por eso también conviene que el archivo esté siempre en GitHub: es la
copia de seguridad real.

## Ojo con la versión compartida

Compartir el link **fija** la versión de ese momento. Si republicas y el equipo
sigue viendo lo viejo, entra al menú de compartir de la página y actualiza la
versión compartida.
