print("Verifica si aprobaste o no")
print("Ingresa tu nombre")
nombre=input()
suma=0
cont=0

materias=4
while cont<materias:
    cont=cont+1
    if cont==1:
        mat="Matematica"
    elif cont==2:
        mat="Lengua"
    elif cont==3:
        mat="Historia"
    else:
        mat="Geografia"
    
    print("Ingresa la nota de " + mat)
    nota=int(input())
    suma=suma+nota
    if nota>5:
        print("Aprobaste", mat)
    else:
        print("Desaprobaste", mat)


promedio=suma/materias

print(nombre,"el promedio general es de", promedio)

if promedio<6:
    print("Desaprobaste el curso")
elif promedio<7:
    print("Aprobaste de pedo")
else:
    print("Aprobaste!!")