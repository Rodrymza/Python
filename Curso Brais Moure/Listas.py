#se puede iniciar una lista de dos maneras
mi_lista=list()
mi_otra_lista=[]

print(len(mi_lista))

#llenado con elementos
mi_lista=[32,30,25,29,20,19,18,24,26,30]
print(mi_lista)
print(f"El tamaño de la lista es {len(mi_lista)}")

mi_otra_lista=[32,1.68, "Rodrigo", "Ramirez"]
print(mi_otra_lista)
print(f"El tipo de dato es {type(mi_otra_lista)}")

#el tipo aparece como "list"

print(mi_otra_lista[2])  #se imprime el elemento '2' de la lista
print(mi_otra_lista[-1]) #al colocar un indice negativo se imprime el ultimo o la cantidad indicada con el numero negativo
#print(mi_otra_lista[4] daria error por estar fuera de indice, al igual que llamar a [-5]

print(mi_otra_lista[len(mi_otra_lista)-1]) #llamado para imprimir el ultimo elemento, un quilombo al pedo, mejor usar [-1]

#count sirve para contar la cantidad de elementos determinados que hay:
print(f"En la lista encontramos {mi_lista.count(30)} veces el numero 30")

#es un metodo que sirve para cualquier elemento iterable, es por eso que tambien podemos usarlo en cadenas de texto:

print(f"Encontramos la letra 'o' {"Rodrigo".count("o")} veces en el nombre 'Rodrigo'")


edad, altura, nombre, apellido = mi_otra_lista[0], mi_otra_lista[1], mi_otra_lista[2], mi_otra_lista[3]
#se pueden asignar muchas variables en una lista de errores pero es algo que puede producir ERRORES, no es recomendado

print(edad)

#las listas puesen sumarse facilmente consiguiendo que se concatenen ambas, se colocan los elementos de una al final de la otra:
print(mi_lista + mi_otra_lista)

for i in mi_lista + mi_otra_lista:  #tambien pueden sumarse directamente en un bucle for
    print(i)

lista_nombre=list("Rodrigo")
print(lista_nombre)

#ojo! si usamos el mismo nombre de variable que usamos en una lista y le asignamos un valor, la lista queda anulada, esto es porque
#python es un lenguaje debilmente tipado y los tipos de variable se van dando a medida que se escribe el codigo, ej:

#mi_lista="Hola como estas"
#print(mi_lista)
#print(type(mi_lista))

#esto le daria el valor de "Hola como estas" a la variable mi_lista, con lo que los datos anteriores quedarian borrados

#una forma de definir una especie de constante en pyton es definir a la variable en MAYUSCULAS, ya que en pyton las constantes en si no existen

#el metodo append inserta un elemento al final de la lista
mi_otra_lista.append("Hospital Santa Isabel")
print(mi_otra_lista)

#Insert inserta un elemento en la posicion indicada
#insert(posicion,elemento a insertar)
mi_otra_lista.insert(0,"Rojo")
print(mi_otra_lista)

#Metodo remove, elimina la primera aparicion del elemento determinado
mi_otra_lista.remove("Rojo")
print(mi_otra_lista)

#Metodo pop elimina el ultimo elemento
print("Eliminar por pop")       #este metodo devuelve el valor del elemento que se elimino, en este caso devolveria un 30, sirve para quitar 'sustraer' un elemento
print(mi_lista)
print(f"{mi_lista} \n Eliminamos el ultimo elemento: {mi_lista.pop()} \n {mi_lista}")
#de manera predeterminada elimina el ultimo elemento, pero entre los parentesis se puede determinar que indice de elemento queremos eliminar

#metodo clear.() elimina la lista completa

#mi_lista.clear()

print(mi_lista) #esto imprimiria la lista vacia

#copiar una lista
nuevalista = mi_lista.copy()
print(nuevalista)
print(mi_lista)

#metodo sort ordena los elementos de menor a mayor, entre parentesis se pasan criterios para ordenarla
mi_lista.sort() #hay que ejecutar la oden primero, si lo hacemos dentro del print directamente retorna un none
print(mi_lista)
print(mi_lista.sort())

#sorted devuelve una nueva lista

listaordenada=sorted(mi_lista,reverse=True) #reverse=True la ordena en orden inverso, de mayor a menor
print(listaordenada)

"""resumen de fuciones:

- list() o lista=[] para crearla
- len() nos devuelve la cantidad de elementos
- count.("elemento") nos devuelve la cantidad de veces que encuentra el ememento 
- append() inserta elemento al final, insert(indice, elem) inserta elemento en posicion indicada
- remove(-elemento-) remueve la primera aparicion del elemento mencionado
- pop(-indice-) remueve de forma predeterminada el ultimo elemento o el elemento indicado y retorna el valor de ese elemento
- .copy() copia la lista
- .sort ordena la lista, .sort hace el ordenado directamente y sort(lista) retorna una nueva lista ordenada sin modificar la lista que se paso por parametro
"""
