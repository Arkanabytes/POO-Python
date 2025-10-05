from crud import *





menu = """
1. Crear Mascota
2. Ver Mascotas
3. Salir
"""


while True:
    print(menu)
    eleccion = input("Elija una opción: ")
    if eleccion == '1':
        crear_mascota()
    elif eleccion == '2':
        print("###### Mostrando Mascotas! ########")
        mostrar_mascotas()
    elif eleccion == '3':
        print("Adioooos 🤞")
    else:
        print("Esa no es una opción valida")

