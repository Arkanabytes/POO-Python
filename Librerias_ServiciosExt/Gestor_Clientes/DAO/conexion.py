import pymysql

class Conexion: 
    def __init__(self, host, usuario, clave, bd):
        self.con = pymysql.connect(host=host, user= usuario, password=clave, db=bd)
        self.cursor = self.con.cursor()
        
    def ejecutarQuery(self,sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def desconectar(self):
        self.con.close()
        
    def commit(self):
        self.con.commit()
    
    def rollback(self):
        self.con.rollback()