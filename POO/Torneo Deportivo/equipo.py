class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        
    def actualizar_puntos(self, puntos:int):
        self.puntos += puntos
    
    def __str__(self):
        return f'{self.nombre} {self.puntos}'