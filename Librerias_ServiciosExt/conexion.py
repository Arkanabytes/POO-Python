import pymysql

host = "localhost"
user = "root"
password = ""
db = "prueba"

con = pymysql.connect(host= user, user= user, password=password, db =db)
cursor = con.cursor()

select = cursor.execute("Select * from clientes")
datos select.fetchall()
