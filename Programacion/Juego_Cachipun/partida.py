from piedra import Piedra
from papel import Papel
from tijeras import Tijeras
from jugador import Jugador
import random

class Partida:
    def __init__(self, jug1, jug2):
        self.__jugador1 = jug1
        self.__jugador2 = jug2
        
    def jugar(self):
        print(self.__jugador1.getNombre())
        print("vs")
        print(self.__jugador2.getNombre())
        
        resultado = self.__jugador1.getJugada().comparar(self.__jugador2.getJugada())
        
        return resultado
    
    

print("Bienvenido al grandioso juego del Cachipun!!")
print("ingresa tu nombre: ")
nombreJugador = input()
print("Selecciona tu jugada:")
print("1.- Piedra:")
print("2.- Papel:")
print("3.- Tijeras:")

opcion = input("Ingresa una opcion (1-3): ")

jugada_usuario = None
if opcion == "1":
    print("Haz elegido la opcion Piedra")
    jugada_usuario = Piedra()
elif opcion == "2":
    print("Haz elegido la opcion Papel")
    jugada_usuario = Papel()
elif opcion == "3":
    print("Haz elegido la opcion Tijeras")
    jugada_usuario = Tijeras()
else:
    print("opcion no valida, se asignara piedra por defecto.")
    jugada_usuario = Piedra()
    
jug1 = Jugador(nombreJugador)
jug1.setJugada(jugada_usuario)
print(f"{jug1.getNombre()} ha elegido {jug1.getJugada().getNombre()}")
jugada_pc = random.choice([Piedra(),Papel(),Tijeras()])

jug2 = Jugador("Computadora")
jug2.setJugada(jugada_pc)
print(f"{jug2.getNombre()} ha elegido {jug2.getJugada().getNombre()}")

partida = Partida(jug1,jug2)
print(partida.jugar())