###### CLASES ABSTRACTAS ######

#tiene la funcion de crear una plantilla

from abc import ABC, abstractmethod#esto es un decorador

#un metodo abstracto es un metodo que esta creado pero no esta implementado

#obliga a que lo que este en la plantilla debe estar en las otras clases
#si es que tiene abstractmethod

#PLANTILLA QUE NOS PERMITE CREAR PERSONAS
class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, sexo, edad, actividad):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"hola me llamo: {self.nombre} y tengo {self.edad} años")



class Estudiante(Persona):
    def __init__(self, nombre, sexo, edad, actividad):
        super().__init__(nombre, sexo, edad, actividad)
    
    #la abstraccion nos pide si o si crear la funcion abstracta para poder usarla
    def hacer_actividad(self):
        return f"estoy haciendo esta actividad: {self.actividad}"

class Trabajador(Persona):
    def __init__(self, nombre, sexo, edad, actividad):
        super().__init__(nombre, sexo, edad, actividad)
    
    #la abstraccion nos pide si o si crear la funcion abstracta para poder usarla
    def hacer_actividad(self):
        return f"actualmente trabajo en el rubro: {self.actividad}"


def main():
    
    #si hay metodo abstracto no se puede crear la clase porque es una clase abstracta
    #en caso de sacar el ABC que heredo si se podria usar
    
    dalto = Estudiante("dalto", "masculino", 23, "programando")
    pedro = Trabajador("pedro", "masculino", 34, "basurero")
    
    #aca se pone en practica la abstraccion que tenemos 2 clases distintas
    #donde cambia su actividad y es obligatorio que ambos hagan una actividad
    #cambia que uno hace una actividad de cierta forma
    
    #de la primer clase estudiante
    dalto.presentarse()
    print(dalto.hacer_actividad())
    
    #de la segunda clase Trabajador
    pedro.presentarse()
    print(pedro.hacer_actividad())
    
    pass

if __name__ == "__main__":
    main()