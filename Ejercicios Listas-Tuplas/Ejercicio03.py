"""Sumar dos listas"""

lista_1=[1,2,3]
lista_2=[4,5,6]

nuevalista=lista_1+lista_2

print(nuevalista)

#Metodo append:
lista_1.append(lista_2)
print(lista_1)
#con este metodo se obtiene un resultado diferente, ya que se dentro de la lista_1, en la posicion 3 se coloca la lista_2
#[1, 2, 3, [4, 5, 6]]