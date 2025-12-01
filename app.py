from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# --- Datos simulados en memoria ---
ingresos = []
salidas = []
stock = {}  # Diccionario: {medicamento: {"cantidad": int, "ultima_actualizacion": str}}

# --- Constantes ---
RESPONSABLES = ["Nicolás", "Daniela", "Barbara", "Syndy", "Veronica", "Maka", "Camila"]

MODULOS = [
    "1","2","11","12","13","14",
    "31","32","33","34",
    "41","42","43","44","45","46","47","48",
    "51","52","53","54",
    "71",
    "81","82","83","84","85","87",
    "91","92","93","94","95"
]

TIPOS = ["Tableta", "Inyectable", "Jarabe"]

# --- Funciones auxiliares ---
def obtener_fecha():
    """Devuelve la fecha y hora actual en formato YYYY-MM-DD HH:MM (24 hrs)."""
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def capturar_medicamentos(request, max_meds=5):
    """Captura hasta max_meds medicamentos desde el formulario de salida."""
    meds = []
    for i in range(1, max_meds + 1):
        nombre = request.form.get(f"medicamento{i}")
        cantidad = request.form.get(f"cantidad{i}")
        if nombre and cantidad:
            meds.append({"nombre": nombre, "cantidad": int(cantidad)})
    return meds

def actualizar_stock(nombre, cantidad, operacion="ingreso"):
    """Actualiza el stock automáticamente según ingreso o salida."""
    global stock
    ahora = obtener_fecha()

    if nombre not in stock:
        stock[nombre] = {"cantidad": 0, "ultima_actualizacion": ahora}

    if operacion == "ingreso":
        stock[nombre]["cantidad"] += cantidad
    elif operacion == "salida":
        stock[nombre]["cantidad"] -= cantidad
        if stock[nombre]["cantidad"] < 0:
            stock[nombre]["cantidad"] = 0  # evitar negativos

    stock[nombre]["ultima_actualizacion"] = ahora

# --- Rutas ---
@app.route("/")
def index():
    return render_template(
        "index.html",
        ingresos=ingresos,
        salidas=salidas,
        stock=stock,
        responsables=RESPONSABLES,
        modulos=MODULOS,
        tipos=TIPOS
    )

@app.route("/agregar_ingreso", methods=["POST"])
def agregar_ingreso():
    medicamento = request.form.get("medicamento")
    cantidad = int(request.form.get("cantidad"))
    tipo = request.form.get("tipo")

    ingreso = {
        "medicamento": medicamento,
        "cantidad": cantidad,
        "tipo": tipo,
        "fecha": obtener_fecha()
    }
    ingresos.append(ingreso)

    # Actualizar stock
    actualizar_stock(medicamento, cantidad, "ingreso")

    return redirect(url_for("index"))

@app.route("/agregar_salida", methods=["POST"])
def agregar_salida():
    salida = {
        "meds": capturar_medicamentos(request),
        "responsable": request.form.get("responsable"),
        "paciente": request.form.get("paciente"),
        "modulo": request.form.get("modulo"),
        "fecha": obtener_fecha()
    }
    salidas.append(salida)

    # Actualizar stock por cada medicamento
    for m in salida["meds"]:
        actualizar_stock(m["nombre"], m["cantidad"], "salida")

    return redirect(url_for("index"))

# --- Main ---
if __name__ == "__main__":
    app.run(debug=True)
