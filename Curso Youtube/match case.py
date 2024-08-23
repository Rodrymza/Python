dia=-1
while dia<1 or dia>7:
    dia=int(input("Ingrese un dia de la semana \n"))
    match dia:
        case 1 or 2 or 3 or 4 or 5:
            print("Es dia laborable")
        case [6,7]:
            print("Es fin de semana")
            