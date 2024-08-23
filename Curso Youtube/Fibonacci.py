def fibonacci(numero):
    if numero<=1:
        resultado=numero
    else:
        resultado=fibonacci(numero-1)+fibonacci(numero-2)
    return resultado

for i in range(1,10):
    print(fibonacci(i),end=" ")