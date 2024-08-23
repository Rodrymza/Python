"""Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base 
y comisiones."""

base=3500
comision=0.10
ventas=3
cont=1
total=0

while cont<=ventas:
    print("Venta", cont)
    venta=float(input("Ingrese el monto: "))
    cont=cont+1
    total=total+venta

comisiontotal=total*comision
sueldo=round(base+comisiontotal,2)

print("Sueldo base $", base)
print("Total vendido $", total)
print("Comision $", comisiontotal)
print("El total a percibir sera de $",sueldo)