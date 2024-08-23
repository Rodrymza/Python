""" Desarrollar un algoritmo que permita ingresar un monto en dólares (entero). La computadora debe
mostrar cómo pagar ese monto con la menor cantidad de billetes posibles. """

monto = int(input("Ingrese un monto de dinero en dolares: "))

cien = monto//100
monto = monto%100

cincuenta = monto//50
monto = monto%50

veinte = monto//20
monto = monto%20

diez = monto//10
monto=monto%10

cinco = monto//5
monto = monto%5

dos = monto//2
monto = monto%2

uno = monto//1


print("Billetes de u$d100:",cien)
print("Billetes de u$d50:",cincuenta)
print("Billetes de u$$d20:",veinte)
print("Billetes de u$d10:",diez)
print("Billetes de u$d5:",cinco)
print("Billetes de u$d2:",dos)
print("Billetes de u$d1:",uno)