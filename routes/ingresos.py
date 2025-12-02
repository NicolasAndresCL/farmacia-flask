from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from models import db, Ingreso, Stock   # importar modelos

ingresos_bp = Blueprint("ingresos", __name__, url_prefix="/ingresos")

TIPOS = ["Tableta", "Inyectable", "Jarabe", "Broncodilatador"]

def obtener_fecha():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

@ingresos_bp.route("/")
def index_ingresos():
    ingresos = Ingreso.query.all()   # 🔥 ahora desde la base
    return render_template("ingresos.html", ingresos=ingresos, tipos=TIPOS)

@ingresos_bp.route("/agregar", methods=["POST"])
def agregar_ingreso():
    medicamento = request.form.get("medicamento")
    cantidad = int(request.form.get("cantidad"))
    tipo = request.form.get("tipo")

    ingreso = Ingreso(
        medicamento=medicamento,
        cantidad=cantidad,
        tipo=tipo,
        fecha=obtener_fecha()
    )
    db.session.add(ingreso)

    # 🔥 actualizar stock en la base
    stock_item = Stock.query.filter_by(medicamento=medicamento).first()
    if not stock_item:
        stock_item = Stock(medicamento=medicamento, cantidad=0, ultima_actualizacion=obtener_fecha())
        db.session.add(stock_item)

    stock_item.cantidad += cantidad
    stock_item.ultima_actualizacion = obtener_fecha()

    db.session.commit()   # guardar cambios en la base

    return redirect(url_for("ingresos.index_ingresos"))
