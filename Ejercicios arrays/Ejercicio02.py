""" Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector con datos leídos por el teclado.
Copia los elementos del vector en otro vector pero en orden inverso, y muéstralo por la pantalla. """

palabras=[]
tamanio=5
palabrasinv=[]
for i in range(tamanio):
    palabras.append(input("Ingrese una palabra: "))

for elemento in palabras:
    palabrasinv.insert(0,elemento)  #(indice, elemento a agregar), al agregarlo siempre en el indice 0 se agregan los elementos en orden iverso
    
for elemento in palabrasinv:    
    print(elemento)

