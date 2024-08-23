#Ejercicio04
#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

print("Operaciones matematicas:")

num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))

suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
division=round(num1/num2,2)
resto=num1%num2

print("La suma de ambos numeros es:\n",  suma)
print("La resta de ambos numeros es:\n",  resta)
print("La multiplicacion de ambos numeros es:\n",  multiplicacion)
print("La divison de ambos numeros es:\n",  division)
print("El resto de", num1, "y", num2, "es: ",  resto)