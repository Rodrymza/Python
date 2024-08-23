""" Desarrollar un programa que permita ingresar el ancho y el largo de un terreno (en metros) y el
precio del metro cuadrado de tierra. La computadora debe calcular y mostrar el precio del terreno
y la cantidad de metros de alambre que habría que comprar para cercarlo en tres pasadas. """

precio=float(input("Ingresa el precio por metro cuadrado $"))
ancho=float(input("Ingresa el ancho del terreno: "))
largo=float(input("Ingresa el largo del terreno: "))

perimetro=ancho*2+largo*2
area=ancho*largo

valor_terreno=area*precio

print("El valor del terreno es de $" + str(valor_terreno))

print("El total de metros necesarios para cercar el terreno 3 veces es de", (perimetro*3), "metros")
