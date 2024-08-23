""" Hacer un programa que inicialice un vector de números con valores aleatorios,
y posterior ordene los elementos de menor a mayor. """

import random

lista=[]
tamanio=10

for i in range(tamanio):
    lista.append(random.randint(0,50))
    print(f"{i+1} - {lista[i]}")
    
print("Ordenamiento: ")

for i in range(tamanio):
    for j in range(i,tamanio):
        if lista[j]<lista[i]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
            
[print(f"{i+1} - {lista[i]}") for i in range(tamanio)]

#se puede ejecutar un metodo for en una linea encerrandolo entre corchetes y cambiando la sintaxis

#con el metodo sort tambien podemos ordenar los numeros de menor a mayor y al reves con el metodo reverse

menoramayor=sorted(lista)
mayoramenor=sorted(lista,reverse=True)

print("De menor a mayor")
[print(f"{i+1} - {menoramayor[i]}") for i in range(tamanio)]
print("De mayor a menor")
[print(f"{i+1} - {mayoramenor[i]}") for i in range(tamanio)]

