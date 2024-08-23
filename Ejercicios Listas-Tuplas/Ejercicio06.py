"""Crear una lista y sumar los elementos que la contienen"""
import random
lista=[]
for i in range(0,10):
    lista.append(random.randint(1,10))
print(lista)
suma=0
for i in lista:
    suma+=i
    
print("La suma de todos los elementos es", suma)
    