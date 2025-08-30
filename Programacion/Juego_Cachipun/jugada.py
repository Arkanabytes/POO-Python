from abc import ABC, abstractmethod

class Jugada(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
        
    @abstractmethod
    def comparar(self,otra_jugada):
        pass