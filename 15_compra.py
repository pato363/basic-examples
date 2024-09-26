def descuento(precio,porcentaje):
    return precio -(precio*porcentaje/100)

def iva(precio,iva):
    return precio + precio * iva /100

def compra(dic,value):
    total=0
    for precio, descuento in dic.items():
        total += value(precio,descuento)
    return(total)

print('El precio de la compra tras aplicar los descuentos es: ', compra({1000:20, 500:10, 100:1}, descuento))
print('El precio de la compra tras aplicar el IVA es: ', compra({1000:20, 500:10, 100:1}, iva))


