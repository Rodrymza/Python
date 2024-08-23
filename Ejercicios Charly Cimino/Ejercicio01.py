""" Programa que calcule la edad del usuario """

anioactual=2024
mesactual=5
diaactual=23

diaingresado=int(input("Ingresa dia de nacimiento: "))
mesingresado=int(input("Ingresa mes de nacimiento: "))
anioingresado=int(input("Ingresa año de nacimiento: "))

edad=anioactual-anioingresado-1

if mesactual>mesingresado:
    edad+=1
elif mesactual==mesingresado:
    if diaactual>=diaingresado:
        edad=edad+1

print("Tienes",edad, "años")