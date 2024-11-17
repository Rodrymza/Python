from presentacion import Presentacion
class Escenario:
    def __init__(self, nombre_escenario):
        self.nombre_escenario = nombre_escenario
        self.presentaciones = []
        
    def calcular_costo_escenario(self):
        costo = 0
        presentacion: Presentacion
        for presentacion in self.presentaciones:
            costo += presentacion.costo
        return costo
    
    def mostrar_escenario(self):
        print("".center(30,"-"))
        print(f"    {self.nombre_escenario}:")
        presentacion: Presentacion
        for presentacion in self.presentaciones:
            presentacion.mostrar_presentacion()
        print("".center(30,"-"))
        
        
    def validar_minimo_presentaciones(self, minimo=2):
        return len(self.presentaciones) >= minimo
    
    def agregar_presentacion(self, presentacion_agregar: Presentacion):
        self.presentaciones.append(presentacion_agregar)
        print(f"Presentacion de {presentacion_agregar.artista} agregada")
        
    def validar_artista_duplicado(self, presentacion_verificar: Presentacion):
        presentacion: Presentacion
        for presentacion in self.presentaciones:
            if presentacion.artista == presentacion_verificar.artista:
                return True
        return False
    
    def total_presentaciones(self):
        return len(self.presentaciones)
