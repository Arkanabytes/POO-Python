class Libro:
    #metodo constructor
    def __init__(self,nombre,genero,isbn,autor,estado=False):
        self.__nombre= nombre
        self.__genero= genero
        self.__isbn= isbn
        self.__autor= autor
        self.__estado= estado
    
    #metodo str
    def __str__(self):
        return f"Nombre: {self.__nombre} - Genero: {self.__genero} - ISBN: {self.__isbn} - Autor: {self.__autor} - Estado: {self.__estado}"
    #Metodos Destructor
    def __del__(self):
        print (f"El libro {self.__nombre} ha sido eliminado")

    # metodos get y set
    def getNombre(self):
        return self.__nombre
    def getGenero(self):
        return self.__genero
    def getIsbn(self):
        return self.__isbn
    def getAutor(self):
        return self.__autor
    def getEstado(self):
        return self.__estado
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setAutor(self,autor):
        self.__autor = autor
    def setGenero(self,genero):
        self.__genero = genero
    def setIsbn(self,isbn):
        self.__isbn = isbn
    def setEstado(self,estado):
        self.__estado = estado
        

it = Libro("IT","Terror",12312411124,"Stiphen King")
print(it)
it.setAutor("Stephen King")
print(it.getAutor())

