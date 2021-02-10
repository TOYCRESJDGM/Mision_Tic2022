# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:37:48 2020

@author: user
"""


diccionario ={('H', 'H') : 0, ('H', 'A') : 60, ('H', 'B') : 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0 }

ruta_inicial = ['MDE', 'PEI', 'BOG', 'CTG', 'SMR', 'MDE']


# clave = diccionario.keys()
# valor = diccionario.values()

# dic = diccionario.items()


# for clave, valor in dic:
#     if clave[0]== clave[1] and valor == 0 or clave[0] != clave[1] and valor > 0:
#         print('yes')
#     else :
#         print ('el resultado es {}'.format(valor))


# lista = ruta_inicial.copy()

# i=1
# while i <= len(lista) -2:
#     a = lista[i]
#     j = i + 1
    
#     while j <= len(lista) -2:
#         b = lista[j]
#         tupla = (a,b)
        
#         print (tupla)
        
#         j +=1
        
#     i+=1
    
    
# def calc_distancia(ruta:list,distancias:dict)->int:
    
 
#     distancia = 0
    
#     for uno in ruta:
       
        
#         print(a)
      
# print(calc_distancia(ruta_inicial,diccionario))        
def cadena(ruta_inicial:list)->str:
    resultado=''
    i=0
    while i < len(ruta_inicial) - 1 :
             
        resultado += ruta_inicial[i]+'-'
        
        i =i+1            
    return resultado+ruta_inicial[0]
             
   
print(cadena(ruta_inicial))    
    