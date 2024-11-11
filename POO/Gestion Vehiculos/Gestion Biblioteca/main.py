from biblioteca import Bilioteca
from seccion import Seccion
from libro import Libro
class Main:
    def __init__(self):
        pass
    def main(self):
        biblioteca = Bilioteca("belgrano".title())
        seccion_novelas = Seccion("Novelas")
        seccion_ciencia_ficcion = Seccion("Ciencia Ficcion")
        self.agregarLibrosSeccion(novelas, seccion_novelas)
        self.agregarLibrosSeccion(ciencia_ficcion, seccion_ciencia_ficcion )
        seccion_novelas.mostrar_seccion()
        seccion_ciencia_ficcion.mostrar_seccion()
        
    def agregarLibrosSeccion(self,lista: list, seccion: Seccion):
        for titulo, autor, precio in lista:
            libro = Libro(titulo, autor, precio)
            seccion.agregar_libro(libro)
    
novelas =[["El Quijote", "Miguel de Cervantes", 15.99],
    ["Don Quijote de la Mancha", "Miguel de Cervantes", 12.99],
    ["La Sombra del Viento", "Carlos Ruiz Zafón", 10.99],
    ["El Aleph", "Jorge Luis Borges", 9.99],
    ["Cien Años de Soledad", "Gabriel García Márquez", 14.99]
]

ciencia_ficcion = [["Dune", "Frank Herbert", 12.99], 
                   ["Fundación", "Isaac Asimov", 10.99], 
                   ["1984", "George Orwell", 9.99], 
                   ["El fin de la eternidad", "Isaac Asimov", 11.99], 
                   ["Neuromante", "William Gibson", 13.99]]


app = Main()
app.main()