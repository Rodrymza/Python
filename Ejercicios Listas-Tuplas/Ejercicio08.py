"""Ordenar lista de tuplas"""
def ordenar_lista():
    pass

lista_original=[("Roberto",90),("Bob",70),("Charlie",85)]
lista_ordenada=sorted(lista_original,key=lambda tupla:tupla[1],reverse=True)
print(lista_ordenada)

#el metodo lambda tupla:tupla[#] hace que se ordene la lista segun el elemento de la tupla que se indica