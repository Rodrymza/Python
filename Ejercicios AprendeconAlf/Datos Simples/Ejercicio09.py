#Programa que pregunte al usuario una cantidad a invertir, el interes anual, los dias invertidos y el capital obtenido de la inversion

capital_inicial=int(input("Ingrese el capital a invertir \n"))

interes=int(input("Ingrese el interés anual \n"))

plazo=int(input("Ingrese la cantidad de dias de inversion \n"))

interes_generado=(interes/365)*plazo*capital_inicial/100

print("El total a retira es de $", interes_generado)