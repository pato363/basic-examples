ing_veg = ('pimiento','tofu')
ing_carn = ('peperoni', 'jamon','Salmon')


menu = input ('Deseas pizza vegetariana:')
if menu == 'si':
    solicita = input ('Elige cual ingrediente deseas:')
    print('La pizza elegida es Vegetariana y contiene los ingredientes Tomate, Mozarella y',solicita)

else:
    solicita_2= input ('Elige cual ingrediente deseas:')
    print ('La pizza elegida No es Vegetariana y contiene los ingredientes Tomate, Mozarella y', solicita_2)