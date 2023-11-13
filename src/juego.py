from ast import List
from typing import Optional

class Juego:
    
    def __init__(self,jugador_1 = None,jugador_2= None,juez = None, juego_previo_1:Optional["Juego"]=None,juego_previo_2:Optional["Juego"]=None) -> None:
        self.__jugador_1 = jugador_1
        self.__jugador_2 = jugador_2
        self.__juez = juez
        self.__juego_previo_1 = juego_previo_1
        self.__juego_previo_2 = juego_previo_2
        self.__juego_siguiente = "Juego"
        self.__sets: List["Set"] = []

        if self.__jugador_1 is None:
            self.__jugador_1 = self.asignar_ganador(juego_previo_1)
            self.__jugador_2 = self.asignar_ganador(juego_previo_2)

        self.asignar_juegos(self.__jugador_1)
        self.asignar_juegos(self.__jugador_2)

    def asignar_ganador(self,juego):
        puntos1 = 0
        puntos2 = 0
        for set in juego.get_set():
            if set.get_p1() > set.get_p2():
                puntos1 = puntos1+1
            else:
                puntos2 = puntos2+1
            
        if puntos1>puntos2:
            jugador = juego.__jugador_1
        else:
            jugador = juego.__jugador_2

        return jugador
    
    def asignar_juegos(self,jugador):
        jugador.add_juego(self)

    def get_set(self):
        return self.__sets
    
    def add_sets(self, set1:"Set", set2:"set", set3:Optional["set"]=None) -> None:
        self.__sets.append(set1)
        self.__sets.append(set2)
        if set3 is not None:
            self.__sets.append(set3)
    
    def sets_ganados_juego(self, jugador):
        if jugador == self.__jugador_1:
            indice = "Jugador1"
        else:
            indice = "Jugador2"
        
        contador = 0

        for set in self.__sets:
            if indice == set.ganador_set():
                contador = contador+1

        return contador

    def __repr__(self) -> str:
        return f'Report({self.__jugador_1.nombre},{self.__jugador_2.nombre},{self.__juez.nombre},{self.__sets})'
       
class Set:
    def __init__(self,puntos1:int, puntos2:int) -> None:
        self.__puntos_jugador_1 = puntos1
        self.__puntos_jugador_2 = puntos2

    def get_p1(self):
        return self.__puntos_jugador_1
    def get_p2(self):
        return self.__puntos_jugador_2

    def __repr__(self) -> str:
        return f'Report({self.__puntos_jugador_1},{self.__puntos_jugador_2})'
    
    def ganador_set(self):
        if self.__puntos_jugador_1>self.__puntos_jugador_2:
            return "Jugador1"
        else:
            return "Jugador2"