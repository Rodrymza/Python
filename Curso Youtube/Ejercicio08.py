"""Tablas de multiplicar"""

num=input("Ingresa numero para ver la tabla de multiplicar\n")
if num.isnumeric():
    num=int(num)
    for i in range(1,10):
        print(f"{num}x{i} = {num*i}")
else:
    print("No ingresaste un numero")
    