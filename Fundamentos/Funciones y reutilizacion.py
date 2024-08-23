def calcular_resto(x,y):
    return x - y * (x // y)

def es_multiplo(a,b):
    return calcular_resto(a,b)== 0

num1=int(input("Ingresa un numero: "))
num2=int(input("Ingresa otro numero: "))

print(f"El resto entre {num1} y {num2} es {calcular_resto(num1,num2)}")

if es_multiplo(num1,num2):
    print(f"{num1} es multiplo de {num2}")