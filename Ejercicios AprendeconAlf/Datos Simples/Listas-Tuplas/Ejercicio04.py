#Loteria primitiva
from random import randint
def sorteo(cantidad):
    numeros_sorteados = []
    for _ in range(cantidad):
        numero = randint(1,100)
        if not numero in numeros_sorteados:
            numeros_sorteados.append(numero)
    
    return numeros_sorteados

lista_sorteo = sorteo(10)
lista_sorteo.sort()
print(lista_sorteo)


