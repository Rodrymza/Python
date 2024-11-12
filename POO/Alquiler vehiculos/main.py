from vehiculo import Auto
from vehiculo import Camioneta
from agenciaAlquiler import AgenciaAlquiler
from cliente import Cliente
class Main:
    def main():
        mi_agencia = AgenciaAlquiler("Todo automoviles")
        Main.cargar_vehiculos(mi_agencia)
        print(f"Bienvenido a la agencia {mi_agencia.nombre}")
        while True:
            Main.menu()
            opcion = input()
            match opcion:
                case "1":
                    mi_agencia.mostrar_disponibles()
                case "2":
                    nombre = input("Ingrese su nombre: ")
                    edad = int(input("Ingrese su edad: "))
                    cliente = Cliente(nombre, edad)
                    if cliente.getEdad() >= 21:
                        vehiculo_alquilar = Main.seleccionar_vehiculo(mi_agencia)
                        cliente.alquilar_vehiculo(vehiculo_alquilar)
                        print(f"Alquilaste {vehiculo_alquilar.marca} {vehiculo_alquilar.modelo}")
                        print(f"Precio por dia: {vehiculo_alquilar.costo_alquiler_diario}")
                        mi_agencia.agregar_cliente(cliente)
                    else:
                        print("No puedes alquilar un vehiculo si tienes menos de 21 años")
                case "3":
                    mi_agencia.mostrar_alquilados()
                case "4":
                    mi_agencia.total_ingresos()
                case "5":
                    mi_agencia.mostrar_lista_clientes()

    





    def cargar_vehiculos(agencia: AgenciaAlquiler):   
        autos = [("Toyota", "Corolla", 125, 4),
            ("Honda", "Civic", 125, 5),
            ("Ford", "Fusion", 135, 4),
            ("Nissan", "Altima", 140, 5),
            ("Chevrolet", "Cruze", 170, 4)]
        for marca, modelo, precio, puertas in autos:
            auto_agregar = Auto(marca, modelo, precio, puertas)
            agencia.agregar_auto(auto_agregar)
        print("Autos añadidos correctamente")

        camionetas = [("Ford", "F-150", 200, 1000),
              ("Chevrolet", "Silverado", 250, 1200),
              ("Ram", "1500", 220, 2500),
              ("Toyota", "Tacoma", 180, 900),
              ("Nissan", "Frontier", 200, 2400)]
        for marca, modelo, precio, capacidad in camionetas:
            camioneta_agregar = Camioneta(marca, modelo, precio, capacidad)
            camioneta_agregar.costo_capacidad_carga(2000)
            agencia.agregar_camioneta(camioneta_agregar)
        print("Camionetas añadidas correctamente")

    def menu():
        print("Seleccione una opcion: \n1 Mostrar vehiculos disponibles\n2 Alquilar vehiculos \n3 Mostrar vehiculos alquilados")
        print("4 Total de vehiculos alquilados \n5 Lista de clientes")
        
    def seleccionar_vehiculo(agencia: AgenciaAlquiler):
        lista_disponibles = agencia.mostrar_disponibles()
        while True:
            seleccion = input("Ingrese numero de vehiculo de la lista: ")
            try:
                seleccion = int(seleccion)
                if seleccion <= len(lista_disponibles) and seleccion >=1:
                    return lista_disponibles[seleccion-1]
                else:
                    print("Numero incorrecto")
            except:
                print("Valor incorrecto")

Main.main()