from conexion import Conexion
import os
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("HOST")
passwd = os.getenv("PASS")
user = os.getenv("USER")
db = os.getenv("DB")

conexion1 = Conexion(host, user, passwd, db)
cursor = conexion1.ejecutarQuery("select * from cliente")
datos = cursor.fetchall()
print(datos)
conexion1.desconectar()