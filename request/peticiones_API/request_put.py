# con dependencias (REQUEST)

#instarlo con pip install requests

import requests

def main():
    #pasarle el id por la url para saber cual va cambiar
    id = 1
    api_post = f"https://jsonplaceholder.typicode.com/posts/{id}"
    print("\nPUT: ")
    try:
        response = requests.put(api_post, json={
            "title": "jorge espinozon",
            "body" : "dev",
            "userId" : 1,
        })
        print(response.status_code)
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"error en la solicitud: {e}")

    #el patch es para cambiar solo 1 o mas atributos
    #el put requiere de llamar a todos y que todos se actualizen sea con los mismos datos
    #pero lo requiere esa es la diferencia con el patch que ahi solo podes cambiar un valor
    #sin necesidad de llamar a los otros



if __name__ == "__main__":
    main()