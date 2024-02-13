from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

dict = {
    "Mercedes": "mcast386@xtec.cat",
    "Rayane": "rayane@rayane.sa",
    "Mohamed": "moha@gmail.com",
    "Jad": "jad@gmail.com",
    "Oriol": "joam@gmail.com",
    "Elias": "hola123@gmail.com",
    "Armau": "arnau@gmail.com",
    "Asdrubal": "asdrubal@gmail.com",
}

mydb = mysql.connector.connect(
    host="192.168.127.54",
    user="novel",
    password="1234",
    database="webdb"
)

db = mydb.cursor()

@app.route('/dashboard/<name>')
def dashboard(name):
    mail = dict.get(name)
    if mail:
        return 'Hola , %s! Tu correo es %s' % (name, mail)
    else:
        return 'Usuario desconocido'


@app.route('/getmail', methods=['POST', 'GET'])
def getmail():
    if request.method == 'POST':
        name = request.form['name']
        user = db.execute("select * FROM data where Nombre = %s", (name,))
        return redirect(url_for('dashboard', name=user))
    else:
        user = request.args.get('name')
        return render_template('getmail.html')


@app.route('/addmail', methods=['POST', 'GET'])
def adduser():
    if request.method == 'POST':
        user = request.form['name']
        mail = request.form['mail']
        db.execute("INSERT INTO data (Nombre,Correo) VALUES (%s,%s)", (user, mail))
        mydb.commit()
        return render_template('infoadduser.html')
    else:
        return render_template('adduser.html')


if __name__ == '__main__':
    app.run(debug=True)
