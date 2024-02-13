import random
ninicio = int(input("Introduce el valor inicial: "))
nfinal = int(input("introduce el valor final: "))

numero = random.randrange(ninicio,nfinal)

respuesta = 0
contador = 0
while True:
    respuesta = int(input("Introduce un numero:")) 
    if respuesta == numero:
        print("Numero Correcto, el numero era el " , numero)
        print("Numero de intentos: " , contador)
        break
    elif respuesta < numero:
        print("El numero es mas grande")
    elif respuesta > numero:
        print("El numero es mas pequeño")
    contador += 1
    


