from agencia import Agencia
from vehiculo import Auto
class Main:
    def main():
        mi_agencia = Agencia("Automotores 360")
        while True:
            print("Selecciona una opcion:\n1 Agregar auto\n2 Agregar Camion" + 
                "\n3 Calcular valor total\n4 Totales por tipo de vehiculo\n5 Listar vehiculos \n6 Salir")
            opcion = input("Ingrese una opcion: ")
            match opcion:
                case "1":
                    while True:
                        mi_agencia.agregar_auto()
                        print("¿Desea agregar otro auto? (s/n): ")
                        respuesta = input()
                        if respuesta.lower() != "s":
                            break
                case "2":
                    while True:
                        mi_agencia.agregar_camion()
                        print("¿Desea agregar otro camion? (s/n): ")
                        respuesta = input()
                        if respuesta.lower() != "s":
                            break
                case "3": 
                    print(f"Valor total en agencia ${mi_agencia.valor_total_agencia()}")
                case "4":
                    print(f"Total de autos: {mi_agencia.total_autos()}")
                    print(f"Total de camiones {mi_agencia.total_camiones()}")
                    input()
                case "5":
                    mi_agencia.mostrar_vehiculos()
                    input()
                case "6":
                    print("Hasta luego")
                    break
                case _:
                    print("Opcion invalida")

Main.main()