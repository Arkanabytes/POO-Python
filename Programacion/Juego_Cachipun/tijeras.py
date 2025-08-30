from jugada import Jugada

class Tijeras(Jugada):
    def __init__(self):
        super().__init__("Tijeras") 
        

    def comparar(self, otra_jugada):
        if otra_jugada.getNombre().lower() == super().getNombre().lower():
            return "Empate"
        elif otra_jugada.getNombre().lower() == "piedra":
            return "Pierde"
        else:
            return "Gana"
        
        
        