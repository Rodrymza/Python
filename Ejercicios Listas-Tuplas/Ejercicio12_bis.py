"""Trasponer una matriz, es decir intercambiar filas por columnas"""
def trasponer_matriz(matriz):
    traspuesta=[]
    for i in range(len(matriz[0])): #se itera en el rango de la cantida de elementos que tienen las sublistas de la matriz
        aux=[]
        for fila in matriz:         #se van agregando los elementos 'i' de cada sublista, trasponiendo asi la matriz
            aux.append(fila[i])
        traspuesta.append(aux)
    print(traspuesta)
    
matriz=[[1,2,3,4],
        [4,5,6,5],
        [7,8,9,6]]
trasponer_matriz(matriz)