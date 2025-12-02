from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

ingresos_bp = Blueprint("ingresos", __name__, url_prefix="/ingresos")

ingresos = []

def obtener_fecha():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

@ingresos_bp.route("/")
def index_ingresos():
    return render_template("ingresos.html", ingresos=ingresos)

@ingresos_bp.route("/agregar", methods=["POST"])
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

    return redirect(url_for("ingresos.index_ingresos"))
