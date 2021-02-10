# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def inicio_reaccion (codigo: str, hora_terminacion: int, minuto_terminacion: int, duracion_horas: int, duracion_minutos: int, duracion_segundos:int ) -> str:
        hora_duracion_segundos = duracion_horas*3600+duracion_minutos*60+duracion_segundos
        hora_terminacion_segundos = hora_terminacion*3600+minuto_terminacion*60
        diferencia_segundos = hora_terminacion_segundos - hora_duracion_segundos
        
        hora_inicio_d =  diferencia_segundos/3600
        hora_inicio = int(hora_inicio_d)
        
        minutos_inicio_d = (hora_inicio_d - hora_inicio)*60
        minutos_inicio = int(minutos_inicio_d)
        
        segundos_inicio_d = (minutos_inicio_d - minutos_inicio)*60
        segundos_inicio = round(segundos_inicio_d)
                
        
        hora = str(hora_inicio)
        minutos =str(minutos_inicio).zfill(2)
        segundos =str(segundos_inicio).zfill(2)
        #return "Minutos en segundos decimal "+ str(minutos_inicio_d)
        return "La reacción {} debe iniciarse a las {} horas, {} minutos con {} segundos para que esté lista en en el momento requerido" .format(codigo,hora,minutos,segundos)

print (inicio_reaccion("AA01",16,30,4,11,23))