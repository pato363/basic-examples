numero = int(input('Ingresa el numero que quieres la tabla  =>'))

if numero <= 1:

    print (f"\n### Tabla de multiplicar del numero{numero}### ")
for numero_tabla in range (1,11):
    print(f"{numero} x {numero_tabla} = {numero*numero_tabla} ")

else:
    print("Finaliza tabla")
