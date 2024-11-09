class Vehiculo:
    def __init__(self) -> None:
        self.marca = ""
        self.modelo = ""
        self.precio = ""
        
    
    def mostrar_detalles(self):
        pass

    def pedir_datos():
        pass
class Auto(Vehiculo):
    def __init__(self) -> None:
        super().__init__()
        self.cantidad_puertas = 0

    def mostrar_detalles(self):
        print(f"Auto: {self.marca} {self.modelo} \nPrecio: {self.precio}\nCantidad de puertas: {self.cantidad_puertas}")

    def pedir_datos(self):
        self.marca = input("Ingrese la marca: ")
        self.modelo = input("Ingrese el modelo: ")
        self.precio = float(input("Ingrese el precio: "))
        self.cantidad_puertas = int(input("Ingrese la cantidad de puertas: "))

class Camion(Vehiculo):
    def __init__(self) -> None:
        super().__init__()
        self.capacidad_carga = 0
    def mostrar_detalles(self):
        print(f"Camion: {self.marca} {self.modelo} \nPrecio: {self.precio}\nCapacidad de carga: {self.capacidad_carga}")

    def pedir_datos(self):
        self.marca = input("Ingrese la marca: ")
        self.modelo = input("Ingrese el modelo: ")
        self.precio = float(input("Ingrese el precio: "))
        self.capacidad_carga = int(input("Ingrese la capacidad de carga: "))
