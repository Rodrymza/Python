class Nota:
    def __init__(self, valor: int, descripcion: str):
        self.valor = valor
        self.catedra = descripcion
        
    def mostrar_nota(self):
        print(f"Descripcion: {self.descripcion} Nota: {self.valor}")
        
