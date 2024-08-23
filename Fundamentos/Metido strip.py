"""El metodo strip sirve para ir eliminando caracteres de los extremos de la cadenas. 
rstrip y ltrip sirve para hacerlo desde un u otro extremo determinado"""

palabra="Hola como estas"

"Se utilizan como la mayoria de las funciones en python con el .strip()"

subcadena=palabra.strip("Hsa")

print(subcadena)
print("Se eliminaron las letras H,s y a que estaban en los extremos de la cadena, el metodo busca una letra determinada en ambos extremos")
print("y luego vuelve a empezar con el caracter siguiente")
"""En caso de no asignar ningun parametro la funcion eliminara los espacios en blanco de manera predeterminada"""

cadena="     ....Hola...     "
print(f"Cadena con espacios:\n {cadena} ")
print(f"Cadena sin espacios \n {cadena.strip()}")

"""Los metodos strip y ltrip eliminan los caracteres especificados de un lado determinado, l: izquierda, r:derecha"""

cadenader="Hola........"
cadenaizq="........Hola"

print(f"Cadena con puntos a la der {cadenader}")
print(f"Cadena con puntos a la izq {cadenaizq}")

print("Eliminando puntos:")
print(cadenaizq.lstrip("."))
print(cadenader.rstrip("."))