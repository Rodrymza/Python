#Strings

my_string="Mi string"
my_other_string="Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string, my_other_string)

my_newline_string="Este es un string con\nsalto de linea"
print(my_newline_string)

tab_string="Esto es un string\tcon tabulacion"
print(tab_string)

scape_string="Caracter de escape \\n no hace salto de linea"
print(scape_string)

#Formateo

nombre,apellido,edad ="Rodrigo","Ramirez",32

print("Mi nombre es {}, mi apellido es {} y mi edad es {}".format(nombre,apellido,edad))    #pasaje como con fstrings
print(f"Mi nombre es {nombre}, mi apellido {apellido} y mi edad {edad}")                    #inferencia de datos
print("Mi nombre es %s %s y mi edad es %d" %(nombre,apellido,edad))                         #se pasa el dato tal cual, formateado

#desempaquetado

language="Python"
a,b,c,d,e,f=language
#print(a,b,e,f)

#division

language_slice=language[::2]
print(language_slice)

language_slice=language[0:4:]
print(language_slice)

language_reversed=language[::-1]
print(language_reversed)

print(language.capitalize())
print(language.count("t"))
language_slice=language[::2]
print(language.lower())
print(language.isnumeric())
print("123".isnumeric())

number=input("Ingrese un numero \n")
if number.isnumeric():
    print(f"{nombre} ingresaste un numero")
else:
    print("So tonto vo'")