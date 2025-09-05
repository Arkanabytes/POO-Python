class Libro:
    def _init__(self, nombre, genero, isbn, autor, estado= false):
        self.__nombre = nombre
        self.__genero = genero
        self.__isbn = isbn
        self.__autor = autor
        self.__estado = estado

def__ str__(self):
    return f"Nombre: {self.__nombre}, Genero: {self.__genero}, ISBN: {self.__isbn}, Autor: {self.__autor}, Estado: {'Prestado' if self.__estado else 'Disponible'}"

def get_nombre(self):
    return self.__nombre

def get_genero(self):
    return self.__genero
def get_isbn(self):
    return self.__isbn
def get_autor(self):
    return self.__autor
def get_estado(self):
    return self.__estado


def set_Nombre(self, nombre):
    self.__nombre = nombre
def set_Autor(self, autor):
    self.__autor = autor

def set_Genero(self, genero):
    self.__genero = genero

def set_Isbn(self, isbn):
    self.__isbn = isbn

def set_Estado(self, estado):
    self.__estado = estado
