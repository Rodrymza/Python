def eliminar_espacios(frase):
    frase = frase.strip()
    i=0
    nuevafrase = ""
    while i<len(frase):
        if frase[i] == " ":
            while frase[i+1] == " ":
                i += 1
        nuevafrase += frase[i]
        i += 1
    return nuevafrase    
frase = "  hola   gente    a    todos como      va    todo bien?   "
print(eliminar_espacios(frase))
