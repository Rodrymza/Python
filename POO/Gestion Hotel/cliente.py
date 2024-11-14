class Cliente:
    def __init__(self, nombre: str, documento: str):
        self.nombre = nombre
        self.documento = documento
        
    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Documento: {self.documento}"