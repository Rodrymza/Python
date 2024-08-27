#lista anidada que contiene filas y columnas (como una tabla)
#puede tener cualquier cantida de columnas y filas
#columnas verticales y filas horizontales

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]] #columnas y filas

print(matrix)

print(matrix[1][1])

#recorrer elementos en un ciclo for

print("Recorriendo elementos de la matriz")
for filas in matrix:
    for elemento in filas:
        print(elemento, end= " ")       #esto imprime la matriz en formato de filas y columnas
    print("")
    
