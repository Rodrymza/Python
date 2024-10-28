def es_anagrama(palabra1, palabra2):
    set1 = set(list(palabra1.lower()))
    set2 = set(list(palabra2.lower()))
    print("Son anagramas") if set1 == set2 else print("No son anagramas")

texto1 = input("Ingresa una palabra\n")
texto2 = input("Ingresa otra palabra\n")

es_anagrama(texto1, texto2)
