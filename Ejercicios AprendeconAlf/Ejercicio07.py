#programa que mida indice de masa corporal

peso=int(input("Ingrese su peso en kg \n"))
altura=int(input("Ingrese su altura en cm \n"))

imc=peso/(altura/100)**2
print("El indice de masa corporal es de", round(imc,2))
