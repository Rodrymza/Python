class Nota:
    def __init__(self, valor: int, catedra: str):
        self.valor = valor
        self.catedra = catedra
        
    def mostrar_nota(self):
        print(f"Materia: {self.nombre} Nota: {self.valor}")