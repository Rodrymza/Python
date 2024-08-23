"""Lista numeros pares
Crear una lista que contenga los numeros pares de 1 a 20 y luego eliminar los mayores a 10"""

lista=[]
lista_filtrada=[]
for i in range(1,21):
    if i%2==0:
        lista.append(i)
print("Lista numeros pares", lista)
print("Eliminando mayores a 10")

for i in lista:
    if i<=10:
        lista_filtrada.append(i)
  
lista=lista_filtrada
print("Mayores a 10 eliminados:", lista)
    