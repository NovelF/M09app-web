from flask import Flask, render_template
app = Flask(__name__)

@app.route("/edad100/<nombre>/<int:edad>")
def edad100(nombre,edad):
    anyo = 2024 + ( 100 - edad )
    return render_template('edad.html',nombre=nombre,anyo=anyo)

