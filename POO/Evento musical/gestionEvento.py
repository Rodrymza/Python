from presentacion import Presentacion
from escenario import Escenario
from diaEvento import DiaEvento
from eventoMusical import EventoMusical

def main():
    mi_evento = EventoMusical(input("Ingrese el nombre del evento: ").title())
    
    dias = pedir_dias()
    for numero_dia in range(dias):
        nuevo_dia = DiaEvento(numero_dia + 1)
        
        agregar_escenarios_a_dia(nuevo_dia, mi_evento)
            
    mi_evento.calcular_costo_total()
    mi_evento.mostrar_evento()
           
def agregar_escenarios_a_dia(nuevo_dia: DiaEvento, evento: EventoMusical):
    while nuevo_dia.maximo_escenarios():
        nuevo_escenario = Escenario(input("Ingrese el nombre del nuevo escenario: ").title())
        agregar_presentaciones(nuevo_escenario, evento)
        nuevo_dia.agregar_escenario(nuevo_escenario)
        
        if preguntar("Agregar mas escenarios?"):
            break
          
def preguntar(mensaje):
    print(mensaje + " (s/n)")
    respuesta = input().lower()
    return True if respuesta == "n" else False          
            
def agregar_presentaciones(escenario: Escenario, evento: EventoMusical):
    maximo = 500000
    while True:
        artista = input("Ingrese el nombre del artista: ").title()
        duracion = int(input("Ingrese la duracion de la presentacion: "))
        costo = float(input("Ingrese el costo de la presentacion: "))
        nueva_presentacion = Presentacion(artista, duracion, costo)
        if not escenario.validar_artista_duplicado(nueva_presentacion):
            evento.calcular_costo_total()
            costo_total = evento.total_costo + escenario.calcular_costo_escenario() + nueva_presentacion.costo
            if  costo_total <= maximo:
                escenario.agregar_presentacion(nueva_presentacion)
            else:
                print(f"No se agrego la presentacion ya que se supera el maximo de ${maximo}")
        else:
            print("El artista ya tiene una presentacion designada")
        respuesta = input("Desea agregar mas presentaciones? ")
        if respuesta.lower() == "n" and escenario.validar_minimo_presentaciones():
            break
        else:
            print("Falta agregar mas presentaciones")
            
            
def pedir_dias(minimo = 1, maximo = 7):
    while True:
        dias = int(input("Ingrese el numero de dias: "))
        if minimo <= dias <= maximo:
            return dias
        else:
            print(f"La cantidad de dias debe ser entre {minimo} y {maximo}")
    
if __name__ ==  "__main__":
    main()