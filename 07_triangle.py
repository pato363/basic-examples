valor = int(input('Escribe un numero entero para darte una sorpresa:'))

for i in range(valor):
    for x in range (i+1):
        print ('*', end="")
    print()
