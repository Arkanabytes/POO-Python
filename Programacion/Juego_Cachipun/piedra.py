from jugada import Jugada

class Piedra(Jugada):
    def __init__(self):
        super().__init__("Piedra") 

    def comparar(self, otra_jugada):
        if otra_jugada.getNombre().lower() == super().getNombre().lower():
            return "Empate"
        elif otra_jugada.getNombre().lower() == "papel":
            return "Pierde"
        else:
            return "Gana"
        
        
        