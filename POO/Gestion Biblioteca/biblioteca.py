from libro import Libro
from seccion import Seccion
class Bilioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_secciones =[Seccion]
        
    def calcular_valor_total(self):
        return sum([libro.precio for libro in self.lista_libros])
    
    def agregar_libro(self, libro: Libro):
        self.lista_libros.append(libro)