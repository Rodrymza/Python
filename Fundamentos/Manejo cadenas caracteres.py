
print("Manejo de cadena de caracteres")

print("Asignacion")

mensaje="Hola como va"


print("Concatenacion")

nombre=" Rodrigo"

mensaje=mensaje + nombre

print(mensaje)


mensaje+= " , que onda"
print(mensaje)


print("Busqueda")

print(mensaje.find("q"))


print("Extraccion")


subcadena=mensaje[0:5]
print(subcadena)


print("Comparacion")
print("Comparando varible mensaje y variable nombre")
SonIguales=mensaje==nombre

if SonIguales==True:
    print("Las variables son iguales")
else:
    print("Las variables son diferentes")


for i in range(10):
    print("Numero " + str(i))
