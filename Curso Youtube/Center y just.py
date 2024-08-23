"""Los metodos center y just añaden caracteres especificos a la cadena, si no se envian parametros se colocan espacios sino se especifica
el caracter dentro de los parametros de la funcion"""

cadena="Rodrigo"

print("Cadena centrada con '='")
print(cadena.center(20,"="))

"""Los metodos l y rjust añaden los caracteres a la derecha o izquierda respectivamente"""

print("ljust:")
print(cadena.ljust(20,"="))

print("rjust:")
print(cadena.rjust(20,"="))