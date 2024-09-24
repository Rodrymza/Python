### Sets ###

#creacion de un set, el set es un tipo de dato al igual que las listas y las tuplas
#son basicamente listas pero con unas diferencias:
# - no es una estructura ordenada
# - no admite elementos repetidos

my_set=set()
my_other_set={}     #inicialmente es un diccionario

print(type(my_set))
print(type(my_other_set))

my_other_set={"Rodrigo", "Ramirez", 32}
print(type(my_other_set)) #en este punto python lo define como set ya que el metodo de ingreso entre un diccionario y un set es distinto

#utiliza las mismas funciones que una lista o tupla

print(f"El total de elemenos del set es {len(my_other_set)}")
try:
    print(my_other_set[0])
except:
    print("Los elementos de los sets no se pueden convocar mediante indices como las listas")

#operaciones

#add agrega un elemento
my_other_set.add("rodrymza")
print(my_other_set)

#el elemento se agrega, pero no tiene indice ni se encuentran ordenados, no tienen un control por indices
my_other_set.add("Rodrigo")
print(my_other_set)
#NO se admiten repetidos, por lo tanto al intentar ingresar un elemento que ya se encuentra en la lista no se agrega

#Sintaxis para determinar si existe un elemento en el set
print("Rodrigo" in my_other_set)
print("Rodry" in my_other_set)

flag="Rodigo" in my_other_set   #comprobar elemento dentro del set
print(flag)

#eliminar con remove
my_other_set.remove("rodrymza")
print(my_other_set)

#elimina un elemento aleatorio ya que no se encuentra ordenado
print(my_other_set.pop())
print(my_other_set)
my_other_set={"Rodrigo", "Ramirez", 32}

#difference devuelve los valores distintos entre el set enviado y comparado
my_set={"Rodrigo", 32, "rodrymza"}
print(my_set.difference(my_other_set))

#clear borra los elementos y del borra el objeto
#my_other_set.clear()
#print(type(my_other_set))
#del my_other_set
#print(type(my_other_set))

my_list=list(my_other_set)
my_list.sort(key=str) # determino que se ordene segun fueran tipos str
print(my_list)

my_other_set = {"Python", "Pureabasic", "Java"}

#concatenar sets

my_new_set = my_set.union(my_other_set)
print(my_new_set)
