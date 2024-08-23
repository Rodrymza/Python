"""Title es una funcion que nos devuelve una cadena con las primeras letras de cada palabra en mayuscula y las demas en imprenta
istitle sirve para verificar si la cadena cumple con ese formato"""

cadena="Hola gente cOmo Va"

print(f"Cadena sin formato: {cadena}")
print(f"Verificar si cumple con el fotmato de title: {cadena.istitle()}")

print(f"Cadena con formato: {cadena.title()}")
cadena=cadena.title()   #se le asigna nuevo formato a la cadena
print(f"Verificar si cumple con el fotmato de title: {cadena.istitle()}")