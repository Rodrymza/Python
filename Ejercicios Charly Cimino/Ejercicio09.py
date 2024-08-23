""" Desarrollar un algoritmo que permita ingresar una cantidad de personas. La computadora debe 
pedir la edad de cada una y finalmente mostrar el porcentaje de personas que es mayor de edad. """

personas=int(input("Ingrese la cantidad de personas: "))
mayores=0
while personas<=0:
    personas=int(input("Ingrese un numero mayor a cero. Ingrese la cantidad de personas: "))
    
for i in range (personas):
    edad=int(input(f"Ingrese edad de la persona {i+1}: "))
    while edad<1 or edad>99:
        edad=int(input("Ingrese una edad valida: "))
    
    if edad>=18:
        mayores +=1 
        
promedio=round((mayores/personas)*100)

print(f"Se ingreso un total de {personas} personas")
print(f"El total de personas mayores de edad es de {mayores}, que representa el {promedio}% del total")   
    