def agregar_pais(diccionario):
    nombre_pais = input("Ingresa el nombre del pais\n").capitalize()
    if diccionario.get(nombre_pais):
        print("El pais ya se encuentra agregado")
    else:
        diccionario[nombre_pais] = []
        print(diccionario)
        agregar_cuidad(diccionario, nombre_pais)
    
def agregar_cuidad(diccionario, nombre_pais):
    if diccionario.get(nombre_pais) != None:
        while True:
            nombre_ciudad = input("Ingresa nombre de una ciudad\n").capitalize()
            diccionario[nombre_pais].append(nombre_ciudad)
            opcion = input("Desea agregar otra ciudad? (y/n)").lower()
            if opcion == "n":
                break
    else:
        print("El pais no existe")


def mostrar_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print("\t Pais:", clave)
        print(*valor, sep="\n")

def mostrar_paises(diccionario):
    print("\tLista de paises:")
    print(*diccionario.keys(), sep= "\n")

def eliminar_cuidad(diccionario, pais):
    if diccionario.get(pais) == False:
        print("El pais no tiene ciudades asignadas")
    elif diccionario.get(pais) == None:
        print("El pais no existe")
    else:
        print("\tLista de ciudades:")
        print(*diccionario[pais],sep="\n")
        eliminar = input("Escriba ciudad a eliminar\n").capitalize()    #Agregar verificacion de ciudad
        print(eliminar)
        diccionario[pais].remove(eliminar)
      



paises = {}
agregar_pais(paises)
#agregar_pais_ciudad(paises)
mostrar_diccionario(paises)

eliminar_cuidad(paises, "Argentina")
eliminar_cuidad(paises, "Argentina")
mostrar_diccionario(paises)
