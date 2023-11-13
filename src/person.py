from abc import ABC, abstractmethod
from juego import Juego

class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
class Jugador(Persona):
    def __init__(self, nombre: str,sueldo: int) -> None:
        super().__init__(nombre)
        self.__sueldo = sueldo
        self.__juegos: list["Juego"]=[]
    
    def add_juego(self, juego: "Juego") -> None:
        self.__juegos.append(juego)
    
    def get_juegos(self):
        return self.__juegos
    
    def __repr__(self) -> str:
        return f'Report({self.__juegos})'
    
class Juez(Persona):
    def __init__(self, nombre:str, edad:int) -> None:
        super().__init__(nombre)
        self.__edad = edad
        self.__juegos: list["Juego"]=[]
        
    def add_juego(self, juego: "Juego") -> None:
        self.__juegos.append(juego)

