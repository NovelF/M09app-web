from flask import Flask
app = Flask(__name__)

@app.route("/numero/<int:num>")
def show_post(num):
    if num % 2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"