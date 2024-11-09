from departamento import Departamento
class Piso:
    def __init__(self,piso ) -> None:
        self.nro_piso = piso
        self.lista_departamentos = []

    def total_superficie_piso(self):
        suma = 0
        for departamento in self.lista_departamentos:
            suma += departamento.total_metros_cuadrados()
        return suma
    
    def calcular_costo_piso(self):
        suma = 0
        for departamento in self.lista_departamentos:
            suma += departamento.calcular_costo_departamento()
        return suma
    
    def agregar_departamento(self,departamento):
        self.lista_departamentos.append(departamento)
        if self.total_superficie_piso() > 800:
            self.lista_departamentos.pop()
            print("Metros cubiertos excedidos, el ultimo departamento no se agrego")

    def mostrar_departamentos(self):
        print(f"----------Departamentos piso {self.nro_piso}----------")
        for departamento in self.lista_departamentos:
            departamento.mostrar_ambientes()
        print("-------------------------")
