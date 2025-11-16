### TRABAJANDO CON FECHA Y HORAS EN PYTHON ###

#importar el modulo datetime y de ahi sacamos datetime , timedelta, timezone

from datetime import datetime, timedelta, timezone

import locale #para configurar la fecha

#obtener fecha hora actual
now = datetime.now()
print(f"fecha y hora actual: {now} ")


# 2. crear una fecha y hora especifica

fecha_especifica = datetime(2025, 1, 12) #AAAAMMDD y luego se le puede poner la informacion de zona horaria o minutos o segundos
print(fecha_especifica)


#3. formatear fechas 
#metodo strftime() para formatear fecha
#ir a la documentacion para saber mas de datetime python

#pasarle el objeto datetime y el formato especificado
#formato:
formato_de_fecha = now.strftime("%d/%m/%Y  hs: %H:%M:%S")
print(f"fecha formateada: {formato_de_fecha}")


#4. operaciones con fechas(sumar/restar dias, minutos, horas, meses)

# se usa el timedelta

ayer = datetime.now() - timedelta(days=1)
print(f"Ayer: {ayer}")

mañana = datetime.now() + timedelta(days= 1)
print(f"mañana: {mañana}")




#obtener los componentes individuales de la fecha

#primero hay que crear un objeto con el datetime seria esto ej:  now = datetime.now()

año = now.year
mes = now.month
dia = now.day

print(f" año:{año}  mes:{mes}   dia:{dia}")


#calcular 2 fechas

dia1 = datetime.now()
dia2 = datetime(2025, 2 , 12)
diferencia = dia1 - dia2

print(f"esta es la diferencia: {diferencia}")


#fechas en otro idioma
# usar la libreria locale