# Tenés una lista con puntajes [450, 1200, 999, 3000, 1500]
# Mostrá el mayor, el menor, el promedio (sum/len)
# Si el promedio es mayor que 1000 → “Buen rendimiento”
# Si está entre 500 y 1000 → “Regular”
# Si es menor → “Mal rendimiento”


lista_puntajes = [450,1200,999,3000,1500]

menor_puntaje = lista_puntajes[0]
mayor_puntaje = lista_puntajes[0]
todos_puntajes = 0

for puntaje in lista_puntajes:
    if puntaje > mayor_puntaje:
        mayor_puntaje = puntaje
    
    if puntaje < menor_puntaje:
        menor_puntaje = puntaje
    
    todos_puntajes += puntaje

promedio = todos_puntajes / len(lista_puntajes)

print(f"el mayor puntaje es: {mayor_puntaje}")
print(f"el menor puntaje es: {menor_puntaje}")
print(f"el promedio de puntajes: {promedio}")


if promedio > 1000:
    print("buen rendimiento")
elif promedio < 1000 and promedio > 500:
    print("regular")
else:
    print("mal rendimiento")
    
    
#con funciones de python   max()   min()  sum()  len()

puntajes = [450, 1200, 999, 3000, 1500]

mayor = max(puntajes)
menor = min(puntajes)
promedio = sum(puntajes) / len(puntajes)

print(f"Mayor: {mayor}, Menor: {menor}, Promedio: {promedio:.2f}")

if promedio > 1000:
    print("Buen rendimiento")
elif promedio >= 500:
    print("Regular")
else:
    print("Mal rendimiento")