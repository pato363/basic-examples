
fruta = {'platano':1.35, 'manzana':0.80, 'Pera':0.85, 'Naranja':0.70}
pedido = input('Cual fruta deseas: ')
kilo = float(input('Cuantos kilos deseas: '))

if pedido in fruta:
    total= fruta[pedido]*kilo
    print(kilo, ' de fruta cuesta ',total,'Euros')

else:
    print('No se encuentra esta fruta en la canasta')
