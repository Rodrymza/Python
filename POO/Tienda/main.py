from cliente import Cliente
from tienda import Tienda
from pedido import Pedido
from producto import Producto
def main():
    mi_tienda = crear_tienda()
    agregar_productos(mi_tienda)
    agregar_clientes(mi_tienda)
    while True:
        print("Crendo un nuevo pedido")
        pedido:Pedido = crear_pedido()
        pedido.mostrar_pedido()
        mi_tienda.agregar_pedido(pedido)
        mi_tienda.calcular_total()
    
    
def crear_tienda():
    nombre = input("Ingresa el nombre de la tienda: ")
    return Tienda(nombre)

def agregar_productos(tienda: Tienda):
    pass

def agregar_clientes(tienda: Tienda):
    pass

def crear_pedido(tienda: Tienda):
    pass

def agregar_pedidos(pedido: Pedido):
    pass


    
    