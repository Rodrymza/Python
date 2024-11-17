class Cliente:
    def __init__(self, nombre, correo, documento):
        self.nombre = nombre
        self.correo = correo
        self.documento = documento
        self.pedidos = []
        
    def __str__(self):
        return f"{self.documento} - {self.nombre}"
    
    def agregar_pedido(self, pedido_nuevo):
        self.pedidos.append(pedido_nuevo)
        
