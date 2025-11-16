###### HERENCIA MULTIPLE #######


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


class Estudiante(Persona):
    
    def __init__(self, sexo, dni, ubicacion, nombre, edad, materias, curso):
        
        # ❌ CAMBIO 1: QUITAMOS super() porque rompe con herencia múltiple
        # super().__init__(sexo, dni, ubicacion, nombre, edad)

        # ✔️ USAMOS Persona DIRECTAMENTE
        Persona.__init__(self, sexo, dni, ubicacion, nombre, edad)

        self.materias = materias
        self.curso = curso
        
    def estudiar(self):
        print("estudiar")


class Empleado(Persona):

    def __init__(self, sexo, dni, ubicacion, nombre, edad, salario, trabajo):

        # ❌ CAMBIO 2: QUITAMOS super() porque pide parámetros que Estudiante no tiene
        # super().__init__(sexo, dni, ubicacion, nombre, edad)

        # ✔️ USAMOS Persona DIRECTAMENTE
        Persona.__init__(self, sexo, dni, ubicacion, nombre, edad)

        self.salario = salario
        self.trabajo = trabajo

    def trabajar(self):
        print("trabajar")


# ✔️ Mantener este orden es correcto para evitar errores de MRO
class Estudiante_trabajador(Empleado, Estudiante): #ENTRA COMO EMPLEADO -> ESTUDIANTE -> PERSONA

    def __init__(self, sexo, dni, ubicacion, nombre, edad, materias, curso, salario, trabajo):

        # ❗ IMPORTANTE:
        # Inicializamos Persona UNA sola vez
        Persona.__init__(self, sexo, dni, ubicacion, nombre, edad)

        # Luego inicializamos las partes específicas
        Estudiante.__init__(self, sexo, dni, ubicacion, nombre, edad, materias, curso)
        Empleado.__init__(self, sexo, dni, ubicacion, nombre, edad, salario, trabajo)


def main():

    estudiante = Estudiante("M", 47159127, "mar del plata", "martin", 20, "analisis 1", "k3004")
    print(estudiante.nombre)
    print(estudiante.edad)
    print(estudiante.sexo)
    print(estudiante.dni)
    print(estudiante.ubicacion)
    print(estudiante.materias)
    print(estudiante.curso)

    estudiante_Trabaja = Estudiante_trabajador(
        "M", 47159127, "mar del plata", "martin", 
        20, "analisis 1", "k3004", 2500, "programador"
    )
    
    estudiante_Trabaja.estudiar()
    estudiante_Trabaja.trabajar()
    estudiante_Trabaja.caminar()
    estudiante_Trabaja.dejar_caminar()

    #como saber de donde hereda
    
    herencia = issubclass(Estudiante_trabajador, Estudiante) #trabajador hereda de estudiante
    print(herencia)
    
    instancia = isinstance(estudiante_Trabaja, Estudiante_trabajador) #va a dewvolver true siempre que traiga datos de alguno que esta heredando
    print(instancia)
    
    instancia2 = isinstance(estudiante, Empleado) #aca por ejemplo no hereda nada de empleado entonces es false
    print(instancia2)


if __name__ == "__main__":
    main()