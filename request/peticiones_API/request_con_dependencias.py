# con dependencias (REQUEST)

#instarlo con pip install requests

import requests

def main():
    api_post = "https://jsonplaceholder.typicode.com/posts/"
    try:
        response = requests.get(api_post)
        #con esto ya podemos acceder a cualquier elemento
        json = response.json()

        #ejemplo de acceder al elemento 1
        print(json[0])

        #dentro de esta libreria tambien podemos usar
        #POST
        #PUT
        #PATCH
        #DELETE

    except requests.JSONDecodeError as e:
        print(f"error: {e}")





    #EJEMPLO DE UN POST
    #utilizo la variable anterior de la URL

    objeto_gurdar = { #ejemplo para el primer response comentado pasarlo como variable al json=
        "title": "jorge espinozon",
        "body" : "dev",
        "userId" : 5
    }

    #podemos pasarlo asi
    print("\n POST: ")
    # response = requests.post(api_post, json= objeto_gurdar)

    try:
        # sino de esta otra forma , ambas son correctas
        response = requests.post(api_post, json= {
            "title": "jorge es",
            "body" : "devebo",
            "userId" : 6
        })


        print(response.json()) #mostramos el post que se hizo

        #Poder ver estado en el que se encuentra la peticion  response.status_code
        print(response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"error en la solicitud: {e}")







if __name__ == "__main__":
    main()