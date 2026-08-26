# -*- coding: utf-8 -*-
"""Lee el repositorio de GitHub del equipo y detecta qué tareas ya tienen evidencia.

Flujo:
  1. git pull del repo del equipo
  2. recorre los archivos y los cruza contra sistema/evidencias.json
  3. reporta qué tareas del tablero pasarían a "en curso" o "hecha"
  4. con --aplicar, actualiza el tablero local (luego hay que republicarlo)

Uso:
  python sistema/avance.py                 solo reporta, no toca nada
  python sistema/avance.py --aplicar       actualiza el tablero
  python sistema/avance.py --sin-pull      no baja del remoto (trabaja con lo local)

Marca en HECHA (2) solo lo que tiene evidencia clara. Lo dudoso lo deja en
EN CURSO (1) y lo enlista aparte para que lo revise una persona.
"""
import os, sys, re, csv, json, io, unicodedata, subprocess, datetime

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
REPO = r"C:\Users\rodri\Documents\GitHub\Ciberf-sicos-7mo"
TABLERO = os.path.join(RAIZ, "proyecto-reto", "06-documentacion", "tablero-avance.html")
MAPA = os.path.join(RAIZ, "sistema", "evidencias.json")
BITACORA = os.path.join(RAIZ, "proyecto-reto", "05-calidad", "bitacora-evidencias.md")

# Archivos que ya existían al crear el tablero: no cuentan como evidencia nueva
BASE = {
    "readme.md", ".gitignore",
    "proyecto-reto/06-documentacion/tablero-avance.html",
    "proyecto-reto/06-documentacion/diagrama-celda.html",
    "proyecto-reto/06-documentacion/readme.md",
}
IGNORAR_DIR = {".git", "node_modules", "__pycache__"}


def plano(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.lower().replace("\\", "/")


def coincide(patron, ruta):
    """Coincidencia por limite de palabra: 'slam' NO debe casar con 'slamtec',
    ni 'pid' con 'rapido'. Los separadores validos son todo lo que no sea letra
    o digito."""
    for mm in re.finditer(re.escape(patron), ruta):
        i, j = mm.start(), mm.end()
        izq = ruta[i - 1] if i > 0 else "/"
        der = ruta[j] if j < len(ruta) else "/"
        if not izq.isalnum() and not der.isalnum():
            return True
    return False


# Palabras en el nombre del archivo que indican que el trabajo esta CERRADO,
# no solo empezado. Sin una de estas, la evidencia solo mueve a "en curso".
CIERRE = ["final", "aprobado", "aprobada", "firmado", "firmada", "liberado",
          "liberada", "validado", "validada", "entregado", "entregada",
          "terminado", "terminada", "v1.0", "rev-final"]


def pull():
    if not os.path.isdir(os.path.join(REPO, ".git")):
        print("No encuentro el repositorio en %s" % REPO)
        return False
    r = subprocess.run(["git", "pull", "--ff-only"], cwd=REPO,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    salida = (r.stdout or "") + (r.stderr or "")
    print(salida.strip()[:400] or "(sin salida)")
    if r.returncode != 0:
        print("\nEl pull fallo. Si pide credenciales, corre 'git pull' a mano una vez.")
    return r.returncode == 0


def archivos_repo():
    out = []
    for r, ds, fs in os.walk(REPO):
        ds[:] = [d for d in ds if d not in IGNORAR_DIR]
        for f in fs:
            rel = os.path.relpath(os.path.join(r, f), REPO).replace("\\", "/")
            out.append(rel)
    return out


# --------------------------------------------------------------- reglas
def regla_bom_sin_pendientes(_):
    ruta = os.path.join(REPO, "proyecto-reto", "02-proveeduria", "catalogo-materiales.csv")
    if not os.path.exists(ruta):
        return None, "no hay catalogo"
    with io.open(ruta, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    faltan = [x["codigo_erp"] for x in filas if x.get("proveedor", "").strip() in ("POR DEFINIR", "")]
    if not filas:
        return None, "catalogo vacio"
    if faltan:
        return 1, "%d de %d materiales sin proveedor" % (len(faltan), len(filas))
    return 2, "los %d materiales tienen proveedor" % len(filas)


def regla_po_criticas(_):
    ruta = os.path.join(REPO, "proyecto-reto", "03-compras", "registro-po.csv")
    if not os.path.exists(ruta):
        return None, "no hay registro de PO"
    with io.open(ruta, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    n = len(filas)
    if n == 0:
        return None, "ninguna PO emitida"
    if n < 5:
        return 1, "%d de 5 PO criticas emitidas" % n
    return 2, "%d PO emitidas" % n


def regla_hoja_firmada(coincidencias):
    if not coincidencias:
        return None, "sin hojas viajeras"
    return 1, "%d hoja(s) viajera(s) en el repo, falta confirmar firmas" % len(coincidencias)


REGLAS = {
    "bom_sin_pendientes": regla_bom_sin_pendientes,
    "po_criticas": regla_po_criticas,
    "hoja_firmada": regla_hoja_firmada,
}


def main():
    aplicar = "--aplicar" in sys.argv

    if "--sin-pull" not in sys.argv:
        print("=== Bajando del repositorio del equipo ===")
        pull()
        print()

    mapa = json.load(io.open(MAPA, encoding="utf-8"))
    mapa = {k: v for k, v in mapa.items() if not k.startswith("_")}

    todos = archivos_repo()
    nuevos = [f for f in todos if plano(f) not in BASE]
    print("=== Archivos en el repositorio: %d (%d fuera de la base inicial) ===\n" % (len(todos), len(nuevos)))

    s = io.open(TABLERO, encoding="utf-8").read()
    pat = re.compile(r'(<script id="estado" type="application/json">)(.*?)(</script>)', re.S)
    m = pat.search(s)
    est = json.loads(m.group(2))
    por_id = {}
    for c in est["cols"]:
        for t in c["ts"]:
            por_id[t.get("id")] = t

    subir, revisar, sin_cambio = [], [], 0
    planos = [(f, plano(f)) for f in nuevos]

    for tid, cfg in sorted(mapa.items()):
        t = por_id.get(tid)
        if t is None:
            continue
        coincidencias = []
        for pt in cfg.get("p", []):
            p = plano(pt)
            for orig, pl in planos:
                if coincide(p, pl) and orig not in coincidencias:
                    coincidencias.append(orig)

        propuesto, motivo = None, ""
        if "regla" in cfg and cfg["regla"] in REGLAS:
            propuesto, motivo = REGLAS[cfg["regla"]](coincidencias)
        elif coincidencias:
            minimo = cfg.get("min", 1)
            cerrado = any(any(c in plano(x) for c in CIERRE) for x in coincidencias)
            lista = ", ".join(coincidencias[:3]) + (" y %d mas" % (len(coincidencias) - 3) if len(coincidencias) > 3 else "")
            if len(coincidencias) >= minimo:
                # Un archivo prueba que hubo trabajo, no que la tarea quedo cerrada.
                # Solo sube a "hecha" si el nombre lo declara terminado.
                propuesto = 2 if cerrado else 1
                motivo = lista + ("" if cerrado else "  (hay trabajo, no consta que este cerrado)")
            else:
                propuesto = 1
                motivo = "%d de %d archivos esperados: %s" % (len(coincidencias), minimo, coincidencias[0])

        if propuesto is None:
            continue
        if propuesto <= t.get("e", 0):
            sin_cambio += 1
            continue
        registro = (tid, cfg.get("n", ""), t.get("e", 0), propuesto, motivo)
        (subir if propuesto == 2 else revisar).append(registro)

    if subir:
        print("=== EVIDENCIA DE CIERRE -> hecha ===")
        for tid, n, ant, nue, mot in subir:
            print("  [%s] %s" % (tid, n))
            print("        evidencia: %s" % mot)
        print()
    if revisar:
        print("=== HAY TRABAJO -> en curso ===")
        for tid, n, ant, nue, mot in revisar:
            print("  [%s] %s" % (tid, n))
            print("        %s" % mot)
        print()
    if not subir and not revisar:
        print("Sin cambios: ninguna tarea nueva tiene evidencia en el repositorio.\n")

    if not aplicar:
        if subir or revisar:
            print("Esto fue solo un reporte. Para aplicarlo:")
            print("  python sistema/avance.py --aplicar --sin-pull")
        return 0

    for tid, n, ant, nue, mot in subir + revisar:
        por_id[tid]["e"] = nue
    est["actualizado"] = datetime.date.today().isoformat()
    nuevo = m.group(1) + "\n" + json.dumps(est, ensure_ascii=False, indent=1) + "\n" + m.group(3)
    io.open(TABLERO, "w", encoding="utf-8").write(s[:m.start()] + nuevo + s[m.end():])
    print("Tablero actualizado: %d tareas cambiaron de estado." % (len(subir) + len(revisar)))

    os.makedirs(os.path.dirname(BITACORA), exist_ok=True)
    existe = os.path.exists(BITACORA)
    with io.open(BITACORA, "a", encoding="utf-8") as f:
        if not existe:
            f.write("# Bitacora de evidencias\n\n")
            f.write("Registro automatico de que archivo del repositorio movio que tarea.\n")
            f.write("Generado por `sistema/avance.py`.\n\n")
        f.write("\n## %s\n\n" % datetime.date.today().isoformat())
        f.write("| Tarea | ID | Estado | Evidencia |\n|---|---|---|---|\n")
        for tid, n, ant, nue, mot in subir + revisar:
            f.write("| %s | `%s` | %s | %s |\n" % (n, tid, "hecha" if nue == 2 else "en curso", mot))
    print("Bitacora: %s" % os.path.relpath(BITACORA, RAIZ))
    print("\nFalta republicar el tablero para que el equipo lo vea.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
