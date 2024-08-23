def imprimir_simbolo(simbolo,veces):
    for i in range(veces):
        print(simbolo,end=" ")
        
simbolo=input("Ingrese simbolo o letra a repetir: ")
veces=int(input(f"Ingrese las veces que quiere repetir {simbolo}: "))

imprimir_simbolo(simbolo,veces)