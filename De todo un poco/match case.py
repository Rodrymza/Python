dia=0
dia=int(input("Ingrese un dia de la semana \n"))
match dia:
    case 1 | 8 | 9:
        print("El dia es lunes")
    case 2:
        print("El dia es martes")        
    case 3:
        print("El dia es miercoles")  
    case 4:
        print("El dia es jueves")  
    case 5:
        print("El dia es viernes")  
    case 6:
        print("El dia es sabado")  
    case 7:
        print("El dia es domingo")
    case _:
        print("No ingresaste un dia valido")  
            