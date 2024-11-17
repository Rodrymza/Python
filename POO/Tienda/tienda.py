from cliente import Cliente
from producto import Producto
from pedido import Pedido

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_productos = []
        self.lista_cliente: dict = {}
        self.lista_pedidos = []
        
    def agregar_producto(self, producto: Producto):
        if not self.producto_duplicado(producto):
            self.lista_productos.append(producto)
            print(f"Producto {producto.nombre} añadido")
        else:
            print("El producto ya se encuentra en la lista")
    
    def eliminar_producto(self, producto: Producto):
            if producto in self.lista_productos:
                print(f"Producto {producto.nombre} eliminado")
                self.lista_productos.remove(producto)
            else:
                print(f"Producto {producto.nombre} no encontrado")
                
    def registrar_cliente(self, cliente: Cliente):
        if not self.lista_cliente.get(cliente.documento):
            self.lista_cliente[cliente.documento] = cliente
        else:
            print("El DNI ya se encuentra asociado a un cliente existente")
    
    def agregar_pedido(self, pedido: Pedido):
        self.lista_pedidos.append(pedido)
        print("Pedido agregado a la tienda")
        
    def mostrar_productos(self):
        for indice, producto in enumerate(self.lista_productos,start=1):
            print(f"{indice} - {producto}")
            
    def producto_duplicado(self, producto_nuevo: Producto):
        producto: Producto
        for producto in self.lista_productos:
            if producto_nuevo.nombre == producto.nombre:
                return True
            
    