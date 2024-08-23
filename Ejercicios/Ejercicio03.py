#Ejercicio03
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cat1=0
cat2=0
hip=0

#Teorema de Pitagoras hip=(cat1**2+cat2**2)

print("Calcularemos la hipotenusa de un triangulo rectangulo")
cat1=float(input("Ingresa el valor del primer cateto: "))
cat2=float(input("Ingresa el valor del segundo cateto: "))

hip=round((cat1**2+cat2**2)**1/2,2)

print("La hipotenusa del triangulo es de", hip)