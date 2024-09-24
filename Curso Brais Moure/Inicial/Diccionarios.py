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

print(my_dict["Apellido"])

#obtener un listado cada uno de los items, clave-valor
print(my_dict.items())

#obtiene un listado de las keys
print(my_dict.keys())

#obtiene un listado de todos los elementos guardados
print(my_dict.values())



#crear un diccionario a partir de otros objetos
lista=["hola", "como", "va"]
my_new_dict=dict.fromkeys((lista))
print(my_new_dict)

#ej, crear un diccionario vacio con las claves almacenadas en una lista
#el segundo parametro es para darle un valor predeterminado al valor almacenado
campos=["Nombre", "Apellido", "DNI", "Direccion"]
valores=["Rodrigo", "Ramirez", 36499229, "Moldes"]
diccionario=dict.fromkeys(campos, valores)
print(diccionario)
print(list(diccionario)) #se crea un lista con las keys del diccionario, las claves no se toman en cuenta

