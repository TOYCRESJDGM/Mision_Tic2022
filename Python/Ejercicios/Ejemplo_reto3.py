# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 08:41:03 2020

@author: user
"""
b= {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}

a= ['H', 'B', 'E', 'A', 'C', 'D', 'H'] 



def RutaInicialVecinoMasCercano (distancias: dict, nodos:list)-> dict:
    rutaSolucion = []
    kilometros = 0
    #modelar los nodos ya visitados
    yaesta ={}
    for nodo in nodos:
        yaesta.update({nodo:0})
        
    nodoActual = nodos[0]
    #iteracion de cuantos arcos de deben agregar
    for i in range(1,len(nodos)-1):
        
        #crear unicamente las llaves que nos interesan 
        listallaves = []
        for nodo in nodos:
            if nodo != nodoActual and yaesta[nodo] == 0:
                arco = (nodoActual,nodo)
                listallaves.append(arco)
        #Encontrar el minimo        
        minimaDistancia = 999999
        
        for arco in listallaves:
            if distancias [arco] < minimaDistancia:
                minimaDistancia = distancias[arco]
                minimoarco = (minimaDistancia, arco)
        #Actualizar las listas de solucion y de Yaesta
        rutaSolucion.append(minimoarco[1])
        kilometros = kilometros + minimoarco[0]
        
        yaesta [minimoarco[1][0]] = 1
        yaesta [minimoarco [1][1]] =1
        
        nodoActual = minimoarco[1][1]
        
        
    ultimoarco = (nodoActual,nodos[0])
    rutaSolucion.append(ultimoarco)
    kilometros = kilometros + distancias[ultimoarco]
    
    #salida
    salida = {}
    salida.update({"ruta":rutaSolucion})
    salida.update({"kilometraje":kilometros})
    
    return salida
                
               
print (RutaInicialVecinoMasCercano(b,a))               
        
        