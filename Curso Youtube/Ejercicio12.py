"""Programa que debe eliminar el primer y ultimo elemento de la lista
se desconocen los elementos de la lista
crear otras dos listas, la de los elementos que no fueron eliminados y la lista de los que fueron eliminados"""

lista_numeros = [1, 2, 3, 4, 5,6 ,7, 8]

lista_eliminados =[]
lista_conservados =[]

print(lista_numeros)

lista_eliminados.append(lista_numeros.pop(0))
lista_eliminados.append(lista_numeros.pop()) #por defecto el metodo pop elimina el ultimo elemento

lista_conservados=lista_numeros.copy()
print("Elementos eliminados: ", lista_eliminados)
print("Elementos conservados: ", lista_conservados)
