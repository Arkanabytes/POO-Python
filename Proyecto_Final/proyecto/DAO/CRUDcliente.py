from DAO.conexion import Conexion
from dotenv import load_dotenv
import os
load_dotenv()

# Parámetros de conexión
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def agregar(c):
    try:
        con = Conexion(host, user, password, db)
        # Usamos los getters para obtener los valores
        sql = "INSERT INTO CLIENTE SET run='{}', nombre='{}', apellido='{}', direccion='{}', " \
              "fono={}, correo='{}', montoCredito={}, deuda={}, TIPO_id={}".format(
              c.get_run(), c.get_nombre(), c.get_apellido(), c.get_direccion(), c.get_fono(),
              c.get_correo(), c.get_montoCredito(), c.get_deuda(), c.get_tipo())
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nDatos Ingresados Satisfactoreamente")
        con.desconectar()
    except Exception as e:
        print(e)

def editar(c_lista):
    try:
        con = Conexion(host, user, password, db)
        sql = "UPDATE CLIENTE SET run='{}', nombre='{}', apellido='{}', direccion='{}', fono={}, correo='{}', " \
              "montoCredito={}, deuda={}, TIPO_id={} WHERE id={}".format(
              c_lista[1], c_lista[2], c_lista[3], c_lista[4], c_lista[5], c_lista[6],
              c_lista[7], c_lista[8], c_lista[9], c_lista[0])
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nDatos Modificados Satisfactoreamente")
        con.desconectar()
    except Exception as e:
        print(e)

# --- El resto de las funciones no necesitan cambios ---
def eliminar(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM CLIENTE WHERE id={}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nCliente Eliminado Satisfactoreamente")
        con.desconectar()
    except Exception as e:
        print(e)

def mostrartodos():
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from CLIENTE"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def consultaparticular(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from CLIENTE where id={}".format(id)
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def consultaparcial(cant):
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from CLIENTE"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size=cant)
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def mostrartipos():
    try:
        con = Conexion(host, user, password, db)
        sql = "select id,nombre from TIPO"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)
