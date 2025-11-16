#herencia multiple y MRO

#imagina que estas modelando animales en un zoo. crear tres clases: "ANIMAL", "MAMIFERO", "AVE" . la clase ANIMAL debe tener METODO COMER. la clase MAMIFERO debe tener metodo AMAMANTAR y la clase AVE debe tener METODO VOLAR

#crear otra clase murcielago que herede mamifero y ave

#finalmente juega con el orden de herencia de la clase murcielago y observa como cambia el MRO y el comportamiento de sus metodos al usar super()

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"el animal {self.nombre} esta comiendo")




class Mamifero(Animal):
    def __init__(self, nombre):
        Animal.__init__(self, nombre )

    def amamantar(self):
        print(f" {self.nombre} esta amamantando")



class Ave(Animal):
    def __init__(self, nombre):
        Animal.__init__(self, nombre)

    def volar(self):
        print(f"{self.nombre} esta volando")


class Murcielago(Mamifero, Ave):
    def __init__(self, nombre):
        super().__init__(nombre)

def main():
    
    murcielago = Murcielago("Murcielago")
    
    murcielago.comer()
    murcielago.amamantar()
    murcielago.volar()
    
    ave = Ave("pajaro")
    
    ave.comer()
    ave.volar()
    
    #ver orden
    
    print(Murcielago.mro())
    

if __name__ == "__main__":
    main()