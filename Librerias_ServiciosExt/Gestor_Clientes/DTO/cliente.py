class Cliente: 
    def __init__(self, codigo, tipo, montoCredito, deuda):
        self.con = (codigo,tipo, montoCredito, deuda)
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