class Producto:
    def __init__(self, id: int, nombre: str, precio: float, categoria: str):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
    def get_precio(self):
        return self.precio
    
    def get_categoria(self):
        return self.categoria
