# Una clase
# Clae -> plantilla

# Estructura de una clase
# nombre clase    -> Capitalizada y singular
# propiedades     -> Atributos
# comportamiento  -> Metodos

class Persona:
    #Contructor
    def __init__(self, nombre, apellido, edad ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
# Metodos
    def saludar(self):
        print("Hola! Mi nombre es ", self.nombre)

p1 = Persona("Pablo", "Picasso", 89)
print(p1.nombre)

p2 = Persona("Diego", "Nepucemo", 78)
print(p2.nombre)

p1.saludar()
p2.saludar()
