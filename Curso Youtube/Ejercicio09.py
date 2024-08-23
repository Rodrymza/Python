"""Solicitar frase desde el teclado y un caracter, imprimir en pantalla la frase sin vocales y en caso de encontrar el caracter
el bucle debe finalizar"""

frase="hola gente como va"
caracter="p"
for i in frase:
    if i!="a" and i!="e" and i!="i" and i!="o" and i!="u":
        if i==caracter:
            break
        else:
            print(i,end="")
