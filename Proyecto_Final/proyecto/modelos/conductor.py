from .usuario import Usuario

class Conductor(Usuario):
    def __init__(self, id: int, nombre: str, email: str, telefono: str,
                 patente: str, tipo_vehiculo: str):
        super().__init__(id, nombre, email, telefono)
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.calificacion = 5.0
        self.viajes = []
        
    def mostrar_info(self) -> str:
        return f"Conductor: {self.nombre} - Patente: {self.patente}"
        
    def calcular_tarifa(self, distancia: float) -> float:
        tarifa_base = 1000
        return tarifa_base + (distancia * 300)
        
    def registrar_viaje(self, origen: str, destino: str, distancia: float):
        tarifa = self.calcular_tarifa(distancia)
        self.viajes.append({
            "origen": origen,
            "destino": destino,
            "tarifa": tarifa
        })
        return tarifa
