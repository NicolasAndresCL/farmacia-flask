from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from models import db, Cooperativa
from routes.stock import actualizar_stock  # reutilizamos tu función

cooperativas_bp = Blueprint("cooperativas", __name__, url_prefix="/cooperativas")

RESPONSABLES = {
    "fin de semana": ["Tens Nicolás", "Tens Barbara"],
    "dental": ["Dr Galvez", "Dr Aguilera"],
    "semanal": ["Tens Maka", "Tens Veronica", "Tens Syndy"],
    "especial": ["Tens Nicolás", "Tens Barbara", "Tens Maka", "Tens Veronica", "Tens Syndy"]  # puedes ajustar
}

DOCTORES = ["Dr Franco", "Dr Consuegra", "Dr Segovia", "Dr Galvez", "Dr Aguilera"]

@cooperativas_bp.route("/", methods=["GET", "POST"])
def index_cooperativas():
    if request.method == "POST":
        tipo = request.form["tipo"]
        responsable = request.form["responsable"]
        doctor = request.form["doctor"]
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Procesar hasta 3 medicamentos
        for i in range(1, 4):
            nombre = request.form.get(f"medicamento{i}")
            cantidad = request.form.get(f"cantidad{i}")
            if nombre and cantidad:
                coop = Cooperativa(
                    medicamento=nombre,
                    cantidad=int(cantidad),
                    tipo=tipo,
                    responsable=responsable,
                    doctor=doctor,
                    fecha=fecha
                )
                db.session.add(coop)
                actualizar_stock(nombre, int(cantidad), operacion="salida")

        db.session.commit()
        return redirect(url_for("cooperativas.index_cooperativas"))

    cooperativas = Cooperativa.query.all()
    return render_template("cooperativas.html", cooperativas=cooperativas,
                           responsables=RESPONSABLES, doctores=DOCTORES)
