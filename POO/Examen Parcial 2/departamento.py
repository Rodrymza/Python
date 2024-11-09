
class Departamento:
    def __init__(self, letra) -> None:
        self.letra = letra
        self.lista_ambientes = []

    def total_metros_cuadrados(self):
        total = 0
        for ambiente in self.lista_ambientes:
            total += ambiente.metrosCuadrados
        return total
    
    def mostrar_ambientes(self):
        print("-------------------")
        print(f"Departamento Letra:{self.letra}")
        print("-------------------")
        for ambiente in self.lista_ambientes:
            print(f"{ambiente.tipoAmbiente}       {ambiente.metrosCuadrados}m2")
        print(f"Total superficie {self.total_metros_cuadrados()}m2")
        print("-----------------------")


    def calcular_costo_departamento(self):
        suma = 0
        for ambiente in self.lista_ambientes:
            suma += ambiente.costoAmbiente
        return suma
    
    def agregar_ambientes(self, ambientes):
        self.lista_ambientes = ambientes