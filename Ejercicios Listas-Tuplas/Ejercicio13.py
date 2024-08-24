"""Sumar los elementos consecutivos de una matriz"""
def sumar_matriz(matriz):
    suma=0
    for sublista in matriz:
        for i in sublista:
            suma+=i
    print(suma)
matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

sumar_matriz(matriz)