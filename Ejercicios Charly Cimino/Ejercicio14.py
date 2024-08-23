""" Desarrollar un algoritmo que permita ingresar un nombre de usuario y una contraseña. En caso de 
ser válidos, se imprimirá "Acceso concedido", de lo contrario, se deben volver a pedir las 
credenciales hasta un máximo de tres intentos. Si se supera la cantidad de intentos fallidos, se 
mostrará "Cuenta bloqueada" """

max_intentos=3
usuario="rodry"
contrasenia="1234"
cont=1

user=input("Ingrese usuario: ")
password=input("Ingrese contraseña: ")

while (user!=usuario or contrasenia!=password) and cont<max_intentos:
    print("Datos incorrectos")
    cont+=1
    user=input("Ingrese usuario: ")
    password=input("Ingrese contraseña: ")
    
if user==usuario and contrasenia==password:
    print("Acceso correcto")
else:
    print("Acceso bloqueado")