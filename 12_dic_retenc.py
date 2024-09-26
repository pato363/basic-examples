clientes = {}
opcion = ''
opcion = input('Menu de opciones \n(1)Añadir cliente \n(2)Eliminar cliente \n(3)Consultarcliente \n(4)Listar todos los clientes \n(5)Listar clientes preferentes \n(6)Finalizar \n Elige una opcion: ')
#while opcion != '6':
if opcion == '1':
    nif = input('Escribe el Nif del cliente: ')
    name = input ('Escribe nombre del cliente:')
    tel = input ('Escribe numero telefonico:')
    email = input ('Escribe el email: ')
    preferente = input ('Eres cliente preferente Si/No: ')
    cliente = {'Nombre':name, 'Tel':tel, 'email':email, 'preferente':preferente=='Si'}
    clientes[nif] = cliente    

if opcion == '2':
    nif = input('Ingresa Nif de cliente que deseas eliminar:')
    if nif in clientes:
        del clientes[nif]
        print('El cliente',nif,'quedo eliminado')

    else:
           print('El cliente con este Nif', nif ,'no se encuentra')
                 
if opcion == '3':
        nif = input('Escribe el NIF del cliente que deseas consultar:')
        if nif in clientes:
                print('Nif',nif)
                for clave, valor in clientes[nif].items():
                        print(clave.title() + ':',valor)
        else:
                print('No se encuentra el cliente con el nif ',nif)

if opcion == '4':
        print(clientes)

if opcion == '5':
        print (clientes[preferente])

if opcion == '6':
        print('Adios')













