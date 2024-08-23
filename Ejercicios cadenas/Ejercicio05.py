#Funciones
def capitalizar(palabra):
    capitalizada=palabra.upper()[0]+palabra.lower()[1:len(palabra)]
    return capitalizada

#Programa principal
nombre="rodRiGo"
nombre=capitalizar(nombre)
nombre1="roCio"
nombre1=capitalizar(nombre1)

nombre3="ferNaNdo"
nombre3=nombre3.capitalize()