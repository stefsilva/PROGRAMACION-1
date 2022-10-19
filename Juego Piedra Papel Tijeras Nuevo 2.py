#Piedra Papel o Tijera

import random

res = int(1)
jugadas = ["Piedra", "Papel", "Tijera"]

while(res == 1):

    jugadaUsuario = int(input("Por favor ingrese su jugada: [1:Piedra; 2:Papel; 3:Tijera]: "))
    jugada = jugadas[jugadaUsuario - 1]
    jugadaMaquina = jugadas[ random.randint(0,2)]

    if ((jugada == "Piedra") and(jugadaMaquina == "Tijeras")):
        print ("Ganaste Jugador. La máquina jugó: " + str(jugadaMaquina) + "\n");
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
   
res = int(input("\n Desea continuar intentando: [1:si; 2:no]: "))
