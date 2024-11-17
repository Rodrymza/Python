from equipo import Equipo
from partido import Partido
class Torneo:
    def __init__(self, nombre_torneo):
        self.nombre_torneo = nombre_torneo
        self.lista_equipos = []
        self.lista_partidos = []
        
    def agregar_equipo(self, equipo: Equipo):
        if not self.equipo_duplicado(equipo):
            self.lista_equipos.append(equipo)
        else:
            print("El equipo ya se encuentra en el torneo")
        
    def equipo_duplicado(self,equipo: Equipo):
        nombres = [equipo.nombre for equipo in self.lista_equipos]
        if equipo.nombre in nombres:
            return True
        
    def partido_duplicado(self, partido_nuevo: Partido):
        partido: Partido
        for partido in self.lista_partidos:
            if partido.equipo_local == partido_nuevo.equipo_local and partido.equipo_visitante == partido_nuevo.equipo_visitante:
                return True
            
    def agregar_partido(self, partido_nuevo: Partido):
        if not self.partido_duplicado(partido_nuevo) and not self.partido_mismo_equipo(partido_nuevo):
            self.lista_partidos.append(partido_nuevo)
            print("Partido agregado exitosamente")
        if self.partido_duplicado(partido_nuevo):
            print("El partido ya se encuentra en el torneo")
        if self.partido_mismo_equipo(partido_nuevo):
            print("No se puede agregar un partido entre el mismo equipo")
            
    def partido_mismo_equipo(self, patido: Partido):
        return patido.equipo_local == patido.equipo_visitante
        
    def total_equipos(self):
        return len(self.lista_equipos)
    
    def mostrar_equipos(self):
            print(f"{'Posición':<10}{'Equipo':<20}{'Puntos':<10}") #formateo de string para resultado mas profesional
            for i, equipo in enumerate(self.lista_equipos, start=1):
                print(f"{i:<10}{equipo.nombre:<20}{equipo.puntos:<10}")

            
    def mostrar_partidos(self):
        print("Torneo", self.nombre_torneo)
        print("Lista de partidos:")
        partido: Partido
        for indice, partido in enumerate(self.lista_partidos, start=1):
            print(f"{indice}. {partido.equipo_local.nombre:<15} {partido.goles_local:<2} - {partido.goles_visitante:>2} {partido.equipo_visitante.nombre:>15}")
    
    def total_partidos(self):
        return len(self.lista_partidos)
    
    def ordenar_equipos(self):
        self.lista_equipos.sort(key=lambda equipo: equipo.puntos, reverse= True)
