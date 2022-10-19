#Piedra Papel o Tijera
import random
def funcion():
    print('Bienvenidos al Juego de Piedra, Papel o Tijera')
    vec=0
    jugadas = ["Piedra", "Papel", "Tijera"]

    while vec != 2:

        jugadaUsuario = int(input("Hola! por favor ingreso su jugada: 1. Piedra, 2. Papel o 3. Tijera"))
        jugada = jugadas[jugadaUsuario - 1]
        jugadaMaquina = jugadas[ random.randint(0,2)]

        if ((jugada == "Piedra") and(jugadaMaquina == "Tijeras")):
            print ("Ganaste Jugador!" "La máquina jugó: " + str(jugadaMaquina) + "\n");
        if ((jugada == "Papel") and (jugadaMaquina == "Piedra")):   
            print ("Ganaste Jugador. La máquina jugó:  " + str(jugadaMaquina) + "\n");
        if ((jugada == "Tijera") and (jugadaMaquina == "Papel")):
            print ("Ganaste Jugador. La máquina jugó:  " + str(jugadaMaquina) + "\n");
        if ((jugadaMaquina == "Piedra" and (jugada == "Tijera"))):
            print ("Uy te ganó la Máquina porque jugó: " + str(jugadaMaquina) + "\n");
        if ((jugadaMaquina == "Papel" and (jugada == "Piedra"))):
            print ("Uy te ganó la Máquina porque jugó: " + str(jugadaMaquina) + "\n");  
        if ((jugadaMaquina == "Tijeras" and (jugada == "Papel"))):
            print ("Uy te ganó la Máquina porque jugó: " + str(jugadaMaquina) + "\n");
        if (((jugadaMaquina == "Piedra") and (jugada == "Piedra") or (jugadaMaquina == "Papel") and (jugada == "Papel") or (jugadaMaquina == "Tijeras") and (jugada == "Tijeras"))):
            print ("Empate")
                
        vec=int(input("/n ¿desea continuar? Escriba '1.Si' o '2.No'"))
