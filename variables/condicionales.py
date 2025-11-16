#CONDICIONALES   if   else

a = 423;
b = 423;

print("==============condicion 1===================")

if a != b : # a = 23  b = 423   =  True
    print("esto es verdadero a es distinto de b")
else : # a = 23   b = 23        =  False
    print("a no es distinto de b entonces es falso")


print("=========condicion 2===========")

edad_usuario = 5

if edad_usuario >= 18 :
    print("sos mayor de 18")
else :
    print("sos menor de 18")


print("=========condicion 3===========")

lampara_interruptor = False

if lampara_interruptor == True :
    print("la lampara esta encendida")
else :
    print("esta apagada")


#condicion con else if   o como se escribe en python elif

ingreso_mensual = 25

print("=========condicion 4 Elif===========")

if ingreso_mensual > 100 :
    print("esta bien economicamente")
elif ingreso_mensual > 50 : #elif es como else if
    print("estas en nivel medio economicamente")
else :
    print("sos pobre")
    
    
    
#condicional con operadores logicos



usuario = "jorge"
ingreso_mensual = 105

print("=========condicion 5 OP logicos===========")

if (ingreso_mensual > 100) & (usuario == "jorge") :
    print("sos jorge y sos de sueldo alto")
else :
    print("sos pobre y no sos jorge")