frase="hola Como Va TOdo bien"
i=1
frase=frase.lower()
nueva_frase=""
num_letras=len(frase)
while i<num_letras:
    nueva_frase=nueva_frase+frase.upper()[i:i+1]
    i=i+1
    

print(nueva_frase)