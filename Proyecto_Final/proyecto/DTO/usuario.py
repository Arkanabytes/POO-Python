from DAO.conexion import Conexion
import bcrypt
from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

load_dotenv()

# Parámetros de conexión
host = os.getenv("host")
user = os.getenv("user")
passwordS = os.getenv("password")
db = os.getenv("db")

class Usuario:
    def __init__(self, username, password_hash, nombre, apellidos, email, tipo_usuario):
        self.__username = username
        self.__password_hash = password_hash
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email
        self.__tipo_usuario = tipo_usuario

    # Getters
    def get_username(self):
        return self.__username

    def get_password_hash(self):
        return self.__password_hash

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_email(self):
        return self.__email

    def get_tipo_usuario(self):
        return self.__tipo_usuario

    @staticmethod
    def login(username, password):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                database='unigo_db',
                user='root',
                password=''
            )
            
            cursor = conexion.cursor()
            
            query = "SELECT * FROM usuarios WHERE username = %s"
            cursor.execute(query, (username,))
            usuario = cursor.fetchone()
            
            if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario[2].encode('utf-8')):
                return Usuario(
                    username=usuario[1],
                    password_hash=usuario[2],
                    nombre=usuario[3],
                    apellidos=usuario[4],
                    email=usuario[5],
                    tipo_usuario=usuario[6]
                )
            return None
            
        except Error as e:
            print(f"Error en login: {e}")
            return None
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    @staticmethod
    def registrar_usuario(username, password, nombre, apellidos, email, tipo_usuario):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                database='unigo_db',
                user='root',
                password=''
            )
            
            cursor = conexion.cursor()
            
            # Generar el hash de la contraseña
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            
            # Crear la tabla si no existe
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) UNIQUE,
                    password VARCHAR(255),
                    nombre VARCHAR(100),
                    apellidos VARCHAR(100),
                    correo VARCHAR(100),
                    tipo_usuario VARCHAR(20)
                )
            ''')
            
            # Insertar el nuevo usuario
            query = "INSERT INTO usuarios (username, password, nombre, apellidos, correo, tipo_usuario) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (username, hashed, nombre, apellidos, email, tipo_usuario)
            cursor.execute(query, valores)
            
            conexion.commit()
            print("¡Usuario registrado exitosamente!")
            
        except Error as e:
            print(f"Error al registrar usuario: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()