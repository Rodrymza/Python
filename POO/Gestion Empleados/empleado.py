class Empleado:
    salario_base = 800
    salario = 0.0
    def __init__(self, nombre):
        self.nombre = nombre
        
    def calcular_salario(self):
        pass
    
class EmpleadoTpoCompleto(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def calcular_salario(self):
        self.salario = self.salario_base + 200
        
        
class EmpleadoParcial(Empleado):
    def calcular_salario(self):
        self.salario = self.salario_base + (50)
    