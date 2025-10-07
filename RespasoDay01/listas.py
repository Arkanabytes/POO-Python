ximport os
os.system('cls')

#Listas

#CRUD
#Crear Read Update Delete

lista = [1, 2, 3]
#        0  1  2


# Read- Acceder a un elmento
print(lista[2])# -> Accedo al primer elemento de la lista
# List index out of range

print(lista[-1])# -> Accedo al ultimo elemento de la lista


#Update
#Modificar un elemento en especifico

lista[-1] = 4 # -> Al utlimo elemento de la lista le asigno el valor 4

#Agregar un elemento a la lista
lista.append(5) #-> Agrega un elemento al final de la lista

#Delete
# remove -> Remover un elemento por su dato
lista.remove(4)

# pop -> Saca un elemento de una lista por su index
elemento_sacado = lista.pop(2)# -> saca el elemento publicado en el index 2
print(elemento_sacado)

#Actividad 1
# Crear una varible que guarde la siguiente lista -> [1, 2, "Hola", 3, "Mundo", 4]
lista = [1, 2, "Hola", 3, "Mundo", 4] 
# Mostrar el mensaje  "Hola Mundo" accediendo a los indices de la lista
print(lista[2])
print(lista[4])
print()
# Agregar 2 nuevos elementos (5, 6)
lista.append(5)
lista.append(6)
# Remover el elemento "Hola" con .remove
lista.remove(3)
# Sacar el elemento " Mundo" con .pop
elemento_sacado = lista.pop(5)# -> saca el elemento publicado en el index 2
print(elemento_sacado)
