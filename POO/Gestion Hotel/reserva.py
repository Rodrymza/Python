from cliente import Cliente
from habitacion import Habitacion
class Reserva:
    def __init__(self, cliente: Cliente, numero_noches: int, habitacion: Habitacion, numero_huespedes: int):
        self.cliente = cliente
        self.numero_noches = numero_noches 
        self.habitacion = habitacion
        self.numero_huespedes = numero_huespedes
        
    def costo_reserva(self):
        return self.numero_noches * self.habitacion.costo_por_noche
    
    def mostrar_reserva(self):
        print(f"Reserva de {self.cliente.nombre} para {self.numero_noches} noches")
        print(f"Total de huespedes: {self.numero_huespedes}")
        print(f"Costo total estadia ${self.costo_reserva()}")
    