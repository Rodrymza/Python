#Ejercicio02
#Calcular perimetro y area de un rectangulo dada su base y altura

base=0
altura=0
perimetro=0
area=0

print("Vamos a calcluar el area y perimetro de un rectangulo")
base=float(input("Ingrese base del rectangulo: "))
altura=float(input("Ingrese altura del rectangulo: "))

perimetro=base*2+altura*2
area=base*altura

print("El perimetro del rectangulo es de", round(perimetro,2))
print("El aerea del rectangulo es de", round(area,2))

print("Fin del programa")


