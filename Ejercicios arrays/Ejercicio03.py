""" Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor. """

notas=[]
cantidadNotas=5
notamax=10
notamin=1
total=0
notamenor=10
notamayor=0

for i in range(cantidadNotas):
    notain=int(input(f"Ingrese la nota {i+1}: \n"))
    total+=notain
    if notain<notamenor:
        notamenor=notain
    if notain>notamayor:
        notamayor=notain 
    notas.append(notain)
promedio=round(total/cantidadNotas,2)

print("Notas obtenidas: ")
for i in range(cantidadNotas):
    print(f"Nota {i+1}: {notas[i]}")
    
print(f"Promedio obtenido: {promedio}")
print(f"Mayor nota obtenida: {notamayor}")    
print(f"Menor nota obtenida: {notamenor}")    