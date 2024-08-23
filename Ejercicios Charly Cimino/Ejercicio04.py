""" Desarrollar un algoritmo que permita ingresar una hora del día (entre 0 y 23, si no, informar un
error). La computadora debe mostrar a qué momento del día pertenece según lo siguiente:
▪ Madrugada: Entre 0 y 5, inclusive
▪ Mañana: Entre 6 y 11, inclusive
▪ Mediodía: Entre 12 y 13, inclusive
▪ Tarde: Entre 14 y 19, inclusive
▪ Noche: Entre 20 y 23, inclusive """

hora=int(input("Ingrese la hora: "))
while hora<0 or hora>23:
    hora=int(input("ERROR. Ingrese hora valida Ingrese la hora: "))

minutos=int(input("Ingrese los minutos: "))
while minutos<0 or minutos>59:
    minutos=int(input("ERROR. Ingrese hora valida. Ingrese los minutos: ", hora, ":"))

if hora<=5:
    print("Madrugada")
elif hora<=11:
    print("Mañana")
elif hora<=13:
    print("Mediodia")
elif hora<=19:
    print("Tarde")
else:
    print("Noche")
