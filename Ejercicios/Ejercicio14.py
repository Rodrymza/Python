""" Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
Ejemplo, si se introduce 23 que muestre 32. """

#numero=input("Ingrese un numero a invertir: ")
numero="234"
nnum=""
for i in range(0,len(numero)):
    nnum=numero[i:i+1] + nnum
    
print(nnum)

print("Haremos lo mismo pero con una funcion matematica")

#numero=int(input("Ingresa un numero: "))
numero=43276
aux=numero
multiplo=1
nnum=0
while aux>10:
    aux=aux//10
    multiplo=multiplo*10

while numero>0:
    nnum=nnum+numero%10*multiplo
    numero=numero//10
    multiplo=multiplo//10
    
print(nnum)
    