nombres = []
entrada=""

while entrada!="salir":
    entrada=input("Ingrese un Nombre: ")
    nombres.append(entrada.title())
    
nombres.pop()
for i in range(0,len(nombres)):
    print("Elemento en ubucacion", i+1, nombres[i])
    
    