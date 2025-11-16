def frase(nombre, apellido, adjetivo):
    return f"frase {nombre} apellido: {apellido} , adjetivo {adjetivo}"

#podemos agregar paramtros sin seguir el orden siempre y cuando los asignmeos de esta forma
texto = frase(apellido= "martinez", adjetivo="feo", nombre="martin")
print(texto)




#tambien tenemos este caso

def frase(nombre, apellido, adjetivo = "feo"):
    return f"frase {nombre} apellido: {apellido} , adjetivo {adjetivo}"


frase("martin", "gimenez") #no hace falta que pongamos adjetivo porque ya tiene un parametro forzado es decir ahora se transforma a opcional, siendo que tiene feo por defecto el valor

#podemos poner asi si queremos cambiarlo frase("martin", "gimenez", "tonto") y ahi se cambiaria