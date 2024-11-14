from habitacion import Habitacion
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        
    def total_huespedes(self):
        pass
    
    def ingreso_total(self):
        pass
    
    def agregar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)
    
    def mostrar_habitaciones(self):
        habitacion: Habitacion
        for habitacion in self.habitaciones:
            habitacion.mostrar_habitacion()
            
    def lista_habitaciones_libres(self):
        disponibles = False
        habitacion: Habitacion
        for i, habitacion in enumerate(self.habitaciones, start= 1):
            if not habitacion.ocupada:
                print(f"{i} - {habitacion.tipo} ${habitacion.costo_por_noche}")
                disponibles = True
        return disponibles
                
    def comprobar_disponibilidad(self, huespedes: int):
        habitacion: Habitacion
        for habitacion in self.habitaciones:
            if habitacion.capacidad >= huespedes:
                return True
        return False
    
    def mostrar_todas_habitaciones(self):
        habitacion: Habitacion
        for i,habitacion in enumerate(self.habitaciones, start = 1):
            print("".center(30,"*"))
            print(f"{i} - {habitacion.tipo}\n Capacidad: {habitacion.capacidad} Precio: ${habitacion.costo_por_noche}")
            print(f"Disponibilidad: {habitacion.texto_ocupada}")