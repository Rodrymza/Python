def agregar_productos(productos, cantidad):
    for _ in range(cantidad):
        nombre = input("Ingrese nombre del producto\n").capitalize()
        precio = int(input(f"Ingrese precio de {nombre}\n"))
        stock = int(input(f"Ingrese stock de {nombre}\n"))
        productos[nombre] = {"precio": precio,"stock": stock}

def comprar_producto(productos):
    producto_a_comprar = input("Ingresa el producto a comprar\n").capitalize()
    if productos.get(producto_a_comprar):
        cantidad= int(input("Escribe cantidad a comprar\n"))
        if cantidad > productos[producto_a_comprar]["stock"]:
            print("No hay suficiente stock")
    else:
        productos[producto_a_comprar]["stock"] -= cantidad
        print("Total a pagar", productos[producto_a_comprar]["precio"]*cantidad, sep=" $")

def mostrar_inventario(productos):
    print("Inventario:")
    for clave in productos:
        print("\tProducto:", clave)
        print(f"Precio $ {productos[clave]["precio"]}")
        print(f"Stock {productos[clave]["stock"]}")

productos = {}
agregar_productos(productos,2)    
print(productos)
comprar_producto(productos)
comprar_producto(productos)
comprar_producto(productos)
mostrar_inventario(productos)