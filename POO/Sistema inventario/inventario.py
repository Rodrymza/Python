from producto import Producto
from prettytable import PrettyTable
class Inventario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_productos = {}
    
    def agregar_producto_lista(self, nombre, precio, cantidad):
        """nombre, precio y cantidad como parametros"""
        producto_anadir = Producto()
        producto_anadir.anadir_producto_lista(nombre, precio, cantidad)
        self.lista_productos[nombre] = producto_anadir
        
    def agregar_producto_manual(self):
        producto_agregar = Producto()
        producto_agregar.anadir_datos()
        self.lista_productos[producto_agregar.nombre] = producto_agregar
        
    def modificar_stock_producto(self, cantidad):
        self.mostrar_inventario()
        producto = input("Ingresa el producto a eliminar").title()
        if self.lista_productos.get(producto):
             self.lista_productos[producto].modificar_cantidad(cantidad)
             if self.lista_productos[producto] == 0:
                 print("Procto eliminado")
             else:
                 print("Stock actualizado")
             
        else:
            print(f"{producto.title()} no encontrado")
    
    def mostrar_inventario(self):
        tabla = PrettyTable()
        tabla.field_names = ["Nombre", "Precio", "Stock"]
        for nombre, producto in self.lista_productos.items():
            tabla.add_row([nombre, f"${producto.precio}", producto.cantidad])
        print(tabla)
    
    def valor_total_inventario(self):
        total = 0.0
        for nombre, producto in self.lista_productos.items():
            total += (producto.precio * producto.cantidad)
        print(f"El valor total del inventario es ${total}")
        
        