class Cliente:
    def __init__(self,nombre: str, numero: str):
        self.nombre = nombre.title()
        self.numero = numero
        
    def mostrar_cliente(self):
        print(f"Cliente: {self.nombre} DNI: {self.numero}")