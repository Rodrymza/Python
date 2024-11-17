from equipo import Equipo
class Partido:
    def __init__(self, equipo_local: Equipo, equipo_visitante: Equipo, goles_local, goles_visitante):
            self.equipo_local = equipo_local
            self.equipo_visitante = equipo_visitante
            self.goles_local = goles_local
            self.goles_visitante = goles_visitante
            
    def determinar_resultado(self):
        if self.goles_local > self.goles_visitante:
            self.equipo_local.actualizar_puntos(3)
            return f"Ganador {self.equipo_local.nombre}"
        elif self.goles_local == self.goles_visitante:
            self.equipo_local.actualizar_puntos(1)
            self.equipo_visitante.actualizar_puntos(1)
            return "Empate"
        else:
            self.equipo_visitante.actualizar_puntos(3)
            return f"Ganador {self.equipo_visitante.nombre}"

    