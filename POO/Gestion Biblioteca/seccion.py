class Seccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        
    def agregar_libro(self, libro):
        self.libros.append(libro)
        
    def mostrar_seccion(self):
        print("".center(25, "-"))
        print(f"Seccion {self.nombre}")
        print("".center(25, "-"))
        for libro in self.libros:
            print(libro.titulo, libro.autor, sep=" - ")
        print("".center(25, "-"))