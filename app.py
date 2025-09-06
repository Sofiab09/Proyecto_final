from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/prototipo")
def prototipo():
    return render_template("prototipo.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/interesado")
def interesado():
    return render_template("interesado.html")


if __name__ == "__main__":
    app.run(debug=True)
