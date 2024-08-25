#Diccionarios
#conjunto de objetos almacenados segun clave-valor, similares a los mapas en otros lenguajes de programacion
#un diccionario es practicamente un json


my_dict = {}
my_other_dict = dict()

my_other_dict={"Nombre": "Rodrigo", "Apellido": "Ramirez", "Edad": 32, 1: "Python"} 

my_dict = {
    "Nombre": "Rodrigo",
    "Apellido": "Ramirez",
    "Edad": 32, 1: "Python",                
    "Lenguajes" : {"Python","Purebasic"}, #en este caso la clave es un string y el valores un set (se encuentra entre llaves)
    1: 36499229
    } 
print(my_dict)
print(my_dict["Lenguajes"]) #se imprimen en pantalla valores guardados en la clave "Lenguajes"

print(f"La cantidad de claves en el diccionario es de {len(my_dict)}")  #5 claves en el diccionario

print(my_dict[1])

#modificar un dato
my_dict["Nombre"]="Rodry"

#agregar un nuevo campo al diccionario, como si asignaramos un valor a una lista
my_dict["Calle"]="Moldes"

print(my_dict)

#operaciones
# -eliminar un campo completo:
del my_dict["Calle"]
print(my_dict)

print("Rodry" in my_dict)
print("Nombre" in my_dict) #en este caso lo que busca es la clave, no el valor

