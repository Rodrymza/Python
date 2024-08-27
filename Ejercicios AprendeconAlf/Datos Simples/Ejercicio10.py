peso_payaso=112
peso_muneca=75

cant_munecas=int(input("Ingrese la catidad de muñecas en el pedido \n"))
cant_payasos=int(input("Ingrese la catidad de payasos en el pedido \n"))

peso_total=((cant_munecas*peso_muneca)+(cant_payasos*peso_payaso))/1000

print(f"El peso total sera de {peso_total} kg")