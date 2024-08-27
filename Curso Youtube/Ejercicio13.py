#Generar matriz con valores de tipo entero desde teclado de manera automatizada
#especificar cantidad de filas y columnas
#Pedir valores que contendra la matriz elemento a elementos

filas=int(input("Ingrese la cantidad de filas para la matriz\n"))
columnas=int(input("Ingrese la cantidad de columnas para la matriz\n"))

matrix=[]
auxiliar = []

for i in range(filas):
    auxiliar=[]
    for j in range(columnas):
        auxiliar.append(input(f"Ingresa elemento {i+1}, {j+1}\n"))
    matrix.append(auxiliar)
print(matrix)
matrix
    
for filas in matrix:
    for elemento in filas:
        print(elemento, end=" ")
    print("")