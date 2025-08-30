class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__jugada = None
        
    def getNombre(self):
        return self.__nombre
    
    def getJugada(self):
        return self.__jugada
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setJugada(self, jugada):
        self.__jugada = jugada