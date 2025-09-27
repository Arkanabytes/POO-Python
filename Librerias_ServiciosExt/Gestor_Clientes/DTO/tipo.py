class Tipo: 
    def __init__(self, codigo, nombre):
        self.con = pymysql.connect(codigo, nombre)
        self.cursor = self.con.cursor()
        
