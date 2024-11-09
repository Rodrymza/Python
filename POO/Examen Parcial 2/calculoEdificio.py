from edificio import Edificio
from funciones import pedir_entero
from piso import Piso
from departamento import Departamento
from ambiente import Ambiente
from funciones import pedir_boolean
class CalculoEdificio:
    def __init__(self):
        self.cotizacion = [["AAA", "Cocina", 80, 21000],
                           ["BBB", "Habitacion", 12, 10000],
                           ["CCC", "Baño estandar", 6, 9000],
                           ["DDD", "Habitacion Premium", 16, 1500],
                           ["EEE", "Baño Premium", 8, 12000],
                           ["FFF", "Escritorio", 10, 8000],
                           ["GGG", "Comedor", 30, 25000],
                           ]
        self.edificio = Edificio(input("Ingrese nombre del edificio\n"))

    def main(self):
        numero_pisos = pedir_entero("Ingrese numero de pisos (3-12)", 1, 12)
        for i in range(numero_pisos):
            print("Agregando departamentos al piso", i)
            nuevo_piso = Piso(i)
            while True:
                nuevo_piso.agregar_departamento(self.crear_departamento())
                if not pedir_boolean("Agregar mas departamentos?"):
                    self.edificio.agregar_piso(nuevo_piso)
                    break
        self.edificio.mostrar_edificio()
        self.edificio.calcular_metros_cubiertos()
        self.edificio.total_costo_construccion()

        print(f"Total metros cuadrados cubiertos {self.edificio.totalMetrosCubiertos}")
        print(f"Total costo: ${self.edificio.costoTotalConstruccion}")
        
    def crear_departamento(self):
            nuevo_departamento = Departamento(input("Ingrese letra del departamento").upper())
            while True:
                nuevo_departamento.agregar_ambientes(self.crear_ambiente())
                nuevo_departamento.mostrar_ambientes()
                return nuevo_departamento

    def mostrar_ambientes(self):
        i=1
        for _, nombre, metros, _ in self.cotizacion:
            print(f"{i} - {nombre} {metros}m2 ")
            i += 1

    def crear_ambiente(self):
        hay_baño = False
        tres_ambientes = False
        lista_ambientes = []
        while True:
            self.mostrar_ambientes()
            seleccion = pedir_entero("Seleccione ambiente a agregar", 1, len(self.cotizacion)+1) - 1
            ambiente_nuevo = Ambiente(self.cotizacion[seleccion][1], self.cotizacion[seleccion][2], self.cotizacion[seleccion][3])
            lista_ambientes.append(ambiente_nuevo)

            if len(lista_ambientes) >= 3:
                tres_ambientes = True
            if seleccion in (2,4):
                hay_baño = True
            if not pedir_boolean("Desea agregar mas ambientes?"):
                if hay_baño and tres_ambientes:
                    return lista_ambientes                
                else:
                    if not hay_baño:
                        print("Falta agregar un baño")
                    else:
                        print("Debes agregar al menos 3 ambientes")

app = CalculoEdificio()
app.main()

            


