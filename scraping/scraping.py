import requests

#doc oficial https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

def main():

    url = "https://www.accuweather.com"
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }

    res = requests.get(url, headers=headers)
    print(res.status_code) # si da 200 todo funciona
    #print(res.text)

    #apartir de aca empezamos a usar beauti
    soup = BeautifulSoup(res.text, "html.parser") #devuelve una estructura de objetos python con los datos del html

    # print(soup.title) # devuelve el titulo que aparece en la pestaña, basicamente lo llamo por etiqueta

    #para que devuelva solo el texto
    # print(soup.title.text)

    ############ utilizando los selectores css ###########
    # ejemplo: <etiqueta>.<class>

    elemento = soup.find("a", class_="recent-location-item featured-location")

    #algo a tener en cuenta trayendo todo asi sin modificar viene con espacios textos de mas etc
    # print(elemento.text)
    
    #para poder limpiar el string
    elemento_limpio = elemento.text.strip() #strip funcion de cadena de texto
    #print(elemento_limpio)
    
    # OTRA FORMA
    # Eliminar saltos de línea y dejar todo en una sola línea, en caso de que venga con muchos br y span
    elemento_sin_saltos = elemento.get_text(separator=" ", strip=True)
    print(elemento_sin_saltos)
    
    

if __name__ == "__main__":
    main()