from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# --- Modelo Ingreso ---
class Ingreso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicamento = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)

# --- Modelo Salida ---
class Salida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    responsable = db.Column(db.String(50), nullable=False)
    paciente = db.Column(db.String(100), nullable=False)
    modulo = db.Column(db.String(10), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)

    # Relación uno a muchos con MedicamentoSalida
    medicamentos = db.relationship("MedicamentoSalida", backref="salida", cascade="all, delete-orphan")

# --- Modelo MedicamentoSalida (detalle por salida) ---
class MedicamentoSalida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    salida_id = db.Column(db.Integer, db.ForeignKey("salida.id"), nullable=False)

# --- Modelo Stock ---
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicamento = db.Column(db.String(100), unique=True, nullable=False)
    cantidad = db.Column(db.Integer, default=0)
    ultima_actualizacion = db.Column(db.String(20))
    
class Cooperativa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicamento = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # fin de semana, dental, semanal, especial
    responsable = db.Column(db.String(100), nullable=False)
    doctor = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
