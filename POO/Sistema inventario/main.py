
from inventario import Inventario
class Main:
    def __init__(self):
        self.inventario = Inventario("Gestion de productos")
        

    def iniciar_programa(self): 
        for nombre, precio, cantidad in productos:
            self.inventario.agregar_producto_lista(nombre, precio,cantidad)
        self.menu_principal()
            
    def menu_principal(self):
        while True:
            print("Seleccione operacion deseada\n1 Mostrar Productos\n2 Agregar productos\n3 Sacar productos\n4 Aumentar stock \n5 Salir")
            seleccion = input()
            match seleccion:
                case "1": self.inventario.mostrar_inventario()
                case "2": self.inventario.agregar_producto_manual()
                case "3": self.inventario.modificar_stock_producto(-int(input("Ingrese la cantidad de producto a retirar\n")))
                case "4": self.inventario.modificar_stock_producto(int(input("Ingrese la cantidad de producto a ingresar\n")))
                case "5": return
                case _: "Opcion no valida"

productos = [
        ["Manzanas", 120.50, 50],
    ["Leche", 75.00, 30],
    ["Pan", 90.00, 20],
    ["Arroz", 55.00, 100],
    ["Fideos", 65.50, 60],
    ["Huevos", 200.00, 12],
    ["Azúcar", 80.00, 40],
    ["Yerba", 300.00, 25],
    ["Jabón", 45.00, 50],
    ["Aceite", 250.00, 15],
    ["Sal", 35.00, 80],
    ["Queso", 400.00, 10],
    ["Café", 500.00, 5],
    ["Papel Higiénico", 120.00, 40],
    ["Detergente", 150.00, 20]]
app = Main()
app.iniciar_programa()

