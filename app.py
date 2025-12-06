import os
from flask import Flask, render_template
from models import db
from routes.ingresos import ingresos_bp
from routes.salidas import salidas_bp
from routes.stock import stock_bp
from flasgger import Swagger

app = Flask(__name__)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # Muestra todas las reglas
            "model_filter": lambda tag: True,  # Muestra todos los modelos
        }
    ],
    "title": "Inventario Penitenciario API",
    "version": "1.0.0",
    "basePath": "/",
    "swagger_ui": True,
    "static_url_path": "/flasgger_static",
    "swagger_ui_bundle_path": "/flasgger_static/swagger-ui-bundle.js",
    "swagger_ui_standalone_path": "/flasgger_static/swagger-ui-standalone-preset.js"
}

Swagger(app, config=swagger_config)

# ... tus rutas van aquí

# Ruta absoluta para evitar problemas
db_path = os.path.join(os.path.dirname(__file__), "instance", "farmacia.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")

app.register_blueprint(ingresos_bp)
app.register_blueprint(salidas_bp)
app.register_blueprint(stock_bp)

if __name__ == "__main__":
    app.run(debug=True)
