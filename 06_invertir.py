inv = int(input('Cual es la cantidad que deseas invertir? ='))
year = int(input('Por cuantos años deseas invertir? ='))
inter = float(input('La tasa de interes es de '))

for i in range(year):
    inv *= 1 + inter / 100
    print('El capital recogido por ' +str(i+1) + ' año es $'+ str(round(inv)))

