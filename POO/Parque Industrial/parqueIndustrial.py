class ParqueIndustrial:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.plantas = []
        
    def total_area(self):
        return sum([planta.total_area_planta() for planta in self.plantas])
    
    def agregar_planta(self, planta):
        self.plantas.append(planta)
        print(f"Se agregó la planta {planta.nombre}")
        
    def mayor_a_maximo(self, maximo: int):
        return self.total_area() > maximo
    
    def mostrar_parque(self):
        print(f"Parque Industrial: {self.nombre}")
        for planta in self.plantas:
            planta.mostrar_detalles()
        