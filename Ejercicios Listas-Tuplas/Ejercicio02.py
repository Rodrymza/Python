"""Crear una lista que contenga los elementos del 1 al 10 y luego convertirla para que contenga los numeros invertidos"""
lista=[]

for i in range(1,11):
    lista.append(i)
print("Lista de numeros", lista)
lista_invertida=[]
for i in lista:
    lista_invertida.insert(0,i)
    
print("La lista invertida es", lista_invertida)