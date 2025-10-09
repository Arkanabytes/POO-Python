class Asignatura:
    def __init__(self, id: int, nombre: str, profesor: str, creditos: int):
        self.id = id
        self.nombre = nombre
        self.profesor = profesor
        self.creditos = creditos
        self.horario = None
    
    def __str__(self):
        return f"{self.nombre} - Prof. {self.profesor}"
    
    def asignar_horario(self, horario):
        self.horario = horario
