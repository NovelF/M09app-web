import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="",
  database="correos"
)

def buscar_mail():
  nombre = input("Introduce el nombre del usuario: ") 

  mycursor = mydb.cursor()  

  sql = "SELECT correo FROM correos WHERE nombre = %s"
  mycursor.execute(sql,(nombre,))

  myresult = mycursor.fetchall()

  if not myresult:
    print("El usuario no existe")
  else:
   for x in myresult:
    print(x)

  mycursor.close()
  
def nuevo_usuario():
  mycursor = mydb.cursor()
  nombre = input("Introduce el nombre del usuario: ")
  
  mycursor.execute("SELECT correo FROM correos WHERE nombre = %s",(nombre))
  verificacion=mycursor.fetchall()

  if verificacion:
    print("Este usuario ya existe")
  else:
    correo=input("Introduce el correo del usuario: ")
    mycursor.execute("INSERT INTO correos (nombre, correo) VALUES (%s, %s)",(nombre,correo))
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def menu():
  while True:
    print("1. Buscar Mail")
    print("2. Nuevo usuario")
    print("3. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == '1':
        buscar_mail()
        print("")
    elif opcion == '2':
        nuevo_usuario()
        print("")
    elif opcion == '3':
        print("Fin del Programa")
        break
    else:
        print("Opcion no válida. selecciona una opcion valida.")

menu()