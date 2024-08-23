def agregar_usuario():
    usuarios.append(input("Ingresa el nuevo usuario: "))
    contrasenias.append(input("Ingresa contraseña para el usuario: "))
    import random
    num=random.randint(1000,9999)
    print(f"Numero para validacion: {num}")
    validar=int(input("Ingresa el valor en pantalla para validar usuario: "))
    
    if num==validar:
        print("Usuario y contraseña validado y agregado: ")
    else:
        print("No se valido el usuario")
    

def validar_usuario():
    pass

def imprimir_usuarios():
    for i in range(len(usuarios)):
        print(f"Lista de usuarios y contraseñas: {usuarios[i]} - {contrasenias[i]}")

#Programa principal

usuarios=[]
contrasenias=[]

agregar_usuario()
imprimir_usuarios()
agregar_usuario()
imprimir_usuarios()



