""" Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), 
realiza un programa que cuente cuantas palabras tiene. """

def contarPalabras(frase):
    palabras=1
    for i in range(len(frase)):
        if frase[i]==" ":
            palabras+=1
    
    return palabras
        

frase=input("Ingresa una frase para contar las palabras: \n")

print(f"La frase ingresada tiene {contarPalabras(frase)} palabras")
