class Tipo_Usuario:
    def __init__(self, codigo, nombre):
        self.__id = codigo
        self.__nombre = nombre

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    # Setters
    def set_id(self, codigo):
        self.__id = codigo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self) -> str:
        return f"Cod: {self.__id} - {self.__nombre}"
