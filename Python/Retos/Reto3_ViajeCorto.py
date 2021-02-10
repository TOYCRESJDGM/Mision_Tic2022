# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:01:15 2020

@author: user
"""

diccionario = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}


ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']

def correcto(diccionario:dict)->bool:
    clave = diccionario.keys()
    valor = diccionario.values()
    dic = diccionario.items()
    correcto =True
    for clave, valor in dic:
         if (clave[0] == clave[1] and valor != 0 or valor<0):
            correcto=False
    return correcto

def calc_distancia(ruta:list,distancias:dict)->int:
    
    distancia = 0
    i=0
    while i <= len(ruta) - 1 :
        
        a= ruta[i]
        b=ruta[i+1]
        tupla= (a,b)
        distancia = distancia + distancias[tupla]
        
        i =i+1
        if(i == len(ruta)-1):
            
           i = len(ruta)+1 
             
    return distancia


def cambio(tupla:tuple,lista:list)->list:
    
    valor1 = tupla[0]
    valor2 = tupla [1]
    
    ruta_intercambio=lista.copy()
    
    indicevalor1 = ruta_intercambio.index(valor1)   
    indicevalor2 = ruta_intercambio.index(valor2)
    
    ruta_intercambio[indicevalor1]=valor2
    ruta_intercambio[indicevalor2]=valor1
    
    return ruta_intercambio

def cadena(ruta_inicial:list)->str:
    resultado=''
    i=0
    while i < len(ruta_inicial) - 1 :
             
        resultado += ruta_inicial[i]+'-'
        
        i =i+1            
    return resultado+ruta_inicial[0]

def ruteo(distancias: dict,ruta_inicial:list)-> dict:
    if correcto(distancias):
        ruta_actual = ruta_inicial.copy()
        distancia_actual = calc_distancia(ruta_actual, distancias)
        mejor_distancia= distancia_actual
        
        for t in range(1,len(ruta_actual)-1):
            
            i = 1
            while i <= len(ruta_actual) - 2:
                a = ruta_actual[i]
                j = i + 1
                  
                while j <= len(ruta_actual) - 2:
                    b = ruta_actual[j]                 
                    tupla = (a,b)  
                                     
                    ruta_intercambiada = cambio(tupla,ruta_actual)
                    distancia_intercambio = calc_distancia(ruta_intercambiada, distancias)                                                             
                                    
                    if distancia_intercambio < mejor_distancia:
                        mejoro= True
                        mejor_distancia = distancia_intercambio
                        mejor_ruta_iteracion = ruta_intercambiada
                        
                    j+=1  
                                              
                i +=1
            
            if mejoro:
                mejoro=False
                ruta_actual=mejor_ruta_iteracion
                                                  
            
        resultado=cadena(ruta_actual)
        salida = {}
        salida.update({"ruta":resultado})
        salida.update({"distancia":mejor_distancia})
                  
        return salida
    
    else:
        return "Por favor revisar los datos de entrada."
    


print(ruteo(diccionario,ruta_inicial))
    
