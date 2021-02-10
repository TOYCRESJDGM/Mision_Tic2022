# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 07:37:18 2020

@author: user
"""
unvisited = {'A', 'B', 'C', 'D', 'E', 'C'}
distances = {('A', 'B'): 6, ('A', 'D'): 1, ('B', 'C'): 5, ('B', 'D'): 2, ('B', 'E'):2, ('D', 'E'): 1, ('E','C'): 5,
             ('B', 'A'): 6, ('D', 'A'): 1, ('C', 'B'): 5, ('D', 'B'): 2, ('E', 'B'):2, ('E', 'D'): 1, ('C','E'): 5}
neighbours = {
                'A': ['B', 'D'],
                'B': ['A', 'D', 'C'],
                'C': ['B', 'E'],
                'D': ['A', 'B', 'E'],
                'E': ['D', 'B', 'C']
              }
def dijkstra(unvisited: set, distances: dict, neighbours: dict,start:str):
    
    known = { node :0 if node == start else float('inf') for node in unvisited}
    
    previous = { node : None for node in unvisited}
    
    while len(unvisited) > 0:
        
        distance,visit = min( [ (known[candidate],candidate) for candidate in unvisited])
        
        calculated = {neighbour: distance + distances[visit, neighbour] for neighbour in neighbours[visit]}
   
        previous.update({vertex: visit if calculated[vertex] < known[vertex] else previous [vertex] for vertex in neighbours[visit]} )
        
        known.update( {vertex:calculated[vertex] if calculated[vertex] < known [vertex] else known[vertex] for vertex in neighbours[visit] })
        
        unvisited.remove(visit)
        
    return known, previous
                    
minimas, predecesores = dijkstra(unvisited, distances, neighbours, 'A')
minimas, predecesores = sorted(minimas.items()), sorted(predecesores.items())

print ('Distancias minimas: \n {} \n)Predecesores: \n {}'.format(minimas,predecesores))