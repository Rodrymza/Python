"""nombres=[]

for i in range(5):
    nombres.append(input("Ingresa un nombre: "))
nombre="Rodrigo"    
for i in range(5):
    if nombre.lower==str(nombres[i]).lower:
        print(i)
        
nombres=["rOdrIgo","roci"]
nombre="RODRIGO"
print(nombre.lower()==nombres[0].lower())

print(nombre.lower())
print(nombres[0].lower())"""

tamanio=int(input("Ingrese cantidad de numeros aleatorios que desea en el vector: "))
numeros=[]
import random
for i in range(tamanio):
    numeros.append(random.randint(0,100))
    print(f"Numero {i+1}: {numeros[i]}")


for i in range(tamanio):
    for j in range(i,tamanio):
        if numeros[j]<numeros[i]:
            aux=numeros[i]
            numeros[i]=numeros[j]
            numeros[j]=aux

for i in range(tamanio):
    print(numeros[i])
        