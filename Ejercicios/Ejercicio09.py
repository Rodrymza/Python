"""Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuanto deberá pagar finalmente por su compra."""

descuento=0.15

venta=float(input("Ingrese el monto del producto vendido: "))
print("El descuento aplicado es de", str(descuento*100) + "%")

descontado=round(venta*descuento,2)
valfinal=venta-descontado

print("El valor final del la venta es de $" + str(valfinal))
print("Usted de ahorro $" + str(descontado))
