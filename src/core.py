from ast import List
from person import Juez
from person import Jugador

class Campeonato:
    def __init__(self) -> None:
        self.__juegos: List["Juego"] = []



class LigaTenis:
    def __init__(self) -> None:
        self.__campeonatos: List["Campeonato"] = []
        self.__jueces: List["Juez"] = []
        self.__jugadores: List["Jugador"] = []


    def add_juez(self,juez:Juez):
        self.__jueces.append(juez)

    def add_jugador(self,jugador:Jugador):
        self.__jugadores.append(jugador)

    def add_juez(self,campeonato:Campeonato):
        self.__campeonatos.append(campeonato)