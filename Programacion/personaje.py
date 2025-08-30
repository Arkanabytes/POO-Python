class Personaje:
    
    #Constructor de la clase, primera clase que se ejecuta al instanciar un objeto
    def __init__(self, nombre, nivel, salud, energia, raza):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__salud = salud
        self.__energia = energia
        self.__raza = raza
    
    #metodo get para acceder a un atributo privado o protegido
    def getNombre(self):
        return self.__nombre
    #metodo get para acceder a un atributo privado o protegido
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    #otros metodos definidos en el diagrama de clases
    def atacar(self, enemigo):
        pass 
    
    def defender(self):
        pass 
    
    def curar(self, personaje):
        pass 

# Instancia de la clase Personaje 
superman = Personaje("Clark Kent", 1000000,  1000000,  1000000, "Krypton")
print(f"Nombre del personaje es: {superman.getNombre()}")

superman.setNombre("Bruce Wayne")
print(f"Nombre del personaje es: {superman.getNombre()}")
