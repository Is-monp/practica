from ast import List
from person import Juez,Jugador
from juego import Juego

class Campeonato:
    def __init__(self) -> None:
        self.__juegos: List["Juego"] = []

    def add_juego(self,juego:Juego):
        self.__juegos.append(juego)
    
    def get_juego(self,indice):
        return self.__juegos[indice]
    
    def get_juegos(self,indice):
        return self.__juegos
    
    def show_resumen(self):
        ganador = ""
        for juego in self.__juegos:
            print(juego)
            ganador = juego.asignar_ganador(juego)
            print("Ganador: ", ganador.nombre)
        print("El ganador del campeonato es: ",ganador.nombre)
    

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
    
    def calc_sets_ganados_jugadores_campeonato(self,indice):
        sets_ganados = 0
        for jugador in self.__jugadores:
            for juego in jugador.get_juegos():
                sets_ganados = sets_ganados+juego.sets_ganados_juego(jugador)
            print("El jugador ", jugador.nombre, "ganó ",sets_ganados, " en el campeonato")
            sets_ganados=0
        
    
            


    