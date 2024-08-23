"""Determinar el numero mas grande entre tres numeros pedidos al usuario"""

numeros=[]
for i in range(3):
    numeros.append(int(input("Ingrese un numero: ")))
may=numeros[0]
for num in numeros:
    if num>may:
        may=num

print(f"El numero mayor es {may}")
