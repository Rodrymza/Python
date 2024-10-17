from random import randint
def crear_tupla():
    total_numeros = 10
    lista = []
    for i in range(total_numeros):
        #lista.append(int(input("Ingresa un numero:\n")))
        lista.append(randint(0,10))
    tupla = tuple(lista)
    return tupla

def mayores_que_cinco(tupla):
    set_numeros = set()
    for elemento in tupla:
        if elemento > 5:
            set_numeros.add(elemento)
    return set_numeros
tupla_numeros = crear_tupla()
print(tupla_numeros)

set_numeros = mayores_que_cinco(tupla_numeros)
print(set_numeros)