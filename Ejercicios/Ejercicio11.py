""" Pide al usuario dos números y muestra la “distancia” entre ellos 
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo). """

print("Calculo de diferencia entre dos numeros")
num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))

diferencia=abs(num1-num2)

print("La diferencia entre ambos numeros es de", diferencia)