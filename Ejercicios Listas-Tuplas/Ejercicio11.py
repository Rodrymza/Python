"""Escribir una funcion llamada interseccion que reciba dos listas y devuelva una lista que contenga  los elementos que esten presentes
en ambas listas"""

def interseccion(lista_1,lista_2):
    interseccion=[]
    for i in lista_1:
        for j in lista_2:
            if i==j:
                interseccion.append(i)
    return interseccion
lista1=[1,2,3,4,5]
lista2=[4,5,6,7,8]

print(interseccion(lista1,lista2))
