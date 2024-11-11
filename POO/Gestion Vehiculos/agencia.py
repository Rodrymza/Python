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
        if not self.mayor_a_maximo():
            self.lista_vehiculos.append(auto)
            print("Auto agregado correctamente")
        else:
            print("No se pudo agregar el auto, se supero el maximo")

    def agregar_camion(self):
        camion = Camion()
        camion.pedir_datos()
        if not self.mayor_a_maximo():
            self.lista_vehiculos.append(camion)
            print("Camión agregado correctamente")
        else:
            print("No se pudo agregar el camion, se supero el maximo")
        

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
        if not self.mayor_a_maximo():
            self.lista_vehiculos.append(vehiculo)
        else:
            print("No se pudo agregar el vehiculo, se supero el maximo")
        
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
            
    def mayor_a_maximo(self, maximo):
        return maximo >= len(self.lista_vehiculos)
