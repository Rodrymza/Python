""" Desarrollar un algoritmo que permita ingresar la edad y el sueldo anual en dólares de un empleado.
La computadora debe mostrar el monto del aporte al sindicato que se debe descontar del salario del
empleado, según el siguiente cuadro:
Escala salarial Porcentaje a descontar
Menos de $10000 0.5%
Entre $10000 y $19999 1%
Entre $20000 y $29999 2%
$30000 o más 2.5%
Si la persona tiene 30 años o menos, se sumará un 20% adicional al valor del aporte sindical. """

edad = int(input("Ingrese la edad del empleado: "))
sueldo = float(input("Ingrese sueldo anual del empleado: "))

if sueldo < 10000:
    descuento = 0.005
elif sueldo < 19999:
    descuento = 0.01
elif sueldo < 29999:
    descuento = 0.02
else:
    descuento=0.025

aporte = sueldo * descuento

if edad <= 30:
        print("El empleado tiene menos de 30, se hara 20% de descuento extra")
        aporte=aporte*1.2

print("El monto a descontar fue de", (descuento*100), "%")
print("El valor a aportar sera de $" + str(aporte))

