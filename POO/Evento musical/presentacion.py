class Presentacion:
    def __init__(self, artista: str, duracion: int, costo: float):
        self.artista = artista
        self.duracion = duracion
        self.costo = costo
        
    def mostrar_presentacion(self):
        print(f"{self.artista} {self.duracion} minutos  ${self.costo}")