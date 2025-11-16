#1 introducion a las clases en python

# las clases son plantillas para crear objetos. un objeto es una instancia de una clase

class Coche:
    
    #atributo de clase ( comparte todas las instancias)
    tipo = "vehicuo de cuatro ruedas"
    
    # metodo especial que es el que construye el objeto
    # se llama automaticamente este metodo cuando creas la instancia
    def __init__(self, marca, motor, color):
        self.marca = marca
        self.motor = motor
        self.color = color
        
    
    def arrancar(self):
        print("esta arrancando el coche")




Coche("toyota", "23.4", "rojo").arrancar()