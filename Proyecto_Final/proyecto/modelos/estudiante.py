from .usuario import Usuario
from .asignatura import Asignatura
from .horario import Horario

class Estudiante(Usuario):
    def __init__(self, id: int, nombre: str, email: str, telefono: str,
                 carrera: str, año: int, saldo_cuenta: float):
        super().__init__(id, nombre, email, telefono)
        self.carrera = carrera
        self.año = año
        self.saldo_cuenta = saldo_cuenta
        self.horario = Horario()
        
    def mostrar_info(self) -> str:
        return f"Estudiante: {self.nombre} - Carrera: {self.carrera} - Año: {self.año}"
        
    def pagar_servicio(self, monto: float) -> bool:
        if self.saldo_cuenta >= monto:
            self.saldo_cuenta -= monto
            return True
        raise ValueError("Saldo insuficiente")
        
    def inscribir_asignatura(self, asignatura: Asignatura) -> bool:
        return self.horario.agregar_asignatura(asignatura)
