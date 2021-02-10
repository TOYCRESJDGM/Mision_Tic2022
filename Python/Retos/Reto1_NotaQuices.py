# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:22:17 2020

@author: Juan David González Mosquera
"""

def Calcular_Promedio (codigo: str,nota1: int, nota2: int, nota3:int, nota4: int, nota5: int) -> str:
    nota_menor = min(nota1,nota2,nota3,nota4,nota5)
    total_promedio = round((((nota1 + nota2 + nota3 + nota4 + nota5) - nota_menor)/4)/20,2)
    
    return "El promedio ajustado del estudiante {} es: {}".format(codigo, total_promedio)

  #return ("Este es el promedio" + str(total_promedio))
#print (Calcular_Promedio("AOO1", 5, 14, 76, 91, 5))