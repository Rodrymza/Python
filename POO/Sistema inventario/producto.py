class Producto:
    def __init__(self):
        self.nombre = ""
        self.precio = 0
        self.cantidad = 0
        
    def anadir_datos(self):
        self.nombre = input("Ingresa nombre del producto\n").title()
        self.precio = float(input("Ingresa precio del producto\n"))
        self.cantidad = int(input("Ingresa cantidad\n"))
        
    def modificar_cantidad(self, cantidad):
        if self.cantidad + cantidad >= 0:
            self.cantidad += cantidad
            print("Stock actualizado")
        elif self.cantidad - cantidad < 0:
            print("Stock insuficiente")

    
    def anadir_producto_lista(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio        
        
        