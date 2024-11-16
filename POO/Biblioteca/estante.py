from libro import Libro
class Estante:
    def __init__(self, nombre: str):
        self.nombre = nombre.title()
        self.lista_de_libros = []
        
    def agregar_libro(self, libro: Libro):
        libro: Libro
        if not self.libro_en_estante(libro):
            self.lista_de_libros.append(libro)
            print(f"Libro {libro.nombre} agragado al estante {self.nombre}")
        else:
            print(f"El libro {libro.nombre} ya se encuentra en el estante")
            
    def libro_en_estante(self, libro: Libro):
        libro_estante : Libro
        for libro_estante in self.lista_de_libros:
            if libro_estante.nombre == libro.nombre:
                return True
        return False
    
    def mostrar_estante(self):
        print(f"El estante {self.nombre} tiene los siguientes libros:")
        libro: Libro
        for libro in self.lista_de_libros:
            libro.mostrar_libro()
        print(f"Valor total de estante ${self.calcular_costo_estante()}")
        print("".center(30,"-"))
            
    def calcular_costo_estante(self):
        costo = 0
        libro: Libro
        for libro in self.lista_de_libros:
            costo += libro.precio
        return costo