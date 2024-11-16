from estante import Estante
from cliente import Cliente

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre.title()
        self.lista_de_estantes = []
        self.lista_de_clientes: dict = {}
        
    def agregar_estante(self, estante: Estante):
        self.lista_de_estantes.append(estante)
        print(f"Estante {estante.nombre} agregado")
        
    def mostrar_biblioteca(self):
        print("".center(30,"-"))
        print(f"Biblioteca: {self.nombre}")
        print("".center(30,"-"))

        estante: Estante
        for estante in self.lista_de_estantes:
            estante.mostrar_estante()
        print(f"Valor total biblioteca: ${self.calcular_costo_biblioteca()}")
        print("".center(30,"-"))
        
    def calcular_costo_biblioteca(self):
        estante: Estante
        costo = 0
        for estante in self.lista_de_estantes:
            costo += estante.calcular_costo_estante()
        return costo
            
    def mostrar_clientes(self):
        cliente: Cliente
        for index, cliente in enumerate(self.lista_de_clientes.values(), start = 1):
            print(f"{index} - ",end="")
            cliente.mostrar_cliente()
            
    def cliente_en_lista(self, cliente: Cliente):
        return True if self.lista_de_clientes.get(cliente.numero) else False
    
    def agregar_cliente(self, cliente: Cliente):
        self.lista_de_clientes[cliente.numero] = cliente
        print(f"Cliente {cliente.nombre} agregado")

    def minimo_clientes(self,minimo = 3):
        return len(self.lista_de_clientes) >= minimo
