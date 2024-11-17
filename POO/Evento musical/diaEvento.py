from escenario import Escenario
class DiaEvento:
    def __init__(self, numero_dia):
        self.numero_dia = numero_dia
        self.escenarios = []
        
    def calcular_costo_dia(self):
        costo = 0
        escenario: Escenario
        for escenario in self.escenarios:
            costo += escenario.calcular_costo_escenario()
        return costo
            
    def mostrar_dia(self):
        print(f"Escenarios del dia {self.numero_dia}")
        escenario: Escenario
        for escenario in self.escenarios:
            escenario.mostrar_escenario()
        print("".center(30,"-"))
        
    def agregar_escenario(self, escenario_agregar: Escenario):
        self.escenarios.append(escenario_agregar)
        print(f"Escenario {escenario_agregar.nombre_escenario} agregado")
        
    def total_presentaciones_dia(self):
        total = 0
        escenario: Escenario
        for escenario in self.escenarios:
            total += escenario.total_presentaciones()
        return total
    
    def maximo_escenarios(self, maximo = 3):
        return  len(self.escenarios) == maximo
