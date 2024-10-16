def operacion_matematica(num1, num2, operacion):
    match operacion:
        case 0: return num1+num2
        case 1: return num1-num2
        case 2: return num1*num2
        case 3: return round(num1/num2,2)
        case _: print("Operacion mal ingresada")

numero1 = int(input("Ingrese un numero"))
numero2 = int(input("Ingrese otro numero"))

operaciones = ("Suma", "Resta", "Multiplicacion", "Division")

for i in range(len(operaciones)):
    print(f"La {operaciones[i].lower()} de {numero1} y {numero2} es {operacion_matematica(numero1, numero2, i)}")