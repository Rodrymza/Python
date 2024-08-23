"""Programa que solicite un numero entero al usuario y determine si es par o impar"""

numero=int(input("Ingrese un numero para determinar si es par o impar: "))
if numero%2==0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")
    