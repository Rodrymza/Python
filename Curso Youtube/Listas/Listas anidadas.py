#listas dentro de otras listas
#se puede almacenar una lista dentro de otra lista, ocupando el indice de la lista principal

lista_principal=["a","b"]
lista_anidada=[1,2,3,4,5]

lista_principal.append(lista_anidada)

print(lista_principal)          #la lista principal muestra los elementos, entre ellos la lista anidada
print(lista_principal[2])       #especificando el indice vemos los la lista ubicada en ese indice
print(lista_principal[2][2])    #podemos indicar los dos indices para indicar el elemento espefifico dentro de la lista anidada

#los adinamientos en las listas pueden ser en muchos grados, a la lista anidada podriamos asignarle otra lista mas dentro