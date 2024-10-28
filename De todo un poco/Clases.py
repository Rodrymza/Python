class Biblioteca:
    def __init__(self):
        self.catalogo= {}
        
    def agregar_libro(self, titulo, autor):
        if not self.catalogo.get(titulo):
            self.catalogo[titulo.capitalize()] = autor.title()
            
    def mostrar_libros(self):
        print("Catalogo de Libros")
        for titulo, autor in self.catalogo.items():
            print(f"{titulo} - {autor}")
    
    def eliminar_libro(self):
        self.mostrar_libros()
        print("Escriba nombre del titulo a eliminar")
        titulo = input()
        try:
            self.catalogo.pop(titulo.capitalize())
            print(f"Libro '{titulo.capitalize()}' eliminado")
        except:
            print("El titulo no existe")
            

            
            
class Pedido:
    def __init__(self):
        self.items = []
        self.nombre = ""
        self.total = 0
    def agregar_item(self, plato, precio):
        self.items.append((plato, precio))
        print(f"Item {plato} agregado")
        
    def mostrar_pedido(self):
        for elemento in self.items:
            print(*elemento, sep =" $")
            
    def calcular_total(self):
        total = 0
        for i in range(len(self.items)):
               total += self.items[i][1]
        self.total = total
        print("Total a pagar$", self.total)
pedido = Pedido()
pedido.agregar_item("Papas fritas", 4500)
pedido.agregar_item("Milanesa con papas", 9500)

pedido.mostrar_pedido()
pedido.calcular_total()