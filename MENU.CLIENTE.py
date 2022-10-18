import pandas as pd
import numpy as np

listaclientes= list()
listadni=[]
listanombre=[]
listadireccion=[]
listasaldo=[]
class Clientes:
    def __init__(self):
        self.dni=( )
        self.nombre=(' ')
        self.direccion=( )
        self.saldo=(' ')


def menu():
    seleccion=0
    while seleccion != 4:
        print("------------------------------------------------------")
        print('Bienvenido a la gestion de clientes del quality ISAD')
        print("------------------------------------------------------")
        print('Elija una de las opciones del menu: ')
        print(" 1. Registrar cliente")
        print(" 2. Mostrar clientes registrados")
        print(" 3. Buscar un cliente")
        print(" 4. Salir del sistema")
        seleccion=int(input('Elija una opcion: '))
        if seleccion == 1:
            registrar()
        if seleccion == 2:
            mostrar()
        if seleccion == 3:
            buscar()
        if seleccion == 4:
            salir()


def registrar():
    print('')
    print(' Usted eligio la opcion para registrar clientes')
    print('')
    cant=int(input('Cuantos clientes desea ingresar: '))
    while cant != 0:
        cant=cant-1
        cliente=Clientes()
        cliente.dni=input('introduzca el DNI del cliente: ')
        listadni.append(cliente.dni)
        cliente.nombre=input('ingrese el nombre del cliente: ')
        listanombre.append(cliente.nombre)
        cliente.direccion=input('ingrese la direccion del cliente: ')
        listadireccion.append(cliente.direccion)
        cliente.saldo=input('ingrese el saldo deudor del cliente: ')
        print('')
        listasaldo.append(cliente.saldo)
        listaclientes.append(cliente)


def mostrar():
    print('')
    print(' Usted selecciono la opcion para mostrar los clientes')
    print('')
    data={'dni':listadni,
    'Nombre':listanombre,
    'direccion':listadireccion,
    'saldo':listasaldo}

    dataframe1= pd.DataFrame(data)
    print(dataframe1)

        

def buscar():
    print('')
    print(' Usted eligio la opcion para buscar un cliente')
    print('')
    busqueda=input('Ingrese el DNI o nombre del cliente desea buscar: ')
    for cliente in listaclientes:
        if cliente.dni == busqueda or cliente.nombre == busqueda:
            print("el cliente que busca: ")
            print('DNI del cliente' ,cliente.dni ,'Nombre' ,cliente.nombre ,'Direccion' , cliente.direccion ,'Saldo' , cliente.saldo)


def salir():
    print('')
    print(' Usted selecciono la opcion para salir del sistema')
    print(' Gracias por elegir nuestro sistema, Que tenga buen dia!')
    print('')


menu()

