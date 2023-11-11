from ast import List
from person import Juez,Jugador

class Campeonato:
    def __init__(self) -> None:
        self.__juegos: List["Juego"] = []

    def add_juego(self,juego:"Juego"):
        self.__juego_siguiente = juego
    



class LigaTenis:
    def __init__(self) -> None:
        self.__campeonatos: List["Campeonato"] = []
        self.__jueces: List["Juez"] = []
        self.__jugadores: List["Jugador"] = []

    def add_juez(self,juez:Juez):
        self.__jueces.append(juez)

    def add_jugador(self,jugador:Jugador):
        self.__jugadores.append(jugador)

    def add_campeonato(self,campeonato:Campeonato):
        self.__campeonatos.append(campeonato)


    def get_jugador(self,indice):
        return self.__jugadores[indice]
    
    def get_juez(self,indice):
        return self.__jueces[indice]
    
    def get_campeonato(self,indice:int):
        return self.__campeonatos[indice]