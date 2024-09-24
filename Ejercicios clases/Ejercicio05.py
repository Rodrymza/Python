"""Crear una clase pago con atributo monto y un metodo procesar pago que muestre el mensaje:
procesando pago de x monto
crear clases derivadas pagoefectivo y pagotarjeta, pagotarjeta añade un atributo adicional llamado numero de tarjeta
y modifica procesando pago agregando el numero de tarjeta"""

class Pago:
    def __init__(self, monto):
        self.monto = monto
        
    def procesar_pago(self):
        print(f"Procesando pago de ${self.monto}")
        
class PagoEfectivo(Pago):
    pass

class PagoTarjeta(Pago):
    def __init__(self, monto, numero):
        super().__init__(numero)
        self.numero = numero
    
    def procesar_pago(self):
        print(f"Procesando pago ${self.monto}. Tarjeta N° {self.numero}")
        
efectivo_1=PagoEfectivo(3500)
efectivo_1.procesar_pago()

tarjeta_1=PagoTarjeta(4500, 44393243424)
tarjeta_1.procesar_pago()