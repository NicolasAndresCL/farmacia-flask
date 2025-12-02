from flask import Blueprint, render_template
from datetime import datetime

stock_bp = Blueprint("stock", __name__, url_prefix="/stock")

# Diccionario de stock simulado
stock = {}

@stock_bp.route("/")
def index_stock():
    return render_template("stock.html", stock=stock)

def actualizar_stock(nombre, cantidad, operacion="ingreso"):
    """Actualiza el stock automáticamente según ingreso o salida."""
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M")

    if nombre not in stock:
        stock[nombre] = {"cantidad": 0, "ultima_actualizacion": ahora}

    if operacion == "ingreso":
        stock[nombre]["cantidad"] += cantidad
    elif operacion == "salida":
        stock[nombre]["cantidad"] -= cantidad
        if stock[nombre]["cantidad"] < 0:
            stock[nombre]["cantidad"] = 0

    stock[nombre]["ultima_actualizacion"] = ahora
