
#PIEDRA PAPEL O TIJERA
#JUGADORES DOS: USUARIO Y COMPUTADORA
import random


def jugar():
    usuario = input("Elige una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return '¡Empate!'
    
    if ganó_el_jugador(usuario, computadora):
        return '¡Ganaste!'

    return '¡Perdiste!'


def ganó_el_jugador(jugador, oponente):
    #Retorna el valor True si gana el jugador
    # Si el jugador selecciona Piedra gana a Tijera ( pi>ti)
    # si el jugador selecciona Tijera gana a Papel ( ti> pa)
    # si el jugador selecciona Papel le gana a la Piedra ( pa>pi)
    if (( jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())
     





      
