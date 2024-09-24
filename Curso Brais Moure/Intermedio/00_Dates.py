###  Dates  ###

from datetime import datetime #importar la funcion datetime del modulo datetime

now = datetime.now()

def print_date(date):
    print("Fecha enviada a funcion: ")
    print("Year: ", date.year)
    print("Month:", date.month)
    print("Day:", date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
print_date(now)

timestamp = now.timestamp() #valor numerico de la fecha

year_2023 = datetime(2023,1,1)  #se pueden crear fechas a patir de la funcion datetime
                                # los 3 primeros parametros a enviar son año, mes y dia de forma obligatoria

print_date(year_2023)

fecha_nac = datetime(1991, 9, 7)

print_date(fecha_nac)

from datetime import time
from datetime import date 
current_time = now.time() #para obtener hora minuto segundo y milisegundo
selected_time = time(22, 30, 25)

current_date = date(2024, 9, 24)

print(current_date)
print("Hora actual", current_time)
print("Hora seleccionada", selected_time)