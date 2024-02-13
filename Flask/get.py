from flask import Flask
from flask import render_template
from flask import request


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

@app.route('/dashboard/<name>')
def dashboard(name):
   mail = dict.get(name)
   if mail:
        return 'Hola , %s! Tu correo es %s' % (name, mail)
   else:
        return 'Usuario desconocido' 

@app.route('/getmail',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      return render_template('login.html')

@app.route('/addmail',methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
       user = request.form['name']
       mail = request.form['mail']
       dict.update({user:mail})
       return render_template('infoadduser.html')
    else:
        return render_template('adduser.html')
        
if __name__ == '__main__':
   app.run(debug = True)