""" Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado. """

palabra=input("Ingresa una palabra: ")

busqueda=input("Ingresa la cadena que vas a buscar al principio: ")

if palabra.startswith(busqueda):
    print(f"La primer palabra comienza con '{busqueda}'")
else:
    print(f"La palabra NO comienza con '{busqueda}")