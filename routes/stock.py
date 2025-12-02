from flask import Blueprint, render_template
from datetime import datetime
from models import db, Stock   # 🔥 Importar modelo desde models.py

stock_bp = Blueprint("stock", __name__, url_prefix="/stock")

@stock_bp.route("/")
def index_stock():
    # 🔥 Consultar todos los registros de stock en la base
    stock_items = Stock.query.all()
    return render_template("stock.html", stock=stock_items)

def actualizar_stock(nombre, cantidad, operacion="ingreso"):
    """Actualiza el stock en la base de datos según ingreso o salida."""
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Buscar si el medicamento ya existe en stock
    stock_item = Stock.query.filter_by(medicamento=nombre).first()

    if not stock_item:
        # Si no existe, lo creamos con cantidad inicial 0
        stock_item = Stock(medicamento=nombre, cantidad=0, ultima_actualizacion=ahora)
        db.session.add(stock_item)

    # Actualizar cantidad según operación
    if operacion == "ingreso":
        stock_item.cantidad += cantidad
    elif operacion == "salida":
        stock_item.cantidad -= cantidad
        if stock_item.cantidad < 0:
            stock_item.cantidad = 0

    # Actualizar fecha
    stock_item.ultima_actualizacion = ahora

    # Guardar cambios en la base
    db.session.commit()
