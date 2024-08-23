#Ejercicio06
#Calcular la media de 3 numeros pedidos al usuario
cont=0
suma=0
cont=0
while cont!=3:
    num=float(input("Ingrese un numero: "))
    suma=suma+num
    cont=cont+1

promedio=round(suma/3,2)

print("El promedio de los numeros ingresados es de", promedio)