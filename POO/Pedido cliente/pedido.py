class Pedido:
    def __init__(self,cliente):
        self.cliente = cliente
        self.items = []
        
    def agregar_item(self):
        while True:
            plato = input("Ingrese nombre del plato\n")
            precio = float(input("Ingrese precio\n"))
            self.items.append((plato, precio))
            respuesta = input("Desea agregar mas platos?\n")
            if respuesta == "n":
                break
    def calcular_total(self):
        total = 0.0
        for plato, precio in self.items:
            total += precio
        print(f"El total a pagar es de $ {total}")
        
    def mostrar_pedido(self):
        print("Pedido".center(30,"-"))
        print("Cliente:", self.cliente)
        for plato,precio in self.items:
            print(f"{plato.title()} - ${precio}")
        self.calcular_total()
            
primer_pedido = Pedido("Rodrigo Ramirez")
primer_pedido.agregar_item()
primer_pedido.mostrar_pedido()