"""Crear la clase rectangulo atributos largo y ancho
crear metodos para calcular area y perimetro"""

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        return self.largo*self.ancho
    
    def perimetro(self):
        perimetro = (self.largo*2) + (self.ancho*2)
        return perimetro
rectangulo=Rectangulo(4,6)

print(f"El perimetro del rectangulo es {rectangulo.perimetro()}")
print(f"El area del rectangulo es {rectangulo.area()}")