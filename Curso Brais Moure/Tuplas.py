#las tuplas son un conjuto de elementos que una vez determinado no puede ser modificado
#una forma de hace una tupla mutable es convertirla en una nueva lista
#basicamente son lo mismo que las listas con la siguiente diferencia:
# - no pueden modificarse directamente

#creacion de una tupla

my_tuple=tuple()
my_other_tuple=()

my_tuple = ("Rodrigo", 32, 1.77)
#metodos apliables:
#count, cuenta los elementos determinados

print(my_tuple.count("Rodrigo"))

#len retorna cantidad de elementos
print(len(my_tuple))

#index devuelve el indice del elemento determinado

print(my_tuple.index(32))

#se puede convertir una tupla en una lista y modificarla

my_tuple=list(my_tuple)
print(type(my_tuple))
my_tuple.append("Ramirez")
my_tuple=tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#el metodo funciona pero la funcion de la tupla es no modificar los valores por lo que si 
#se piensa en utilizar una tupla es para mantener los valores constantes

#copiar tupla
my_other_tuple=my_tuple
#del borra la tupla, queda la variable libre
del my_tuple
try:
    print(my_tuple)
except:
    print("La variable my_tuple no existe porque fue borrada")

print("Rodrigo" in my_other_tuple)