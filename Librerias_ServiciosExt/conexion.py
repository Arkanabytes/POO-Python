import pymysql

host = "localhost"
user = "root"
password = ""
db = "prueba"

con = pymysql.connect(host= user, user= user, password=password, db =db)
cursor = con.cursor()

cursor.execute("Select * from clientes")
datos = cursor.fetchall()
print(datos)

cursor.execute("Select * from clientes where cli_nombre = 'Aldo'")
datos = cursor.fetchone()
print(datos)

cursor.execute("Select * from clientes where cli_nombre = 'Aldo'")
datos = cursor.fetchmany(size=2)
print(datos)
