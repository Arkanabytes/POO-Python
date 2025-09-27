# Una clase
# Clae -> plantilla

# Libro

class Libro:
    #Contructor
    def __init__(self, ISBN, titulo, autor, cant_paginas):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.cant_paginas = cant_paginas
        
# Metodos muestra toda la informacion de los libros
    def imprimir_info(self):
        print("Los datos del libro son: ", self.ISBN,self.titulo,self.autor,self.cant_paginas)
        print("El Isbn es ", self.ISBN)
        print("El Titulo es ", self.titulo)
        print("El Autor es ", self.autor)
        print("La cantidad de paginas es: ", self.cant_paginas)
        
#Guardar los libros creados en una lista
    def guardar_libros(self):
        print("Los datos del libro son: ", self.ISBN,self.titulo,self.autor,self.cant_paginas)



l1 = Libro("234560097", "El Quijote", "Miguel de Cervantes", 1000)
print(l1.titulo)

l2 = Libro("234569897", "Cien años de soledad", "Marquz", 300)
print(l2.titulo)

l1.imprimir_info()
l2.imprimir_info()