productos = {}
for i in range(1):
    ingreso_usuario = "fruta:manzana fruta:naranja fruta:mandarina"
    dato = tuple(ingreso_usuario.split(" "))
    for elemento in dato:
            valores = elemento.split(":")
            if productos.get(valores[0]):
                  productos[valores[0]].append(valores[1])
            else:
                  lista = []
                  lista.append(valores[1])
                  productos[valores[0]] = lista

print(productos)