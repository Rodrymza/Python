#Sucesion de Fibonacci hasta 1597 en 7 lineas de codigo
num1, num2 = 0, 1
while num2<=1597:
    print(f"{num1} {num2}",end=" ")
    num1=num1+num2
    num2=num2+num1
