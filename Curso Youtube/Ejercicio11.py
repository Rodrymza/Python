"""Programa que dada una lista se elimine un elemento dado por el usuario, no debe ser sensible a mayusculas y minusculas"""

lista_elementos=["A", "B", "b", "c", "E", "E", "f", "b", "a", "E"]
print("Lista de elementos", lista_elementos)
elemento_eliminar=input("Ingrese el elemento que desea eliminar \n")

while lista_elementos.count(elemento_eliminar.lower())>0 or lista_elementos.count(elemento_eliminar.upper())>0:
    if elemento_eliminar.lower() in lista_elementos:
        lista_elementos.remove(elemento_eliminar.lower())
    if elemento_eliminar.upper() in lista_elementos:
        lista_elementos.remove(elemento_eliminar.upper())
    
print(lista_elementos)

#Alternativa con bucle for

lista_elementos=["A", "B", "b", "c", "E", "E", "f", "b", "a", "E"]
print(lista_elementos)
elemento_eliminar=input("Ingrese el elemento que desea eliminar \n")

for caracter in lista_elementos:
    if elemento_eliminar.lower()==caracter:
        lista_elementos.remove(elemento_eliminar.lower())
    elif elemento_eliminar.upper()==caracter:
        lista_elementos.remove(elemento_eliminar.upper())
        
print(lista_elementos)
