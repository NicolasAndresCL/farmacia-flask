from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

salidas_bp = Blueprint("salidas", __name__, url_prefix="/salidas")

salidas = []

def obtener_fecha():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def capturar_medicamentos(request, max_meds=5):
    meds = []
    for i in range(1, max_meds + 1):
        nombre = request.form.get(f"medicamento{i}")
        cantidad = request.form.get(f"cantidad{i}")
        if nombre and cantidad:
            meds.append({"nombre": nombre, "cantidad": int(cantidad)})
    return meds

@salidas_bp.route("/")
def index_salidas():
    return render_template("salidas.html", salidas=salidas)

@salidas_bp.route("/agregar", methods=["POST"])
def agregar_salida():
    salida = {
        "meds": capturar_medicamentos(request),
        "responsable": request.form.get("responsable"),
        "paciente": request.form.get("paciente"),
        "modulo": request.form.get("modulo"),
        "fecha": obtener_fecha()
    }
    salidas.append(salida)
    return redirect(url_for("salidas.index_salidas"))
