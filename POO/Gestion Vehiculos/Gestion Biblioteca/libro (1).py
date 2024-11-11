class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}")
        