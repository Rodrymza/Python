from vehiculo import Auto
from vehiculo import Camioneta
from cliente import Cliente
class AgenciaAlquiler:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.vehiculos = []
        self.lista_clientes = []

    def alquilar_vehiculo(self):
        pass

    def agregar_auto(self, auto_agregar: Auto):
        self.vehiculos.append(auto_agregar)
        print(f"Auto {auto_agregar.marca} {auto_agregar.modelo} añadido")

    def agregar_camioneta(self, camioneta_agregar: Camioneta):
        self.vehiculos.append(camioneta_agregar)
        #print(f"Camioneta {camioneta_agregar.marca} {camioneta_agregar.modelo} añadida")

    def mostrar_alquilados(self):
        lista_alquilados = [vehiculo for vehiculo in self.vehiculos if vehiculo.alquilado]
        print("Vehiculos alquilados")
        for vehiculo in lista_alquilados:
            print(f"{vehiculo.marca} {vehiculo.modelo} ${vehiculo.costo_alquiler_diario} por dia")

    def mostrar_disponibles(self):
        lista_disponibles = [vehiculo for vehiculo in self.vehiculos if not vehiculo.alquilado]
        i = 1
        print("Vehiculos disponibles")
        for vehiculo in lista_disponibles:
            print(f"{i} - {vehiculo.marca} {vehiculo.modelo}")
            i += 1
        return lista_disponibles
    
    def total_ingresos(self):
        total = sum([vehiculo.costo_alquiler_diario for vehiculo in self.vehiculos if not vehiculo.disponible()])
        print(f"El costo total de ganancia de hoy por los vehiculos alquilados es de ${total}")

    def agregar_cliente(self, cliente: Cliente):
        self.lista_clientes.append(cliente)

    def mostrar_lista_clientes(self):
        print("Lista clientes:")
        for cliente in self.lista_clientes:
            print(f"Cliente: {cliente.nombre}")
            cliente.mostrar_vehiculo()