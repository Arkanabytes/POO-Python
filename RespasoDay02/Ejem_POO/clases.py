from bd import hacer_consulta


class Mascota():
    def __init__(self,id_mascota,nombre,apodo):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.apodo = apodo
        
    def __repr__(self):
        return self.nombre
    
    def info_mascota(self):
        return(f"""
              #####################
              ID: {self.id_mascota}
              Nombre: {self.nombre}
              Apodo: {self.apodo}
              """
              )
              
    def guardar_mascota(self):
        query = "INSERT INTO MASCOTA VALUES (:id,:nombre,:apodo)"
        variables = [self.id_mascota,self.nombre,self.apodo]
        hacer_consulta(query,'insert',variables)
        
    def editar_apodo(self,nuevo_apodo):
        query = "UPDATE MASCOTA SET APODO = :nuevo_apodo WHERE ID_MASCOTA = :id_mascota"
        variables = [nuevo_apodo,self.id_mascota]
        hacer_consulta(query,'update',variables)
        
        
    def eliminar_mascota(self):
        query = "DELETE MASCOTA WHERE ID_MASCOTA = :id"
        variables = [self.id_mascota]
        hacer_consulta(query,'update',variables)