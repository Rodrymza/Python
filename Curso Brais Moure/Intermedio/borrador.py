def analizar_texto(texto):
    nuevapalabra = ""
    abecedario="abcdefghijklmnopqrstuvwxyzñ.áéíóúüöäë "
    abecedario += abecedario.upper()
    for letra in texto:
        if letra in abecedario:
            nuevapalabra = nuevapalabra + letra
    nuevapalabra = nuevapalabra.rstrip().lstrip()
    palabras = 1 if len(nuevapalabra)>0 else 0
    oraciones = 0 if nuevapalabra[-1] == "." else 1
    for letra in nuevapalabra:    
        match letra:
            case ".":
                oraciones += 1
            case " ":
                palabras += 1
    print("Texto formateado:", nuevapalabra)
    print("El texto ingrasado tiene,", palabras, "palabras")
    print("El texto ingresado tiene", oraciones, "oraciones")

frase = "    hola gente como va por aca. Todo bien??? que onda con la ónda. !! ; ()"

analizar_texto(frase)