from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interesados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Modelo de la tabla
class Interesado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Interesado {self.nombre} {self.apellido}>'


# Creación de la base de datos
with app.app_context():
    db.create_all()


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/prototipo")
def prototipo():
    return render_template("prototipo.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/interesado", methods=["GET", "POST"])
def interesado():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        correo = request.form["correo"]

        # Guardar en la base de datos
        nuevo = Interesado(nombre=nombre, apellido=apellido, correo=correo)
        db.session.add(nuevo)
        db.session.commit()

    return render_template("interesado.html")


if __name__ == "__main__":
    app.run(debug=True)
