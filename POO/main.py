### CLASES Y OBJETOS

#una clase es un tipo de objeto que nosotros podemos crear

class Celular:
    
    #atributos estaticos estas variables solo estaran dentro del objeto de la misma clase

    # propiedad1 = "valor 1"
    # propiedad2 = "valor 2"
    # propiedad3 = "valor 3"

    # marca = "samsung"
    # modelo = "483"
    # camara = "48MP"

    #cada vez que instanciamos la clase se ejecuta el metodo confutor __init__

    #self es hacer referncia a si mismo y esta funcion se ejecuta automaticamente
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara


    #METODOS EN OBJETOS / ES DAR ACCIONES A NUESTRO OBJETO, ES SOLO UNA FUNCION



    #se le pasa el parametro self para que entienda que hace refernecia al objeto
    def sonar_notificacion(self):
        print(f"!! llego una notificacion del {self.modelo} ¡¡") #asi podemos llamar a las variables declaradas

    def llamar(self): #importante poner el self siempre para poder autoreferenciarse
        print("estas llamando...")



#estructura inicial de mi proyecto
def main():

    #llamar al objeto / todos los objetos son una instancia para darle valores de objetos (instancia de clase = objeto)
    # celular1 = Celular()
    # celular2 = Celular()

    # otra forma
    # celular1 = Celular.modelo

    #forma de llamar un atributo
    # print(celular1.camara)





    #forma correcta de manejar atributos

    #el self va a ser lo que indica para asignar el valor enviado por parametro en el objeto
    celular1 = Celular("SAMSUNG", "S23", "48mp")
    celular2 = Celular("Apple", "2018", "20mp")

    #caracteristicas del celular traido y asignado por un objeto
    print(celular1.marca)
    print(celular1.modelo)
    print(celular1.camara)


    return



if __name__ == "__main__":
    main()