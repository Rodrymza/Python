from vehiculo import Auto
from vehiculo import Camioneta
from vehiculo import Vehiculo
class Cliente:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad
        self.vehiculo_alquilado = None

    def getEdad(self):
        return self.edad

    def alquilar_vehiculo(self, vehiculo: Vehiculo):
        if vehiculo.disponible():
            vehiculo.marcar_alquilado()
            self.vehiculo_alquilado = vehiculo

    def mostrar_vehiculo(self):
        print(f"Vehiculo alquilado: {self.vehiculo_alquilado.marca} {self.vehiculo_alquilado.modelo}")
