from typing import List
from .producto import Producto

class Pedido:
    def __init__(self, id: int, estudiante_id: int):
        self.id = id
        self.estudiante_id = estudiante_id
        self.productos: List[Producto] = []
        self.precio_total = 0
        self.estado = "pendiente"
        
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        self.precio_total += producto.precio
        
    def confirmar(self) -> bool:
        if self.estado != "pendiente":
            raise ValueError("El pedido ya no está en estado pendiente")
        self.estado = "confirmado"
        return True
        
    def cambiar_estado(self, nuevo_estado: str):
        estados_validos = ["pendiente", "confirmado", "en_preparacion", "entregado"]
        if nuevo_estado not in estados_validos:
            raise ValueError("Estado no válido")
        self.estado = nuevo_estado
