from ast import List
class LigaTenis:
    def __init__(self) -> None:
        self.__campeonatos: List["Campeonato"] = []
        self.__jueces: List["Juez"] = []
        self.__jugadores: List["Jugador"] = []
class Campeonato:
    def __init__(self) -> None:
        self.__juegos: List["Juego"] = []