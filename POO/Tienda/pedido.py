from cliente import Cliente
from producto import Producto
class Pedido:
    def __init__(self, fecha: str, cliente: Cliente):
        self.cliente = cliente
        self.fecha = fecha
        self.estado = "En espera"
        self.lista_productos = []
        
    def mostrar_pedido(self):
        texto = f"Pedido fecha: {self.fecha}\n"
        producto: Producto
        texto += f"{"Nombre":<15}{"Precio":<8}{"Cant":<8}{"Subtotal":<8}\n"
        for producto in self.lista_productos:
            subtotal = round(producto.cantidad * producto.precio, 2)
            texto += f"{producto}${subtotal:<8}\n"
        texto += f"{"Total del pedido":<32}${self.calcular_total_pedido()}"
        return texto
       
    def calcular_total_pedido(self):
        return sum([producto.precio*producto.cantidad for producto in self.lista_productos])
    
    def agregar_producto(self, producto: Producto):
        self.lista_productos.append(producto)
        
productos = [
    Producto("Manzana", 1.50, 10),
    Producto("Leche", 2.00, 5),
    Producto("Pan", 1.00, 8),
    Producto("Huevos", 1.20, 12),
    Producto("Queso", 3.00, 6)
]
     
