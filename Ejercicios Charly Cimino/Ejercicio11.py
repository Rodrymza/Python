""" Desarrollar un algoritmo que permita ingresar el nombre y la edad (por separado) de diferentes 
personas. La carga termina cuando en el nombre de la próxima persona se ingresa un asterisco (*). 
La computadora debe mostrar cómo se llama la persona más joven """

nombre=input("Ingrese nombre de la persona: ")
edadMenor=99
cont=0
while nombre!="*":
    edad=int(input(f"Ingrese edad de {nombre}: "))
    if edad<edadMenor:
        edadMenor=edad
        nombreMenor=nombre
    nombre=input("Ingrese nombre de proxima persona:")
    cont+=1
if cont>0:
    print(f"La persona mas joven es {nombreMenor}, con {edadMenor} años")
else:
    print("No se ingreso ningun nombre")