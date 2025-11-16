# GETTERS Y SETTERS VIENEN DESDE EL TEMA DE ENCAPSULAMIENTO

#Son formas de acceder y establecer atributos con manejo de datos privados o protegidos


class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.__edad = edad

    #obtenre nombre    con atributo protegido
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

    def get_nombre(self):
        return self._nombre


    #obtener edad con atributo privado

    def get__edad(self):
        return self.__edad

    def set__edad(self, new_edad):
        self.__edad = new_edad


def main():

    persona1 = Persona("nahuel", 24)

    #devuelve el nombre a traves de la funcion para obtener el dato de propiead privada en este caso protegida
    nombre = persona1.get_nombre()
    print(nombre)


    #uso del set
    persona1.set_nombre("jorge")

    #uso del get
    nombre = persona1.get_nombre()
    print(f"cambiado por un setter {nombre}")


    #atributo privado forma de acceder

    edad = persona1.get__edad()
    print(edad)

    #seterrs
    persona1.set__edad(56)


    #geters denuevo
    edad = persona1.get__edad()
    print(f"cambiado por un setter {edad}")



if __name__ == "__main__":
    main()