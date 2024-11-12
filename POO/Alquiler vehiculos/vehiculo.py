class Vehiculo:
    def __init__(self, marca: str, modelo: str, costo_alquiler_diario: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.costo_alquiler_diario = costo_alquiler_diario
        self.alquilado = False

    def mostrar_informacion(self):
        print(f"Vehiculo: {self.marca} {self.modelo} \nCosto Diario ${self.costo_alquiler_diario}")

    def marcar_alquilado(self):
        self.alquilado = True

    def marcar_disponible(self):
        self.alquilado = False

    def disponible(self):
        return not self.alquilado
    
class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: str, costo_alquiler_diario: float, puertas: int) -> None:
        super().__init__(marca, modelo, costo_alquiler_diario)
        self.puertas = puertas

    def mostrar_informacion(self):
        print(f"Tipo de vehiculo: Automovil {self.puertas} puertas")
        return super().mostrar_informacion()

    def alquiler_auto(self):
        pass
class Camioneta(Vehiculo):
    def __init__(self, marca: str, modelo: str, costo_alquiler_diario: float, capacidad_carga: int) -> None:
        super().__init__(marca, modelo, costo_alquiler_diario)
        self.capacidad_carga = capacidad_carga
    
    def mostrar_informacion(self):
        print(f"Tipo de vehiculo: Camioneta, capacidad carga: {self.capacidad_carga} kg")
        return super().mostrar_informacion()
    
    def alquilar_camioneta(self):
        pass

    def costo_capacidad_carga(self, maximo: int):
        impuesto_carga = 1.2
        if self.capacidad_carga > maximo:
            self.costo_alquiler_diario *= impuesto_carga