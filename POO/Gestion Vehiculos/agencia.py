from vehiculo import Vehiculo
from vehiculo import Auto
from vehiculo import Camion
class Agencia:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.lista_vehiculos = []

    def agregar_auto(self):
        auto = Auto()
        auto.pedir_datos()
        self.lista_vehiculos.append(auto)
        print("Auto agregado correctamente")

    def agregar_camion(self):
        camion = Camion()
        camion.pedir_datos()
        self.lista_vehiculos.append(camion)
        print("Camión agregado correctamente")

    def valor_total_agencia(self):
        suma = 0
        for vehiculo in self.lista_vehiculos:
            suma += vehiculo.precio
        return suma

    def total_autos(self):
        total_autos= 0
        for auto in self.lista_vehiculos:
            if isinstance(auto, Auto):
                          total_autos += 1
        return total_autos
    
    def total_camiones(self):
        total_camiones = 0
        for camion in self.lista_vehiculos:
            if isinstance(camion, Camion):
                total_camiones += 1
        return total_camiones
    
    def agregar_vehiculo(self, vehiculo):
         self.lista_vehiculos.append(vehiculo)
        
    def verificar_maximo_vehiculos(self, maximo):
        if len(self.lista_vehiculos) < maximo:
            return True
        else:
            return False

    def mostrar_vehiculos(self):
        i = 1
        for vehiculo in self.lista_vehiculos:
            print(f"{vehiculo.marca} {vehiculo.modelo}")
            i += 1
