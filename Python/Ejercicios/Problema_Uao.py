# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:42:32 2020

@author: user
"""

def calculo()->str:
    valores=[10,0,-20,150,-200]
  
    
    minimo = int (input("Ingrese numero minimo"))
    maximo = int (input("Ingrese numero maximo"))
    
    totalentrada=totalvalido=0
    suma=0
    i=0
    
    while totalentrada<5:
        totalentrada +=1
        
        if(valores[i]>minimo and valores[i]<= maximo):
            totalvalido +=1
            suma+=valores[i]
        i+=1
    if totalvalido>0:
        media=suma/totalvalido
        
    else:
        media=-888
        
    return "media {} \n totalentrada {} \n totalvalido {}".format(media,totalentrada,totalvalido)
        
print(calculo())