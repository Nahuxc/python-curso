#### ##### ABSTRACCION ##### ###

#funciona para ocultar la complejidad interna de un sistema

class Auto():
    def __init__(self):
        self.estado = "Apagado"

    def encender(self):
        self.estado = "encendido"
        print(f"el auto esta {self.estado}")

    def conducir(self):
        if(self.estado == "Apagado"):
            #aca tenemos abstraccion ya que el usuario no necesit encender el auto
            #ni tampoco sabe como funciona sino sabe que va a pasar y listo
            self.encender()
        print("conduciendo")

    def apagar(self):
        self.estado = "Apagado"
        print(f"el auto esta {self.estado}")



auto1 = Auto()

auto1.conducir()