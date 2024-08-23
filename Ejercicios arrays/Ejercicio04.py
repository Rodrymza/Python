""" Programa que declare un vector de diez elementos enteros y pida números para rellenarlo 
hasta que se llene el vector o se introduzca un número negativo.
Entonces se debe imprimir el vector (sólo los elementos introducidos). """

lista=[]
num=0

print("Para finalizar ingrese un numero negativo")
while num>=0:
    
    num=int(input("Ingrese un numero: "))
    if num>=0: lista.append(num)

for i in range(len(lista)): print(lista[i])