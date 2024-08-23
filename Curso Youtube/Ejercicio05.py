#Factorial y sucesion de Fibonacci
num=""
while not num.isnumeric():
    num=input("Ingresa un numero para ver su factorial\n")
if num.isnumeric():
    fact=1
    num=int(num)
    for i in range(1,num+1):
        fact*=i
    print(f"El factorial de {num} es {fact}")
else:
    print("No ingresaste un numero")

for i in range(0,50):
    if i==0 or i==1:
        fib=i
    else:
        fib=(i-1)+(i-2)
    print(fib,end=" ")

    


