class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def __str__(self):
         return f"{self.nombre:<15}${self.precio:<8}{self.cantidad:<8}"
