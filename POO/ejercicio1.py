#primer ejercicio POO

class Estudiante:
    
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print("estoy estudiando")
    
    


def main():
    
    nombre = input("ingresa tu nombre: ")
    edad = int(input("ingresa tu edad: "))
    grado = int(input("ingresa tu grado: "))

    estudiante = Estudiante(nombre, edad, grado)

    print(f""" 
el estudiante se llama: {estudiante.nombre}
su edad: {estudiante.edad}
grado: {estudiante.grado}
          """)


    while True:
        seleccion = input("queres estudiar? si o no ")
        if (seleccion.lower() == "si"):
            estudiante.estudiar()
            break



if (__name__ == "__main__"):
    main()