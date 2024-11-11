class Planta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.area = 0
        self.sectores = []
        
    def total_area_planta(self):
        self.area = sum([sector.area for sector in self.sectores])
            
    def mayor_a_maximo(self, maximo: int):
        return self.total_area_planta() > maximo
    
    def mostrar_detalles(self):
        print("".center(20, "-"))
        for sector in self.sectores:
            sector.mostrar_informacion()
        print(f"Area total {self.total_area_planta()}m2")
        print("".center(20, "-"))
        
    def agregar_sector(self, nuevo_sector):
        self.sectores.append(nuevo_sector)
        print(f"Se agrego el nuevo sector {nuevo_sector.nombre}")
