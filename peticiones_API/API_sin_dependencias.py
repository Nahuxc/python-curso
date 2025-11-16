# como hacer peticiones a APIs con python

#con y sin dependencias


#  ESTA ES LA FORMA DIFICIL

#1. sin dependencias
import urllib.request as request
import json

def main():

    #inicializar la variable para guardar la url de la api
    api_posts = "https://jsonplaceholder.typicode.com/posts/"

    try:
        #le indicamos que solo abra la url con urlopen
        response = request.urlopen(api_posts)
        data = response.read() #hasta ca podemos leer los datos pero no estan decodificados
        json_Data = json.loads(data.decode('UTF-8')) #con el loads cargamos los datos y luego con decode decodificamos para que python pueda interpratarlo

        print(json_Data)
        response.close() #importante cerrar la respuesta
    except request.error.URLError as e:
        print(f"error en la solicitud: {e}")



if __name__ == "__main__":
    main()