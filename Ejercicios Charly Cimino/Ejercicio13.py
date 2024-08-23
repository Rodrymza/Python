
base=int(input("Ingrese el tamaño de la base de la piramide: "))

while base<3 or base%2==0:
    base=int(input("Ingrese un numero impar mayor a 3: "))

n=base//2
espacioant=" " * n
espaciopost=" " * n
asteriscos="*"


while n!=-1:
    print(espacioant + asteriscos + espaciopost)
    n=n-1
    asteriscos+="**"
    espacioant=" " * n
    espaciopost=" " * n
    



  