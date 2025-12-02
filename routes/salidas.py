from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from models import db, Salida, MedicamentoSalida, Stock   # 🔥 Importar modelos

salidas_bp = Blueprint("salidas", __name__, url_prefix="/salidas")

# --- Diccionarios/listas de referencia ---
RESPONSABLES = ["TENS Daniela", "TENS Camila", "TENS Barbara", "TENS Nicolás"]
MODULOS = [1,2,11,12,13,14,31,32,33,34,41,42,43,44,45,46,47,48,51,52,53,54,71,81,82,83,84,85,86,87,91,92,93,94,95]

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
    # 🔥 Consultar salidas desde la base
    salidas = Salida.query.all()
    return render_template(
        "salidas.html",
        salidas=salidas,
        responsables=RESPONSABLES,
        modulos=MODULOS
    )

@salidas_bp.route("/agregar", methods=["POST"])
def agregar_salida():
    # Crear objeto Salida
    salida = Salida(
        responsable=request.form.get("responsable"),
        paciente=request.form.get("paciente"),
        modulo=request.form.get("modulo"),
        fecha=obtener_fecha()
    )
    db.session.add(salida)

    # Capturar medicamentos asociados
    meds = capturar_medicamentos(request)
    for m in meds:
        med_salida = MedicamentoSalida(
            nombre=m["nombre"],
            cantidad=m["cantidad"],
            salida=salida
        )
        db.session.add(med_salida)

        # 🔥 Actualizar stock en la base
        stock_item = Stock.query.filter_by(medicamento=m["nombre"]).first()
        if not stock_item:
            stock_item = Stock(medicamento=m["nombre"], cantidad=0, ultima_actualizacion=obtener_fecha())
            db.session.add(stock_item)

        stock_item.cantidad -= m["cantidad"]
        if stock_item.cantidad < 0:
            stock_item.cantidad = 0
        stock_item.ultima_actualizacion = obtener_fecha()

    # Guardar todo en la base
    db.session.commit()

    return redirect(url_for("salidas.index_salidas"))
