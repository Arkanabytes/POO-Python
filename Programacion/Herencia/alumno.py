from persona import Persona
class Alumno(Persona):
    def __init__(self, run , nombre, paterno, materno, fono, correos, direccion, numMatricula, carrera, asignaturas):
        super().__init__( nombre, paterno, materno, fono, correos, direccion)
        self.__numMatricula = numMatricula
        self.__carrera = carrera
        self.__asignaturas = asignaturas
        
    def tomaCarga(a):
        pass
consuelo = Alumno("321223344", "Consuelo", "Jaramillo", "Contreras",13345, "consuelo@incapmail.cl", "puente alto", "193939954", "Informatica", "POO")
        
    
