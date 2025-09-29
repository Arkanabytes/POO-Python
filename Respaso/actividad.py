#Actividad 1

# Crear una varible que guarde la siguiente lista -> [1, 2, "Hola", 3, "Mundo", 4]
lista = [1, 2, "Hola", 3, "Mundo", 4] 

# Mostrar el mensaje  "Hola Mundo" accediendo a los indices de la lista
print(lista[2], lista[4])
print(f"{lista[2]} {lista[4]}")

# Agregar 2 nuevos elementos (5, 6)
lista.append(5)
lista.append(6)

# Remover el elemento "Hola" con .remove
print(lista)
lista.remove("hola")
lista.remove(3)

lista.pop(3)
print(lista)

# Sacar el elemento " Mundo" con .pop
elemento_sacado = lista.pop(5)# -> saca el elemento publicado en el index 2
print(elemento_sacado)




# Otra solucion
import os
os.system('cls')


class Libro:
    def __init__(self,isbn:str,titulo:str,autor:str,cant_paginas:int):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.cant_paginas = cant_paginas
        
    #Metodos
    def imprimir_info(self):
        print("-----------------------------")
        print("Titulo: ",self.titulo)
        print("Autor: ",self.autor)
        print("Cantidad Paginas: ",self.cant_paginas)
        
    def cambiar_titulo(self,nuevo_titulo:str):
        self.titulo = nuevo_titulo
        
libro1 = Libro("1","Papelucho","Marcela Paz",100)
libro2 = Libro("2","La llamada de Cthulhu","HP Lovecraft",45)
libro3 = Libro("3","Harry Potter y la Camara Secreta","JK Rowling",100)

libros = [libro1,libro2,libro3]

libro1.cambiar_titulo("Mujercita")

for libro in libros:
    libro.imprimir_info()
