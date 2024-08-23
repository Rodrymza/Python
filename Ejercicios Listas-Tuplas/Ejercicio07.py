"""Crear una funcion que elimine los elementos duplcados de una lista, y devuelva la lista nueva sin elementos duplicados"""

def eliminar_duplicados(lista):
    for i in lista:
        while lista.count(i)>1:
            lista.remove(i)
    lista.sort()
    return lista


lista_original=[1,2,2,3,4,4,5,1,6]
eliminar_duplicados(lista_original)
print(lista_original)
nuevalista=[]
nuevalista=eliminar_duplicados([2,2,3,5,7,7,1])
print(nuevalista)