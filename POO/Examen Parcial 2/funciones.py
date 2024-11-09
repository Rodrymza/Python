def pedir_entero(mensaje,min = 0, max = 1000):
   while True:
        numero = input(mensaje + "\n")
        try:
            numero = int(numero)
            if numero >= min and numero <= max:
                return numero
            else:
                print(f"Debes colocar un numero entre {min} y {max}")
        
        except:
            print("El valor ingresado es incorrecto")
            
def pedir_decimal(mensaje):
   while True:
        numero = input(mensaje + "\n")
        try:
            numero = float(numero)
            return numero
        except:
            print("El valor ingresado es incorrecto")
            
def pedir_boolean(mensaje):
    while True:
        respuesta = input(mensaje + "(s/n)\n")
        match respuesta:
            case "s": return True
            case "n": return False
            case _: print("Respuesta incorrecta")
            
def buscar_lista(lista, busqueda):
    for elemento in lista:
        if busqueda == elemento:
            print("Elemento encontrado")
            return elemento
    print("No se encontro el elemento en la lista")
    
