""" Realizar un programa que defina un vector llamado “vector_numeros” de 10 enteros,
a continuación lo inicialice con valores aleatorios (del 1 al 10) y posteriormente
muestre en pantalla cada elemento del vector junto con su cuadrado y su cubo. """

import random
numeros=[]

#for i in range(10):
  #  numeros.append(random.randint(0,10))
  #  print(f"Lista {i+1}: {numeros[i]} - cuadrado: {numeros[i]**2} - cubo: {numeros[i]**3} ")

numeros = [random.randint(0,10) for _ in range(10)]

for elemento in numeros:
    print(f"Numero: {elemento} \n Cuadrado: {elemento**2} Cubo: {elemento**3}") 

