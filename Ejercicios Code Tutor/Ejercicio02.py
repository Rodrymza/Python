imprimir_lista = lambda lista: print(*sorted(lista), sep= " ")

lista_numeros = input("Ingrese una serie de numeros separados por un espacio\n")

lista_enteros = (lista_numeros.split())
nuevalista = []
for elemento in lista_enteros:
    nuevalista.append(int(elemento))
print("Elementos ordenados:")
imprimir_lista(nuevalista)

lista_enteros = list(set(nuevalista))

print("Sin elementos repetidos:")
imprimir_lista(lista_enteros)

