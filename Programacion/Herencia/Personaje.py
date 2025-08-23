class Personaje:
    #Constructor de la clase, primera clase que se ejecuta al instanciar un objeto
    def __init__(self, run,nombre,paterno, materno, fono, correos, direccion):
        self.__nombre = run
        self.__nivel = nombre
        self.__salud = paterno
        self.__energia = materno
        self.__raza = fono
        self.__salud = correos
        self.__energia = materno
        self.__raza = direccion
        
    #crear metodos getter and setter para acceder a atributos privados
    
    def saludar():
        pass
    def comer(almuerzo):
        return 0
    def leer(libro, paginas):
        return 0
