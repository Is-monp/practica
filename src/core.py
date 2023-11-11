from ast import List
from person import Juez, Jugador
class LigaTenis:
    def __init__(self) -> None:
        self.__campeonatos: List["Campeonato"] = []
        self.__jueces: List["Juez"] = []
        self.__jugadores: List["Jugador"] = []


    def add_juez(self,juez:"Juez"):
        return 0

class Campeonato:
    def __init__(self) -> None:
        self.__juegos: List["Juego"] = []