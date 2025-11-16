###### HERENCIA SIMPLE #######


class Persona:
    def __init__(self, sexo, dni, ubicacion, nombre, edad):
        self.sexo = sexo
        self.dni = dni
        self.ubicacion = ubicacion
        self.nombre = nombre
        self.edad = edad

    def caminar(self):
        print("caminando...")

    def dejar_caminar(self):
        print("dejar de caminar")


#heredamos pasando por el parametro de la clase
class Estudiante(Persona):
    
    #le pasamos las propiedades anterior y le pasamos el super esas propiedades que herada
    def __init__(self, sexo, dni, ubicacion, nombre, edad, materias, curso, ):
        super().__init__(sexo, dni, ubicacion, nombre, edad) #aca las propieades de la clase anteior
        #aca declaramos las nuevas
        self.materias = materias
        self.curso = curso
        

class Empleado(Persona):

    def __init__(self, sexo, dni, ubicacion, nombre, edad, salario, trabajo):
        super().__init__(sexo, dni, ubicacion, nombre, edad)
        self.salario = salario
        self.trabajo = trabajo



def main():

    estudiante = Estudiante("M", 47159127, "mar del plata", "martin", 20, "analisis 1", "k3004")
    print(estudiante.nombre)
    print(estudiante.edad)
    print(estudiante.sexo)
    print(estudiante.dni)
    print(estudiante.ubicacion)
    print(estudiante.materias)
    print(estudiante.curso)



if (__name__ == "__main__"):
    main()