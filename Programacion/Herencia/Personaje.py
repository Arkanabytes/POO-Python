class Persona:
    def __init__(self,run,nombre,paterno,materno,fono,correos,direccion):
        self.__run = run
        self.__nombre = nombre
        self.__paterno = paterno
        self.__materno = materno
        self.__fono = fono 
        self.__correos = correos
        self.__direccion = direccion

    def getRun(self):
        return self.__run

    def setRun(self, value):
        self.__run = value

    def getNombre(self):
        return self.__nombre

    def setNombre(self, value):
        self.__nombre = value

    def getPaterno(self):
        return self.__paterno

    def setPaterno(self, value):
        self.__paterno = value

    def getMaterno(self):
        return self.__materno

    def setMaterno(self, value):
        self.__materno = value

    def getFono(self):
        return self.__fono

    def setFono(self, value):
        self.__fono = value

    def getCorreos(self):
        return self.__correos

    def setCorreos(self, value):
        self.__correos = value
        
    def getDireccion(self):
        return self.__direccion
    
    def setDireccion(self, value):
        self.__direccion = value

    
    #crear metodos getter and setter para acceder a atributos privados
    
    def saludar():
        pass
    
    def comer(almuerzo):
        return 0
    
    def leer(libro,paginas):
        pass
