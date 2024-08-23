mensaje="hola"
nombre="Rodri"
numero=22
print(mensaje + " " + nombre +  " " + str(numero))

nuevavariable=nombre + mensaje + str(numero)

num1=2
num2=5
resultado = num1 + num2

print("El resultado de " + str(num1) + "+" + str(num2) + " es " + str(resultado))

print("Busqueda con parametro .find")
mensaje="Hola como va"
subcadena_mensaje=mensaje.find("como")

print(subcadena_mensaje)

print("Subcdena especifica")

subcadena=mensaje[5:9] #El numero final de la subcadena no se incluye en la variable (5-8)

print(subcadena)
