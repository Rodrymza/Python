"""Tipos de datos en Python:
-Enteros y largos
-flotantes
-numeros complejos
-cadenas
-boleanos

Enteros sin decimales, flotantes con decimal
Entero: int, long
Flotantes: float
Complejos: parte real y parte imaginaria
			complex
Cadenas: texto
	Escribiendo la cadena entre comillas triples se respetan los saltos de linea
"""
print("""Esto es un comentario
	con saltos de linea utilizando
	las comillas triples""")

"""tambien se puede recurrir al recurso /n para colocar un salto de linea
Booleanos: True False

"""

print("Tipo de dato entero")
num=15
print("usando el comando type Python nos indica que tipo de dato tiene una variable determinada")

print(num, type(num)) #con la instruccion print se pueden concatenar datos usando la coma

print("Este este es un tipo de dato flotante")
num_flotante=15.5
print(num_flotante, type(num_flotante))

print("Este es un tipo de dato de numero complejos")
num_complejo = 5 + 6j
print(num_complejo, type(num_complejo))

print("Esto es una variable de tipo cadena")
cadena="Mucho texto"
print(cadena, type(cadena))

print("Esto es una variable de tipo booleano")
booleano=False
print(booleano, type(booleano))
print(booleano==False)
