class Sector:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area
        
    def mostrar_informacion(self):
        print(f"Sector: {self.nombre} \nArea {self.area}m2")