class Libro:
    def __init__(self,nombre: str, autor: str, precio: float):
        self.nombre = nombre.title()
        self.autor = autor.title()
        self.precio = precio
        
    def mostrar_libro(self):
        print(f"{self.nombre} - {self.autor} Precio ${self.precio}")
        
    def modificar_precio(self, nuevo_precio: float):
        print(f"Se modifico el precio de ${self.precio} a ${nuevo_precio}")
        self.precio = nuevo_precio
        