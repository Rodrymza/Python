"""Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
Dicha calificación se compone de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final."""

nombre=input("Ingrese nombre del alumno: ")
promParciales=0.55
promFinal=0.30
promTrabajo=0.15
totalNotas=3
cont=1
total=0

while cont<=3:
    print("Parcial", cont)
    parcial=float(input("Ingrese la nota: "))
    cont=cont+1
    total=total+parcial

parciales=total/totalNotas

final=float(input("Ingrese nota del Final: "))
trabajo=float(input("Ingrese nota del Trabajo final: "))

notaFinal=round(parciales*promParciales+trabajo*promTrabajo+final*promFinal,2)

print("Alumno:", nombre)
print("Promedio Notas Parciales:",parciales)
print("Nota Trabajo Final:", trabajo)
print("Nota Examen Final:", final)
print("Nota Final:", notaFinal)

if notaFinal>=6:
    print("Alumno APROBADO")
else:
    print("Alumno DESAPROBADO")
