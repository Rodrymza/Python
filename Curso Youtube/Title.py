#funcion title personalizada

frase="hola Como Va TOdo bien"
i=0
frase=frase.upper()
nueva_frase=""
num_letras=len(frase)
while i<num_letras:
    nueva_frase=nueva_frase + frase[i:i+1]
    if frase[i:i+1]==" ":
        frase=frase.upper()
    else:
        frase=frase.lower()
    i=i+1
print(nueva_frase)
    
    