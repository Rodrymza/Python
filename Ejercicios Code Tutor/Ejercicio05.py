from random import randint
lista_numeros = []
for _ in range(10):
    lista_numeros.append(randint(0,10))

tupla_numeros = tuple(lista_numeros)
set_numeros = set(lista_numeros)

claves = ["lista", "tupla", "set"]
valores = [lista_numeros, tupla_numeros, set_numeros]
diccionario = {}

for i in range(len(claves)):
    diccionario[claves[i]] = valores[i]

print(diccionario)