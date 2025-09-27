import os
os.system('cls')

#Una funcion es un bloque de codigo reutilizable para una determinada tarea 
# Snake_case -> to en minuscula y separado con guion bajo masa_user
# Cap
# PascalCase -> Toda palabra capitalizada EsteEsElPeso
def saludar(nombre:str)-> None:
    print("Hola", nombre)
    
print (saludar("Pablo"))
saludar("Pedro")


#Actividad 2

#Crear una funcion que determine si un numero es positivo, negativo o 0

def verificar(numero:int)-> None:

#Esta funcion requiere de un parametro de un numero entero
    if numero > 0:

#Si el numero es postivo. imprima que es un positivo
        print("El numero", numero, " es negativo")

#Si el numero es negativo, imprima que es negativo
    elif numero < 0:
        print("El numero", numero, " es negativo")

#Si el numero es 0, imprima que es 0
    else:
        print("Es 0")

# Muestre cada caso
verificar(5)
verificar(-5)
verificar(0)