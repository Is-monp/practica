from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre):
        self._nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
class jugador(Persona):
    def __init__(self, nombre,sueldo, juegos):
        super().__init__(nombre)
        self.__sueldo = sueldo
        self.__juegos = list[juegos]
    
    @property
    def sueldo(self):
        return self.__sueldo
    
    def __str__(self):
        return f"Nombre: {self.nombre}, sueldo: {self.sueldo}"

class Juez(Persona):
    def __init__(self, nombre, edad, juegos):
        super().__init__(nombre)
        self.__edad = edad
        self.__juegos = list[juegos]
        
    @property
    def edad(self):
        return self.__edad
    
    @property
    def juegos(self):
        return self.__juegos


    

