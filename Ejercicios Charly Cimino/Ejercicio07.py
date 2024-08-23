""" Desarrollar un algoritmo que permita ingresar un número entero positivo. La computadora debe 
mostrar la sucesión de números pares desde el número ingresado hasta el cero (inclusive), en una 
sola línea:
 """
 
num=int(input("Ingresa un numero para realizar la marcha atras :"))
while num<=0:
    num=int(input("Ingresa un numero mayor a 0"))
    
for i in range (num,-1,-1):
    if i%2==0:
        print (i, end=" ")


 
 