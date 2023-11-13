from ast import List
from person import Jugador, Juez

class Juego:
    def __init__(self,jugador:"Jugador",juez:"Juez",juego:"Juego") -> None:
        self.__jugador_1 = jugador
        self.__jugador_2 = jugador
        self.__juez = juez
        self.__juego_previo_1 = juego
        self.__juego_previo_2 = juego
        self.__juego_siguiente = juego
        self.__set: List["Set"] = []

    def prueba(self):
        return 0

class Set:
    def __init__(self,puntos1:int, puntos2:int) -> None:
        self.__puntos_jugador_1 = puntos1
        self.__puntos_jugador_2 = puntos2