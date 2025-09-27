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
