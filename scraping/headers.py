######## personalizar el headers | user-agent ###############

import requests

url = "https://jsonplaceholder.typicode.com/posts"


#se inicializa como un diccionario
header = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

res = requests.get(url, headers= header)

print(res.status_code) #status_code devuelve el codigo de estado

print(res.reason)

print(res.ok)