clave1="Atencion al Cliente"
clave2="Logistica"
clave3="Gerencia"
nombre=""
antiguedad=0
vacaciones=0
sector=0
print("Ingrese nombre del trabajador: ")
nombre=input()
print("Ingrese antigüedad: ")
antiguedad=int(input())
while sector<1 or sector>3:
    print("Seleccione sector: ")
    print(f"1 - {clave1}")
    print(f"2 - {clave2}")
    print(f"3 - {clave3}")
    sector=int(input())
    if sector<=0 or sector >=4:
        print("Valor invalido")


match sector:
    case 1: 
        if antiguedad<=1:
            vacaciones=6
        elif antiguedad>=2 and antiguedad<=6:
            vacaciones=14
        else:
            vacaciones=20
    case 2:
            if antiguedad<=1:
                vacaciones=7
            elif antiguedad>=2 and antiguedad<=6:
                vacaciones=15
            else:
                vacaciones=22
    case 3:
            if antiguedad<=1:
                vacaciones=10
            elif antiguedad>=2 and antiguedad<=6:
                vacaciones=20
            else:
                vacaciones=30

print(f"Al trabajador {nombre} le corresponden {vacaciones} dias de vacaciones") 

    