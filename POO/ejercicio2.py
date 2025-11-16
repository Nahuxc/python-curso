#crear sistema para la escuela
#van a haber 2 clases principales PERSONA Y ESTUDIANTE

#la clase PERSONA: tendra atributos NOMBRE Y EDAD y un METODO que imprima el nombre y la edad de la persona.

#la clase ESTUDIANTE: heredara de la clase PERSONA y tambien tendra un atributo adicional GRADO y un metodo que imprima el GRADO del estudiante

#deberas utilizar super en el metodo de inicializacion init para reutilizar el codigo de la clase padre PERSONA . luego crear una instancia de la clase estudiante e imprime sus atributos y utiliza sus metodos para asegurarte que todo funcione


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def datos_persona(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f"el grado del estudiante es: {self.grado}")

def main():
    
    #datos del estudiante
    
    estudiante = Estudiante("martin", 23, 5)
    estudiante.datos_persona()
    estudiante.mostrar_grado()



if __name__ == "__main__":
    main()