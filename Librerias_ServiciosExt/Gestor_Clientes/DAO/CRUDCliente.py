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


def agregarCliente(nombre, apellido, dni, telefono, direccion):
    try:
        con = Conexion(host,user,passwd, db)
        sql = "Insert into cliente (cli_nombre, cli_apellido, cli_dni, cli_telefono, cli_direccion) values ('{}','{}','{}','{}','{}')".format(nombre, apellido, dni, telefono, direccion)
        cursor = con.ejecutarQuery(sql)
        con.desconectar()
    except Exception as e:
        print(e)
    return "Cliente agregado"
  
def mostrarClientes():
    try:
        con = Conexion(host,user,passwd, db)
        sql = "Select * from cliente"
        cursor = con.ejecutarQuery(sql)
        datos = cursor.fetchall()
        con.desconectar()
    except Exception as e:
        print(e)
    return datos
  
def buscarCliente(dni):
    try:
        con = Conexion(host,user,passwd, db)
        sql = "Select * from cliente where cli_dni = '{}'".format(dni)
        cursor = con.ejecutarQuery(sql)
        datos = cursor.fetchone()
        con.desconectar()
    except Exception as e:
        print(e)
    return datos
  
def editarCliente(id, nombre, apellido, dni, telefono, direccion):
    try:
        con = Conexion(host,user,passwd, db)
        sql = "Update cliente set cli_nombre='{}', cli_apellido='{}', cli_dni='{}', cli_telefono='{}', cli_direccion='{}' where cli_id='{}'".format(nombre, apellido, dni, telefono, direccion, id)
        cursor = con.ejecutarQuery(sql)
        con.desconectar()
    except Exception as e:
        print(e)
    return "Cliente editado"
  
def eliminarCliente(id):
    try:
        con = Conexion(host,user,passwd, db)
        sql = "Delete from cliente where cli_id='{}'".format(id)
        cursor = con.ejecutarQuery(sql)
        con.desconectar()
    except Exception as e:
        print(e)
    return "Cliente eliminado"
  

  
print(mostrarTodos())
print(mostrarParcial(0))
print(mostrarParticular(0))

print(mostrarTodos())
print(mostrarParcial(0))

print(mostrarParticular(0))
