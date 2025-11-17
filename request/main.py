#importamos primero requests utilizando el comando en consola

# pip install requests

import requests



############ GET BASICO ##################

def get():
    #recomendable usar un try except para el manejo de errores
    try:
        #mandamos una consulta mediante requests.get()
        response = requests.get("https://jsonplaceholder.typicode.com/todos/") # le pasamos la url de la api


        #podemos pasar su status code para ver que nos devuelve con response.status_code
        print(response.status_code) #output: 200 si esta todo bien - 404 sino se pudo encontrar la url

        #de esta forma podemos sacar el diccionario de la url
        # print(response.json())

        # almacenamos lo traido del json
        lista_data = response.json()

        #recorremos la lista obtenida
        for data in lista_data:
            print(f"title: {data["title"]}") #obtenemos y manejamos datos como un diccionario


    except requests.exceptions.ConnectionError as e:
        print(f"hubo un error en: {e}")




########## QUERY PARAMS Y PATH PARAMS ##################


def get_queryParams(url, id, params):

    #primer forma para queryParamas
    response = requests.get(url, params=params)
    lista_data = response.json()

    #aca recorremos ya que daria una lista
    for data in lista_data:
        print(data["id"])
        print(data["title"])


    #otra forma seria por query params por url que solo devuelve un objeto en forma de diccionario
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{str(id)}") #le pamos directamtne por la url un parametro

    #al traernos solo un diccionario hacemos
    data = response.json()

    print(data["id"])
    print(data["title"])



############### POST ##################

def post_data():
    #estos van a ser lso datos a crear
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    #uso de headers que puedo verlos por postman
    headers ={
        "Content-type": "application/json"
    }

    #le pasamos por segundo parametro los datos a crear
    response = requests.post("https://jsonplaceholder.typicode.com/posts/", json=data, headers=headers)

    #poder ver los headers por codigo
    print(response.headers)

    #verificamos que todo este bien
    response_data = response.json()
    print(response.status_code)
    print(response_data)

    return response_data

############### HEADERS ##############


def main():

    url = "https://jsonplaceholder.typicode.com/posts/"

    #invocacion de funcion get basica
    # get()
    get_queryParams(url, 11, params= { "userId": 2, "id": 11})

    #metodo POST
    post_data()

if __name__ == "__main__":
    main()