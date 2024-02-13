lista =[1964,1972,1995,1981,2000,2001,2002,2003,2004]
lista2 = []

for i in lista:
    edad = 2023 - i
    lista2.append(edad)

lista2.sort()
print(lista2)