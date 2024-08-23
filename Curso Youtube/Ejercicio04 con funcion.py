def resultado(num1,num2,operacion):
    match operacion:
        case 1: 
            rta="La suma"
            resultado=num1+num2
        case 2:
            rta="La resta"
            resultado=num1-num2
        case 3: 
            rta="La multiplicacion"
            resultado=num1*num2
        case 4:
            rta="La division"
            resultado=num1/num2
        case 5:
            rta="El resto"
            resultado=num1%num2
        case 6:
            rta="La potencia"
            resultado=num1**num2
        case 7:
            rta="La division entera"
            resultado=num1//num2
    return print(f"{rta} de {num1} y {num2} es {resultado}")
    

num1=int(input("Ingrese el valor del primer numero: "))
num2=int(input("Ingrese el valor del segundo numero: "))
print("Seleccione la operacion deseada:")
print("1- Suma 2-Resta 3-Multiplicacion 4- Division 5-Resto 6-Potencia 7-Division Entera")
operacion=int(input())

resultado(num1,num2,operacion)