"""Programa que invierta una cadena de caracteres ingresada por el usuario"""

cadena=input("Ingresa una palabra a invertir\n")
cadena_invertida=cadena[::-1]
print("La palabra invertida es", cadena_invertida)
cadena_invertida=""
for i in cadena:
    cadena_invertida=i+cadena_invertida
    
print("La palabra invertida es", cadena_invertida)