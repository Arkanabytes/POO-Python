import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='unigo_db',
                user='root',
                password=''
            )
        except Error as e:
            print(f"Error de conexión a MySQL: {e}")

    def crear_tablas(self):
        cursor = self.connection.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INT PRIMARY KEY,
                nombre VARCHAR(100),
                email VARCHAR(100),
                carrera VARCHAR(100),
                año INT,
                saldo_cuenta FLOAT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INT PRIMARY KEY AUTO_INCREMENT,
                estudiante_id INT,
                precio_total FLOAT,
                estado VARCHAR(20),
                FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
            )
        ''')
        
        self.connection.commit()
