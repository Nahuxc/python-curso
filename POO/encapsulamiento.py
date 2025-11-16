######## ENCAPSULAMIENTO ######

# sirve para poder entender la funcionalidad de un codigo
# proteger los elementos de una clase
# podemos hacer que el desarrollador no pueda acceder a ciertos datos del codigo

# private, public en algunos otros lenguajes


class Miclase:
    def __init__(self):
        
        #para asignar un atributo privado ponemos al principio del nombre un _ o sea 
        # self._nombreAtributo  / el desarrollador si puede acceder
        self._atributo_privado = "valor"
        
        #poner un atributo muy privado que ya no puede acceder se pone doble __nombreAtributo
        self.__atributo_mas_privado = "valor2"

objeto = Miclase()

#en otros lenguajes se estructura asi
#publico puede ser accedido de cualquier lugar
#protegido solo puede ser accedido desde su clase
#privado que no se puede acceder

print(objeto._atributo_privado)
print(objeto.__atributo_mas_privado) #tira error por que es un atributo privado



#el encapsulamiento sirve para ocultar cierta complejidad del uso de la clase y esto sirve para que podamos ocultar codigo que no debe tocarse


#para acceder a los datos encapsulados se utiliza getters y setters

#getters para obtener un atributo protegido o privado y setters para cambiar o establecer el valor de un atributo protegido o privado