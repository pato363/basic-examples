def factory(num):
    num = int(input('Escribe un numero entero:'))
    factorial = 1
    if num != 0:
        for i in range(1,num + 1):
            factorial = factorial*i
        print('El resultado de factorial es:',factorial)
    else:
        print('Escribe un numero mayor que 0')

print(factory(1))
