letras = ["abcdfghijklmnopqrstuvwxyz", "1234567890", "_[¨*¡?=)(/&%$#n\"!)]{+'¿~\\@}"]
letras.insert(1, letras[0].upper())
from random import randint
from random import shuffle
percent = [0.25, 0.2, 0.2, 0.35]
nombres = ["minisculas", "mayusculas", "numeros", "simbolos"]
password_len = 16
password = ""
indice = 0
for number in percent:
    print(f"Cantidad de {nombres[indice]}: {round(password_len*number,0)}")
    for i in range(round(password_len*number)):
        password += letras[indice][randint(0,len(letras[indice])-1)]
    indice += 1
        
password = list(password)
shuffle(password)
contrasenia = ""
for letra in password:
    contrasenia += letra
    
print(contrasenia, len(contrasenia))