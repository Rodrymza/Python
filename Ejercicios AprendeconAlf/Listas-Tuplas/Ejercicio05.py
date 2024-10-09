lista = [i for i in range(1 ,11)]

def invertir(lista):
    nuevalista = []
    for elemento in lista:
        nuevalista.insert(0, elemento)
    return nuevalista

for elemento in reversed(lista):
    print(elemento)

print(lista)

lista_invertida = invertir(lista)

print(lista_invertida)