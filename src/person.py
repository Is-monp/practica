from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre):
        self._nombre = nombre
    
class Jugador(Persona):
    def __init__(self, nombre: str,sueldo: int) -> None:
        super().__init__(nombre)
        self.__sueldo = sueldo
        self.__juegos: list["Juego"]=[]
    
    def add_juego(self, juego: "Juego") -> None:
        self.__juegos.append(juego)
    
class Juez(Persona):
    def __init__(self, nombre:str, edad:int) -> None:
        super().__init__(nombre)
        self.__edad = edad
        self.__juegos: list["Juego"]=[]
        
    def add_juego(self, juego: "Juego") -> None:
        self.__juegos.append(juego)