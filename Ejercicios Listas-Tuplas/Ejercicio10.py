"""Escribir una funcion que devuelva el producto de cada par de elementos consecutivos de una lista"""

def producto_pares(lista):
    i=0
    producto=[]
    while i<len(lista):
       multiplo=lista[i]*lista[i+1]
       producto.append(multiplo)
       i+=2
    return producto
        
lista=[1,2,3,4,5,6,7,8]
print(producto_pares(lista))