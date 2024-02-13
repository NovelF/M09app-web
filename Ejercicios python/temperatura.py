import csv

tmin = float(100)

with open('tm.csv', 'r') as file:
    dict = csv.DictReader(file)
    for i in dict:
        if i['ACRONIM'] == 'TM':
            valor = float(i['VALOR'])
            if valor < tmin:
                tmin = valor
                codigo = i['CODI_ESTACIO']

with open('estacions.csv','r') as file:
    dict = csv.DictReader(file)
    for i in dict:
        if i

print(tmin)
print (codigo)


