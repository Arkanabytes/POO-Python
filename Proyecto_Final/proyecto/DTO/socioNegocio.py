class SocioNegocio:
    def __init__(self, run, nom, ape, direc, fono, correo):
        self.__run = run
        self.__nombre = nom
        self.__apellido = ape
        self.__direccion = direc
        self.__fono = fono
        self.__correo = correo

    # Getters
    def get_run(self):
        return self.__run

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_direccion(self):
        return self.__direccion

    def get_fono(self):
        return self.__fono

    def get_correo(self):
        return self.__correo

    # Setters
    def set_run(self, run):
        self.__run = run

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_fono(self, fono):
        self.__fono = fono

    def set_correo(self, correo):
        self.__correo = correo