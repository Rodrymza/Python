from cliente import Cliente
from habitacion import Habitacion
from hotel import Hotel
from reserva import Reserva
class Main:
    def __init__(self):
        self.hotel = Hotel("Hotel La Libetad")
        
    def main(self):
        self.crear_habitaciones()
        while True:
            opcion = input("Seleccione opcion: \n1 Hacer reserva \n2 Mostrar todas habitaciones\n")
            match opcion:
                case "1":
                    nueva_reserva = self.crear_reserva()
                    if nueva_reserva:
                        nueva_reserva.mostrar_reserva()
                    else:
                        print("No se pudo realizar la reserva")
                case "2":
                    self.hotel.mostrar_todas_habitaciones()
                case _:
                    print("Opcion no valida")
        
    
    def crear_habitaciones(self):
        habitaciones = [
    ["Suite", 150, 5],  # Habitación 1
    ["Sencilla", 80, 2],  # Habitación 2
    ["Doble", 120, 4],  # Habitación 3
    ["Suite", 150, 5],  # Habitación 4
    ["Sencilla", 80, 2],  # Habitación 5
    ["Doble", 120, 4],  # Habitación 6
    ["Suite", 150, 5],  # Habitación 7
    ["Sencilla", 80, 2],  # Habitación 8
    ["Doble", 120, 4],  # Habitación 9
    ["Suite", 150, 5]   # Habitación 10
]
        for i, habitacion in enumerate(habitaciones, start=1): 
            tipo, precio, capacidad = habitacion
            nueva_habitacion = Habitacion(i, tipo, precio, capacidad)
            self.hotel.agregar_habitacion(nueva_habitacion)

        print(f"Se agrego un total de {i} habitaciones")
    
    def crear_reserva(self):
        cliente: Cliente = Main.crear_cliente()
        while True:
            numero_huespedes = int(input("Ingrese la cantidad de huespedes: "))
            if self.hotel.comprobar_disponibilidad(numero_huespedes):
                numero_noches = int(input("Ingrese el numero de noches: "))
                habitacion: Habitacion = self.seleccionar_habitacion(numero_huespedes)
                reserva = Reserva(cliente, numero_noches, habitacion, numero_huespedes)
                return reserva
            else: 
                print("No existe disponibilidad para la cantidad de huespedes")
                respuesta = input("Desea continuar con el proceso? ")
                if respuesta == "n":
                    return None
        
    def seleccionar_habitacion(self, minimo_huespedes: int):
        print("Habitaciones disponibles:")
        habitacion: Habitacion
        i = 1
        for habitacion in self.hotel.habitaciones:
            if habitacion.capacidad >= minimo_huespedes and habitacion.disponible():
                print(f"{i} - {habitacion.tipo} ${habitacion.costo_por_noche} Capacidad:{habitacion.capacidad} ***{habitacion.texto_ocupada}***")
            i += 1
        while True:
            try:
                opcion = int(input("Seleccione habitacion: "))
                if opcion > 0 and opcion <= len(self.hotel.habitaciones):
                    habitacion: Habitacion = self.hotel.habitaciones[opcion-1]
                    if habitacion.disponible():
                        habitacion.reservar()
                        return habitacion 
                    else: 
                        print("Habitacion no disponible")
                else:
                    print("Habitacion invalida")
            except:
                print("Opcion invalida")
                
    def crear_cliente():
        nombre = input("Ingrese nombre: ")
        documento = input("Ingrese su documento: ")
        return Cliente(nombre, documento)
            
app = Main()
app.main()