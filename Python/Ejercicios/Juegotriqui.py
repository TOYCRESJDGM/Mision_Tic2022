# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 07:13:15 2020

@author: user
"""
import numpy as np

def displayInicialTriqui():
    for i in range(0,3):
        for j in range(0,3):
            print("|_",end="")
        print("|")

def displayTriqui(matriz):
    for i in range(0,3):
        for j in range(0,3):
            if matriz[i,j]==1:
                print("|X", end="")
            else:
                if matriz [i,j]==10:
                    print("|O", end="")
                 
                else:
                    print("|_",end="")
        print("|")
        

def estadoDelJuego(matriz)->int:
    
    #devuelve 1 si gana la x
    if 3 in np.sum (matriz, axis=0) or 3 in np.sum(matriz,axis=1)  or np.sum(np.diagonal(matriz))==3 or np.sum(np.diagonal(np.fliplr(matriz)))==3 :
        salida = 1
    else:
        #devuelve 2 si gana y
         if 30 in np.sum (matriz, axis=0)  or 30 in np.sum(matriz,axis=1) or np.sum(np.diagonal(matriz))==30 or np.sum(np.diagonal(np.fliplr(matriz)))==30 :
             salida = 2
         else:
             #devuelve 3 si no hay ganador
             if np.sum(matriz)== 45 or np.sum(matriz)==54:
                 salida = 3
             else:
                 # devuelve 4 si aun hay juego
                 salida = 4
    return salida
           
def jugarTriqui():
    turno = True
    displayInicialTriqui()
    matriz=np.zeros((3,3))
    estado = 4
    while(estado == 4):
        tupla =tuple(input("Ingrese la casilla a jugar ej: 2,2: "))
        x= int(tupla[0])-1
        y = int(tupla[2])-1
        if x >= 0 and x<=2 and y>=0 and y<=2:
            if matriz[x,y]==0:
                if turno:
                    matriz[x,y]=1
                else:
                    matriz[x,y]=10
                    
                estado = estadoDelJuego(matriz)
                displayTriqui(matriz)
                turno = not (turno)
            else:
                print("Recuerde jugar en casillas vacias")
        else:
            print("recuerde que el tablero es 3x3")
    if estado== 1:
        print("El jugador X ha ganado")
    else:
        if estado==2:
            print("El jugador O ha ganado")
        else:
            print("No hay ganador")

