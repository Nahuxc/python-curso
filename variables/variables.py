#tipos de datos y variables


#datos tipo STRING

nombre = "texto con comillas dobles "; #este es un tipo de dato string
apellido = 'texto con comillas simples'; #string con comillas simples

textoLargo = """ esto es un texto
en otra linea abajo
podemos usar multiples lineasa """; # string con comillas triples es similar a los backticks en js


#DATOS TIPO NUMERO   INT Y FLOAT

numero = 56; #este es un tipo de dato de Numero INT enteros
numero = 5.56; #este es un tipo de dato numero FLOAT flotantes o con coma


#DATOS TIPO BOOL

encendido = True; # es un tipo de valor verdedero que muestra  1
encendido = False; # es un tipo de valor falso que muestra 0


# uso de las variables en python

#operaciones aritmeticas
a = 32;
b = 42;

#suma
c = a + b; #output: 74

#suma con operador +=
c += a + b; #output: 74 += 32 + 42 esto es igual 74 += 74 = 148


print(c);

#multiplicacion
c = b * a;
print(c)

#resta
c = b - a;
print(c)


#division
c = b / a;
print(c)


#resto de una division %
c = b % a;
print(c);


#variables de string

nombre = "nahuel";
print(nombre);


#CONCATENAR CON f   y    +

#concatenar un string podemos concatenar con + y nombrar la variable en medio
bienvenida = "hola " + nombre + " bienvenido";

bienvenida2 = f"hola {nombre} bienvenido2 "; #esta es otra forma de concatenar y mas comoda se usa la f siempre al principio sino no va a tomar las llaves {}

print(bienvenida);

print(bienvenida2);





#algo a tener en cuenta cualquier dato que le mande y lo concatene asi

numero = 24;
texto = f"este es mi numero: {numero} ";


#el numero que se va a imprimir lo convierte a texto
print(texto);

#USO DE  "del" para eliminar memoria

# con " del " podemos hacer que una variable deje de estar definida

# del texto;

#es parecido a cuando haciamos lo del memory leak una vez usado podemos almacenarlo en algun lado y eliminarlo

#print(texto);

#esto devuelve error ya que dice que no esta definida por el " del "





#OPERADORES DE PERTENENCIA (IN / NOT IN)

print("este" in texto); #este in es como decirle "este" esta en la variable texto
# si esta devuelve true, sino esta da false

print("hola" not in texto) #este not in es como decirle "hola esta en la variable texto, sino esta devuelve true, si esta devuelve false"



#variable con camelCase

nombreCompletoDelUsuario = "marquitos293"; # se empieza con minuscula y cada palabra nueva arranca con mayuscula


#para python se utiliza snake_case es recomendado

nombre_completo_del_usuario = "marco3492";