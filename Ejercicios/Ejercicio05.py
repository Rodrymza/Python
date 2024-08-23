#Ejercicio05
#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
#Recordar que la fórmula para la conversión es:
#C = (F-32)*5/9

print("Convertir Farenheit a Celsuis")

far=float(input("Ingresa la temperatura en Farenheit"))
cel=round((far-32)*(5/9),1)

print("La temperatura en Celsius es de:", cel)