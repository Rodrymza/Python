

total=int(input("Ingrese cantidad de empleados a ingresar: "))
nombres=[]
sueldos=[]
for i in range(total):
    nombres.append(input(f"Ingrese apellido del empleado {i+1}: "))
    sueldos.append(input(f"Ingrese el sueldo del empleado {nombres[i]}: "))
    
for i in range(total):
    print(f"{nombres[i]} \t${sueldos[i]}")


  