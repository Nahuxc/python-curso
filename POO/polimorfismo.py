#polimorfismo es para que sepa como implementar dependiendo el tipo de objeto

# funcion hacer ruido pero cada tipo de animal va a hacer un ruido distinto
# perro = ladrar,  gato = maullar


class Gato():
    def sonido(self):
        print("miau")
        
class Perro():
    def sonido(self):
        print("ladrar")


#funcion
def hacer_sonido(animal):
    animal.sonido()



gato = Gato()

perro = Perro()

#seleccion por su tipo de objeto
gato.sonido()
perro.sonido()


#por llamado de funcion y diferencia por su objeto / esto es polimorfismo
hacer_sonido(gato)
hacer_sonido(perro)


#polimorfismo de herencia o de subclases, solo en lenguajes estaticos necesitamos hacer esto

""" 
#necesita heredar si o si para luego hacer esto

class Animal:
    def sonido(self):
        pass

class Gato(Animal): #hereda de animal
    def sonido(self):
        print("miau")

class Perro(Animal): #hereda de animal
    def sonido(self):
        print("ladrar")

#funcion fuera de la clase
def hacer_sonido(animal):
    animal.sonido()

#por llamado de funcion y diferencia por su objeto / esto es polimorfismo
hacer_sonido(gato)
hacer_sonido(perro)

"""

""" 
sobrecarga de metodos quiere decir que dependiendo el tipo de argumento y como se lo pase
se va a comportar el mismo metodo de distinta forma

class Animal:
    
    def sonido(self):
        pass

   def sonido(self, nombre):
        print("animal: {self.nombre}")
        
   def sonido(self, nombre, edad):
       pass


DUCK TYPING - ############ ESTUDIAR #############

TIPO REAL
TIPO DECLARADO

ENLACES DINAMICOS
ENLACES ESTATICOS


"""

