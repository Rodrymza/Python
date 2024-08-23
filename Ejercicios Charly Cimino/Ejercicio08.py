""" Desarrollar un algoritmo que permita ingresar un número entero entre 1 y 10 (inclusive). La 
computadora debe mostrar la tabla de multiplicar del número ingresado. """

num=int(input("Ingresa el numero del que quieres ver su tabla de multiplicar: "))

for i in range (1,11):
    print(f"{num}x{i}={i*num}")