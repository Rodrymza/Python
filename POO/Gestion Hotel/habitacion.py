class Habitacion:
    def __init__(self, numero, tipo, costo_por_noche, capacidad):
        self.numero = numero
        self.tipo = tipo
        self.costo_por_noche = costo_por_noche
        self.capacidad = capacidad
        self.ocupada = False
        self.texto_ocupada = "Libre"
    
    def reservar(self):
        if self.ocupada == False:
            self.ocupada = True
            self.texto_ocupada = "Ocupada"
        else:
            print("La habitacion se encuentra ocupada")
            
    def liberar(self):
        self.ocupada = False
        self.texto_ocupada = "Libre"
    
    def mostrar_habitacion(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        print("".center(30,"-"))
        print(f"Habitacion {self.numero}: {self.tipo}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Costo por noche ${self.costo_por_noche}")
        print(f"Condicion: {estado}")
    
    def disponible(self):
        return True if not self.ocupada else False 