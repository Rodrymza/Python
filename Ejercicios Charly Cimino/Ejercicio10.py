""" Desarrollar un algoritmo que permita ingresar un número natural. La computadora debe calcular y 
mostrar el factorial1 del número """

num=int(input("Ingrese el numero a calcular su factorial: "))
resultado=1
for i in range (1,num+1):
    resultado=resultado*i
    
print(f"El factorial de {num} es {resultado}")