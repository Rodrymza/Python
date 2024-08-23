""" Desarrollar un algoritmo que permita ingresar dos números enteros y un símbolo que indique una
operación matemática a realizar con ellos:
▪ + para sumar
▪ - para restar
▪ x para multiplicar
▪ / para dividir
La computadora debe mostrar el resultado de la operación. """

a=int(input("Ingrese primer numero :"))
b=int(input("Ingrese segundo numero :"))

print("Seleccione la opcion deseada:")
print("(+) Suma")
print("(-) Resta")
print("(*) Division")
print("(/) Multiplicacion")
seleccion=int()
match seleccion:
    case "+":
        print("La suma de", a, "+", b, "es", a+b)