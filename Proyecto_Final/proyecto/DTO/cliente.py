from DTO.socioNegocio import SocioNegocio
from DTO.tipo import Tipo_Usuario

class Cliente(SocioNegocio):
    def __init__(self, run, nombre, apellido, direccion, fono, correo, tipo, montoCredito=500, deuda=0):
        super().__init__(run, nombre, apellido, direccion, fono, correo)
        self.__tipo = tipo
        self.__montoCredito = montoCredito
        self.__deuda = deuda

    # Getters
    def get_tipo(self):
        return self.__tipo

    def get_montoCredito(self):
        return self.__montoCredito

    def get_deuda(self):
        return self.__deuda

    # Setters
    def set_tipo(self, tipo):
        self.__tipo = tipo

    def set_montoCredito(self, monto):
        self.__montoCredito = monto

    def set_deuda(self, deuda):
        self.__deuda = deuda

    def __str__(self):
        # Usamos los getters de la clase padre
        return f"{self.get_nombre()} {self.get_apellido()} - {self.__tipo.get_nombre()}"

    def pagar(self, monto):
        if monto > 0:
            self.__deuda -= monto
            print(f"Se pagaron {monto} pesos. Deuda actual: {self.__deuda} pesos")
        else:
            print("El monto a pagar debe ser mayor que cero.")
