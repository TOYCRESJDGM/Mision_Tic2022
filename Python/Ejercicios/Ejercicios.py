# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:13:33 2020
Desafios
@author: Juan David González Mosquera
"""
import math
#Leer un numero entero y convertirlo a float
def convertir_entero (numero: int)->float:
    r_numero = float(numero)
    
    return r_numero

#print (convertir_entero(8))


#Leer un numero real y determinar su parte entera

def parte_entera(numero : float)->int:
    numero_real = int(numero)
    
    return numero_real

#print(parte_entera(11.2))

#realizar un programa que sume el max y el min de un grupo de datos y su salida sea un string(str)

def suma_maxymin()->str:
    cantidad = int(input("ingrese la cantidad de datos"))
    lista = []
    for contador in range(0,cantidad,1):
        numero = int(input("Ingrese uno de los numeros"))
        lista.append(numero)
        
    numero_max = max(lista)
    numero_min = min(lista)
    suma = numero_max + numero_min
    
    return "La suma del numero max {} y el numero min {} es:".format(numero_max,numero_min) +str(suma)
        
    
#print(suma_maxymin())

#Realizar un programa que  imprima hola mundo, como resultado de asignar a una variable la
#palabra “Hola” y a otra variable la palabra “mundo”.

def hola_mundo(hola:str,mundo:str)->str:
    return "{}".format(hola)+"{}".format(mundo)

#print(hola_mundo("Hola","Mundo"))

#Realizar un programa que me sume solamente los decimales de dos números.

def suma_decimales (numero1:float,numero2:float)-> int:
    decimales_numero1 = numero1 - int(numero1)
    decimales_numero2 = numero2 - int (numero2) 
    
    return decimales_numero1 + decimales_numero2
    

#print(suma_decimales(1.1 , 1.4))

#Construye un programa que pregunte al usuario el radio de una circunferencia (r) y le muestre
#en pantalla un mensaje así: “Para una circunferencia con radio r, el perímetro es p y el área es
#a”. Las fórmulas para el cálculo del perímetro y el área de una circunferencia se presentan a
#continuación:
    #Perímetro = 2*π*r
    #Área = π*r2
#El programa debe definir una función para calcular el área, otra para calcular el perímetro
#y hacer uso de estas dos funciones.


def calcular_area(radio:int)->float:
    area = radio*radio*math.pi
    
    return area

def calcular_perimetro(radio:int)->float:
    perimetro = 2*radio*math.pi
    
    return perimetro

def circunferencia ()->str:
    radio = int(input("Ingrese en radio de la circunferencia"))
    
    print ("“Para una circunferencia con radio {}, el perímetro es p y el área es a”. Las fórmulas para el cálculo del perímetro y el área de una circunferencia se presentan a continuación:".format(radio)+ "\n"+
    "Perímetro = 2*π*r"+"\n"+
    "Área = π*r2")
    
    calculo = input("¿Desea calcularlo? SI/NO")
    if calculo == "SI" :
        
        perimetro = calcular_perimetro(radio)
        area = calcular_area(radio)
        
        return "El perimetro es:" + str(perimetro)+ "\n"+ "El area es:" + str(area)
    
        
#print (circunferencia())

#Construye un programa que pregunte al usuario dos números y le muestre en pantalla un
#mensaje con el resultado de la suma, resta, multiplicación y división de dichos números. El
#programa debe definir e invocar funciones separadas para la suma, resta, multiplicación y
#división.

def suma(sumando1: int, sumando2: int)->str:
    resultado = sumando1+sumando2
    return "La el resultado de la suma de {} + {} es:".format(sumando1,sumando2)+ str(resultado)+"\n"

def resta(restando1:int, restando2: int)->str:
    resultado= restando1 - restando2 
    return "La resultado de la resta de {} - {} es:".format(restando1,restando2) +str(resultado)+"\n"

def multiplicacion(numero1: int, numero2 :int)->str:
    resultado = numero1 * numero2
    return "La resultado de la mutiplicacion de {} * {} es:".format(numero1,numero2)+ str(resultado)+"\n"

def division(numero1: int, numero2: int)->str:
    resultado = round(numero1/numero2,2)
    return "la resultado de la division de {} / {} es :".format(numero1,numero2)+str(resultado)+"\n"

def funciones()->str:
    numero1 = int(input("Digite el primer numero"))
    numero2 = int(input("Digite el segundo numero"))
    
    la_suma = suma(numero1,numero2)
    la_resta = resta(numero1,numero2)
    la_multiplicacion = multiplicacion(numero1,numero2)
    la_division = division(numero1,numero2)

    return la_suma+la_resta+la_multiplicacion+la_division

#print (funciones())
#Construye un programa que pregunte al usuario las longitudes de los tres lados de un triángulo y
#arroje un mensaje informando el área del triángulo

def semi_perimetro(lado1: int, lado2: int, lado3: int)->float:
    s = (lado1+lado2+lado3)/2 
    
   
    heron_area = math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
    
   
    return round(heron_area,2)

def area_triangulo()->float:
    lado1 = int(input("Digite uno de los lados del triangulo"))
    lado2 = int(input("Digite el segundo de los lados del triangulo"))
    lado3 =int (input("Digite el tercero de los lados del triangulo"))
    
    elarea_heron = semi_perimetro(lado1,lado2,lado3)
    
    return "El area es :"+str(elarea_heron)

#print(area_triangulo())
    





