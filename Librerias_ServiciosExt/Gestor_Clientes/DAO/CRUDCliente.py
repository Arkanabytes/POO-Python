from conexion import Conexion
import os
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("HOST")
passwd = os.getenv("PASS")
user = os.getenv("USER")
db = os.getenv("DB")

#conexion1 = Conexion(host, user, passwd, db)
#cursor = conexion1.ejecutarQuery("select * from cliente")
#datos = cursor.fetchall()
#print(datos)
#conexion1.desconectar()

def mostrarTodos() :
      try:
            con = Conexion(host,user,passwd, db)
            sql = "Select * from cliente"
            cursor = con.ejecutarQuery(sql)
            datos = cursor.fetchall()
            con.desconectar()
      except Exception as e:
             print(e)
      return datos

def mostrarParcial(cant) :
      try:
          con = Conexion(host,user,passwd, db)
          sql = "Select * from cliente"
          cursor = con.ejecutarQuery(sql)
          datos = cursor.fetchmany(size=cant)
          con.desconectar()
      except Exception as e:
        print(e)
      return datos

def mostrarParticular(id):
  try:
      con = Conexion(host,user,passwd, db)
      sql = "Select * from cliente where cli_id= '{}' ". format(id)
      cursor = con.ejecutarQuery(sql)
      datos = cursor.fetchone(id)
      con.desconectar()
  except Exception as e:
    print(e)
  return datos

print(mostrarTodos())
print(mostrarParcial(0))
print(mostrarParticular(0))