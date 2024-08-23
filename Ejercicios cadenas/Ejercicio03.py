

""" Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

 """
palabra=input("Escribe una palabra: ")
while not palabra.isalpha():
    palabra=input("ERROR. Escribe una palabra valida: ")
    
caracter=input("Ingrese un caracter: ")

while len(caracter)!=1:
    caracter=input("Ingrese un solo caracter: ")
    
cont=0
for i in range(len(palabra)):
    if caracter==palabra[i]:
        cont+=1
    
print(f"El caracter '{caracter}' aparece {cont} veces")
