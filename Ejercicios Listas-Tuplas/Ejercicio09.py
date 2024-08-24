"""Desarrollar una funcion que rote las posiciones de una lista un numero n de posiciones dadas por el usuario"""

def rotar_lista(lista, num):
   nueva_lista=lista[num+1:len(lista)]+lista[0:num+1]
   return nueva_lista

lista=[1,2,3,4,5]
lista_rotada=rotar_lista(lista,2)
print(lista_rotada)