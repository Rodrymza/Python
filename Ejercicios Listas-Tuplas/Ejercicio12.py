"""Trasponer una matriz, es decir intercambiar filas por columnas"""
def trasponer_matriz(matriz):
    aux=[]
    traspuesta=[]
    for j in range(0,len(matriz)):
        for i in range(0,len(matriz)):
            aux.append(matriz[i][j])
        traspuesta.append(aux)
        aux=[]
    return traspuesta

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(trasponer_matriz(matriz))