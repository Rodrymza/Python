"""Calculadora basica"""
operacion=0
print("Calculadora basica")
num1=int(input("Ingrese el valor del primer numero: "))
num2=int(input("Ingrese el valor del segundo numero: "))
print("Seleccione la operacion deseada:")
while operacion<=0 or operacion>=8:
    print("1- Suma 2-Resta 3-Multiplicacion 4- Division 5-Resto 6-Potencia 7-Division Entera")
    operacion=int(input())

    match operacion:
        case 1:
            print(f"La suma de ambos numeros es {num1+num2}")
        case 2:
            print(f"La resta de ambos numeros es {num1-num2}")
        case 3:
            print(f"La multiplicacion de ambos numeros es {num1*num2}")
        case 4:
            print(f"La divison de ambos numeros es {num1/num2}")
        case 5:
            print(f"El resto de ambos numeros es {num1%num2}")
        case 6:
            print(f"La potencia de ambos numeros es {num1**num2}")
        case 7:
            print(f"La division entera de ambos numeros es {num1//num2}")
        case _:
            print("Seleccion no valida")