import random
def funcion():
    try:
        op=0
        while op != 2:
            opciones = ['piedra', 'papel', 'tijera']
            print('-' * 30)
            print('Piedra, papel o tijera'.center(30))
            print('-' * 30)
            print('1. Piedra'.center(30))
            print('2. Papel'.center(30))
            print('3. Tijera'.center(30))
            humano = int(input('\nIngrese una opción: '))
            pc = random.randint(1,3)
            resultado = 'Vos elegiste ' + opciones[humano - 1] + '.\n'
            resultado += 'La computadora eligió ' + opciones[pc - 1] + '.\n'

            print((humano - pc) % 3)
            if (humano - pc) % 3 == 0:
                resultado += 'Empate'
            elif (humano - pc) % 3 == 1:
                resultado += 'Ganaste'
            else:
                resultado += 'Perdiste.'

            print(resultado)
            try:
                op=int(input("Si desea seguir jugando ingrese cualquier numero, si desea terminar de jugar ingrese 2 "))
            except ValueError:
                print("TE PEDI UN NUMERO NO UNA PALABRA!!")
                break
    except IndexError:
        print("OPS! Ese no es un numero valido ingresa otro maestro!")
    except ValueError:
        print("Un numero NO UNA PALABRA!!!")

