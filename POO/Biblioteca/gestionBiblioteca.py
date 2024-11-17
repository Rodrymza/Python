from estante import Estante
from biblioteca import Biblioteca
from cliente import Cliente
from libro import Libro
def main():
    biblioteca = Biblioteca("Biblioteca Central")
    #cargar_clientes(biblioteca)
    #biblioteca.mostrar_clientes()
    while True:
        nuevo_estante = Estante(input("Ingresa el nombre del estante: "))
        cargar_libros(nuevo_estante, biblioteca)
        respuesta = input("Agregar mas estantes?: ")
        if respuesta.lower() == "n":
            break
    biblioteca.mostrar_biblioteca()
    
def crear_estante():
    nombre_estante = input("Ingresa el nombre del estante: ")
    nuevo_estante = Estante(nombre_estante)
    return nuevo_estante

def crear_libro():
    nombre = input("Ingresa el nombre del libro: ")
    autor = input("Ingresa el autor del libro: ")
    precio = float(input("Ingresa el precio del libro: "))
    nuevo_libro = Libro(nombre, autor, precio)
    return nuevo_libro

def cargar_clientes(biblioteca: Biblioteca):
    minimo_clientes = 3
    while True:
        documento = input("Ingresa el documento del cliente: ")
        nombre = input("Ingresa nombre y apellido del cliente: ")
        nuevo_cliente = Cliente(nombre, documento)
        
        if not biblioteca.cliente_en_lista(nuevo_cliente):
            biblioteca.agregar_cliente(nuevo_cliente)
        else:
            print("El cliente ya existe")
        respuesta = input("¿Desea agregar mas clientes (s/n): ")
        if respuesta.lower() == "n":
            if biblioteca.minimo_clientes():
                return
            else:
                print(f"Debes agregar al menos {minimo_clientes} clientes")
                
def crear_libro():
        nombre = (input("Ingresa nombre del libro: "))
        autor = input("Ingresa autor del libro: ")
        precio = float(input("Ingresa precio del libro: "))
        libro = Libro(nombre, autor, precio)
        return libro
        
def cargar_libros(estante: Estante, biblioteca: Biblioteca):
    valor_maximo_biblioteca = 5000
    while True:
        libro: Libro = crear_libro()
        if biblioteca.calcular_costo_biblioteca() + estante.calcular_costo_estante() + libro.precio <= valor_maximo_biblioteca:
            if not estante.libro_en_estante(libro):
                estante.agregar_libro(libro)
            else:
                print("El libro ya existe en el estante")
        else:
            print("Se supero el valor maximo de la biblioteca, no se agrego el libro")
        respuesta = input("Agregar mas libros?: ")
        if respuesta.lower() == "n":
            break
    biblioteca.agregar_estante(estante)        

if __name__ == "__main__":
    main()