from typing import List
from .asignatura import Asignatura

class Horario:
    def __init__(self):
        self.asignaturas: List[dict] = []
    
    def agregar_asignatura(self, asignatura: Asignatura, dia: str, hora_inicio: str, hora_fin: str) -> bool:
        # Verificar si hay conflicto de horario
        for asig in self.asignaturas:
            if asig['dia'] == dia:
                if (hora_inicio >= asig['hora_inicio'] and hora_inicio < asig['hora_fin']) or \
                   (hora_fin > asig['hora_inicio'] and hora_fin <= asig['hora_fin']):
                    raise ValueError("Conflicto de horario")
        
        self.asignaturas.append({
            'asignatura': asignatura,
            'dia': dia,
            'hora_inicio': hora_inicio,
            'hora_fin': hora_fin
        })
        return True
    
    def get_horario(self) -> List[dict]:
        return self.asignaturas
