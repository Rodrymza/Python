""" Desarrollar un algoritmo que permita ingresar un ancho y un alto (ambos números deben ser 
positivos). La computadora debe dibujar una matriz de cruces en la consola de tales dimensiones. """

ancho=int(input("Ingrese el ancho del dibujo: "))
alto=int(input("Ingrese el alto del dibujo: "))
dibujo=""
for i in range(alto):
    for j in range(ancho):
        print("X", end="") 
    print("")    
    
print("Otra maner de lograr lo mismo") 
   
for i in range(alto):
    for j in range(ancho):
        dibujo+="X"
    print(dibujo)
    dibujo=""      