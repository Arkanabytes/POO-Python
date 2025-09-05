class Usuario:
    #metodo constructor
    def __init__(self,nombre,apellido,dni,telefono,email):
        self.__nombre= nombre
        self.__apellido= apellido
        self.__dni= dni
        self.__telefono= telefono
        self.__email= email
    
    #metodo str
    def __str__(self):
        return f"Nombre: {self.__nombre} - Apellido: {self.__apellido} - DNI: {self.__dni} - Telefono: {self.__telefono} - Email: {self.__email}"
    
    #Metodos Destructor
    def __del__(self):
        print (f"El usuario {self.__nombre} ha sido eliminado")
    
    # metodos get y set
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    def getTelefono(self):
        return self.__telefono
    def getEmail(self):
        return self.__email
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setApellido(self,apellido):
        self.__apellido = apellido
    def setDni(self,dni):
        self.__dni = dni
    def setTelefono(self,telefono):
        self.__telefono = telefono
    def setEmail(self,email):
        self.__email = email

usuario1 = Usuario("Alejandra","Diaz",12345678,987654321, "Alejandra@hotmail.com")
print(usuario1)
usuario1.setNombre("Pepita")
print(usuario1.getNombre())  
