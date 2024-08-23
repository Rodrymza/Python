#programa que elimine una palabra dentro de una cadena de caracteres
#cadena y palabra a eliminar solicitada desde el teclado

frase="Sera por ti sera por mi sera por todo lo que fuimos"
frase=frase.lower()
print(frase)

palabra="sera"     #input("Ingrese palabra a eliminar\n") + " " #agrego espacio para eliminar la palabra y el espacio correspondiente
palabra=palabra.lower()
inicio=frase.find(palabra)
print(frase.find(palabra))
fin=inicio+len(palabra)
print(frase[0:inicio]+frase[fin:]) #con subcadena
#palabra+=" " #se agrega espacio para eliminar espacios duplicados
print(frase.replace(palabra,"")) #con funcion replace

"""La primera solucion solo elimina una palabra encontrada, en esta caso seria la primera, se puede implementar una funcion que 
haga lo que hace el metodo replace?"""

aux=""
print(len(palabra))
indice=0
while indice<=len(frase):
    i=frase[indice:indice+len(palabra)]
    print(i)
    if i!=palabra:
        aux+=i

    indice=indice+len(palabra)
print(aux)