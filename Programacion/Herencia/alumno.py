from persona import Persona
class Alumno(Persona):
    def __init__(self,run,nombre,paterno,materno,fono,correos,direccion,numMatricula,carrera,asignaturas):
        super().__init__(run,nombre,paterno,materno,fono,correos,direccion)
        self.__numMatricula = numMatricula
        self.__carrera = carrera
        self.__asignaturas = asignaturas
        
    def tomarCarga(a):
        pass
    
    
consuelo = Alumno("32132132","Consuelo","Pinto","Toro",321321,"consuelo.pinyo@inacapmail.cl","puente alto","23423","Informatica","POO")

