from flask import Flask, render_template
from models import db
from routes.ingresos import ingresos_bp
from routes.salidas import salidas_bp
from routes.stock import stock_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmacia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# Registrar blueprints
@app.route("/")
def home():
    return render_template("home.html")

app.register_blueprint(ingresos_bp)
app.register_blueprint(salidas_bp)
app.register_blueprint(stock_bp)

if __name__ == "__main__":
    app.run(debug=True)
