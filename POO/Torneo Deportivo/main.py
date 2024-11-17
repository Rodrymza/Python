from torneo import  Torneo
from partido import Partido
from equipo import Equipo
def main():
    torneo = Torneo(input("Ingresa el nombre del torneo: ").title())
    print("Agrega los equipos al torneo")
    agregar_equipos(torneo)
    print("Crea los partidos:")
    agregar_partidos(torneo)
    print("Resultado final: ")
    torneo.mostrar_partidos()
    torneo.ordenar_equipos()
    torneo.mostrar_equipos()
    
def agregar_equipos(torneo: Torneo):
    minimo = 3
    maximo = 10
    while torneo.total_equipos() < maximo:
        nombre_equipo = input("Ingrese el nombre del equipo: ").title()
        equipo_nuevo = Equipo(nombre_equipo)
        torneo.agregar_equipo(equipo_nuevo)
        respuesta = input("¿Desea agregar otro equipo? (S/N): ").upper()
        if torneo.total_equipos() >= minimo and respuesta == "N":
            break
        else:
            print("Aun no se alcanza el minimo de equipos")
        if torneo.total_equipos() >= maximo:
            print("El torneo ya tiene el número máximo de equipos")
            break
        
def agregar_partidos(torneo):
    minimo_partidos = 5
    while True:
        print("Seleccion de equipos:")
        equipo_local = seleccionar_equipo(torneo)
        print(f"Equipo local: {equipo_local.nombre}")
        equipo_visitante = seleccionar_equipo(torneo)
        print(f"Equipo local: {equipo_visitante.nombre}")
        goles_local = obtener_valor_numerico(f"Ingrese goles de {equipo_local.nombre}: ")
        goles_visitante = obtener_valor_numerico(f"Ingrese goles de {equipo_visitante.nombre}: ")
        
        partido = Partido(equipo_local, equipo_visitante, goles_local, goles_visitante)
        resultado = partido.determinar_resultado() #caputura del resultado
        print(resultado)
        
        torneo.agregar_partido(partido)
        respuesta = input("¿Desea agregar más partidos? (S/N): ").upper()
        if respuesta == "N":
            if not torneo.total_partidos() >= minimo_partidos:
                print("Falta agregar mas partidos")
            else:
                break  

def seleccionar_equipo(torneo:Torneo):
    equipo: Equipo
    for indice, equipo in enumerate(torneo.lista_equipos, start=1):
        print(f"{indice} - {equipo.nombre}")
    while True:
        opcion = obtener_valor_numerico("Selecciona un equipo: ")
        if 1 <= opcion <= torneo.total_equipos():
            return torneo.lista_equipos[opcion-1]
        else:
            print("Opción no válida. Por favor, seleccione un equipo existente")
  
def obtener_valor_numerico(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("El valor ingresado no es numérico. Por favor, inténtelo de nuevo.")  
    
if __name__ == "__main__":
    main()
    
