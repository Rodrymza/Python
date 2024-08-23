#Ordenar mayor a menor

a=int(input("Ingresa el primer numero: "))
b=int(input("Ingresa el segundo numero: "))
c=int(input("Ingresa el tercer numero: " ))

if a>b and a>c:
    if b>c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b>a and b>c:
    if a>c:
        print(b,a,c) 
    else:
        print(b,c,a)
elif c>a and c>b:
    if a>b:
        print(c,a,b)
    else:
        print(c,b,a)
        
