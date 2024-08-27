precio_pan=3.65
descuento=0.6

cantidad=int(input("Ingrese la cantidad de pan fresco vendida\n"))
total_fresco=cantidad*precio_pan

cantidad=int(input("Ingrese la cantidad de pan vendida que no era del dia \n"))
total_descuento=cantidad*precio_pan*descuento

print(f"Se vendio un total de ${total_fresco} de pan del dia, ${total_descuento} de pan en descuento\nEl total vendido fue ${total_descuento+total_fresco}")