import requests

url = "https://jsonplaceholder.typicode.com/posts"

res = requests.get(url)

# print(dir(res))
""" output:
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url'] """

#print(res.reason)

print(res.request) #esto devuelve un objeto

print(res.request.headers) #aca podemos acceder a los headers de la peticion y estos headers son personalizables

print(res.request.url) #devuelve la url a la que solicitamos

print(res.request.path_url) #mandaria el recurso al que quermos acceder mediante la url

##### atributos de la respuesta ############

print(res.cookies) #devuelve un objeto de requestcookie

print(res.headers) #acceder a los headers de la respuesta

print(res.history) # muestra las redirecciones

###### 3 formas distintas de poder acceder al cuerpo ######

#1er forma
print(res.content) #para poder acceder al body de la respuesta en bytes
print(type(res.content))

#2da forma
print(res.text) # esto nos lo devuelve en string
print(type(res.text))

#3ra forma
print(res.json()) #nos devuelve el cuerpo de la repsuesta en formato json