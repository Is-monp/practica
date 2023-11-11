from ast import List
from person import Jugador, Juez
from typing import Optional

class Juego:
    def __init__(self,jugador:"Jugador",juez:"Juez",juego:"Juego") -> None:
        self.__jugador_1 = jugador
        self.__jugador_2 = jugador
        self.__juez = juez
        self.__juego_previo_1 = juego
        self.__juego_previo_2 = juego
        self.__juego_siguiente = juego
        self.__sets: List["Set"] = []
    
    def add_sets(self, set1:"Set", set2:"set", set3:Optional["set"]=None) -> None:
        self.__sets.append(set1)
        self.__sets.append(set2)
        if set3 is not None:
            self.__sets.append(set3)
            

class Set:
    def __init__(self,puntos1:int, puntos2:int) -> None:
        self.__puntos_jugador_1 = puntos1
        self.__puntos_jugador_2 = puntos2