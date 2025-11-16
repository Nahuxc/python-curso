# METODO DE RESOLUCION DE ORDEN (MRO) #

#como da las prioridades el MRO las clases

# hace referencia al orden de como toma los metodos y las clases

# -  se centra en la prioridad de orden



class A:
    def hablar(self):
        print("hola A")
class B(A):
    def hablar(self):
        print("hola B")
class C(A):
    def hablar(self):
        print("hola c")
class D(B, C): #como la primer clase que herede es B entonces va a B luego  C y por ultimo A
    
    #sino estuviera el metodo en D
    def hablar(self):
         print("hola D")

d = D()

d.hablar() #le da prioporidad a d si es que esta

print(D.mro()) #para ver como se va a ejecutando


#para llamar desde alguna clase como quisieramos hariamos

llamar_b_desde_d = B.hablar(d) #es decir le pasamos el objeto D 
