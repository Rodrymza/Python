from piso import Piso
class Edificio:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.totalMetrosCubiertos = 0.0
        self.costoTotalConstruccion = 0.0
        self.lista_pisos = []

    def calcular_metros_cubiertos(self):
        for piso in self.lista_pisos:
            self.totalMetrosCubiertos += piso.total_superficie_piso()

    def total_costo_construccion(self):
        for piso in self.lista_pisos:
            self.costoTotalConstruccion += piso.calcular_costo_piso()
    
    def agregar_piso(self, piso_nuevo):
        self.lista_pisos.append(piso_nuevo)

    def mostrar_edificio(self):
        print(self.nombre.center(30,"-"))
        for piso in self.lista_pisos:
            piso.mostrar_departamentos()



