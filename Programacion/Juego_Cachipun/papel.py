from jugada import Jugada

class Papel(Jugada):
    def __init__(self):
        super().__init__("Papel") 
        

    def comparar(self, otra_jugada):
        if otra_jugada.getNombre().lower() == super().getNombre().lower():
            return "Empate"
        elif otra_jugada.getNombre().lower() == "tijeras":
            return "Pierde"
        else:
            return "Gana"
        
        
        