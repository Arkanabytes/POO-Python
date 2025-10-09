from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, id: int, nombre: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    @abstractmethod
    def mostrar_info(self) -> str:
        pass
