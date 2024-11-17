from diaEvento import DiaEvento
class EventoMusical:
    def __init__(self, nombre):
        self.nombre = nombre
        self.total_costo = 0
        self.lista_de_dias = []
        
    def calcular_costo_total(self):
        self.total_costo = 0
        dia: DiaEvento
        for dia in self.lista_de_dias:
            self.total_costo += dia.calcular_costo_dia()
            
    def mostrar_evento(self):
        dia: DiaEvento
        print("".center(30,"-"))
        print(f"Evento: {self.nombre}")
        print("".center(30,"-"))
        for dia in self.lista_de_dias:
            dia.mostrar_dia()
        print(f"Costo total del evento ${self.total_costo}")
        print(f"Costo promedio por presentacion ${self.promedio_por_presentacion()}")
        print(f"Costo promedio por dia ${self.promedio_por_dia()}")
            
    def validar_costo_maximo(self, maximo = 500000):
        self.calcular_costo_total()
        return self.total_costo <= maximo
    
    def agregar_dia(self, dia_agregar: DiaEvento):
        self.lista_de_dias.append(dia_agregar)
        print(f"Dia {dia_agregar.numero_dia} agregado")
        
    def validar_cantidad_dias(self, minimo: int = 1, maximo: int = 7):
        return minimo <= len(self.lista_de_dias) <= maximo
    
    def promedio_por_dia(self):
        return round(float(self.total_costo  / len(self.lista_de_dias)),2)
    
    def promedio_por_presentacion(self):
        return round(float(self.total_costo / self.total_presentaciones_evento()))
        
    def total_presentaciones_evento(self):
        dia: DiaEvento
        total = 0
        for dia in self.lista_de_dias:
            total += dia.total_presentaciones_dia()
        print("Total presentacions", total)
        return total