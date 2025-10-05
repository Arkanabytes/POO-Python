from clases import Mascota
from bd import hacer_consulta



def crear_mascota():
    while True:
        try:
            id = int(input("Ingrese el id de la mascota: "))
        except Exception as e:
            print("Ese no es un id valido")
        else:
            break
    nombre = input("Ingrese el nombre de la mascota: ")
    apodo = input("Ingrese el apodo de la mascota: ")
    mascota = Mascota(id,nombre,apodo)
    print(mascota.info_mascota())
    confirm = input("Está correcto? (y/n) ")
    if confirm.lower() == 'y':
        try:
            mascota.guardar_mascota()
        except Exception as e:
            print("Ha ocurrido un error al crear la mascota")
        else:
            print("Mascota creada con exito!")
        
        
def mostrar_mascotas():
    query = "SELECT * FROM MASCOTA"
    mascotas = []
    try:
        data = hacer_consulta(query,'select')
    except Exception as e:
        print("Ha ocurrido un error al traer las mascotas: ",e)
    else:
        for dato in data:
            mascotas.append(Mascota(dato[0],dato[1],dato[2]))
            
        if mascotas:
            for mascota in mascotas:
                print(mascota.info_mascota())
                
                

        
        
        
        