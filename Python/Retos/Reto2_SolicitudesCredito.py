# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 19:10:20 2020
RETO-2

id_prestamo  str código único alfanumérico que identifica el prestamo
casado  str Aplicante es casado (Si / No)
dependientes  int / str Cantidad de personas dependientes del aplicante (0 / 1 / 2 / ‘3+’)
educacion  str Nivel de educación de la persona (Graduado / No Graduado)
independiente  str Aplicante es independiente (Si / No)
ingreso_deudor  float Ingreso del aplicante
ingreso_codeudor  float Ingreso del codeudor
cantidad_prestamo  float Cantidad de crédito solicitada
plazo_prestamo  int Plazo del crédito
historia_credito  int Aplicante cuenta con historia crediticia favorable (1 / 0)
tipo_propiedad  str Urbana / Rural / Semi Urban
@author: Juan David González Mosquera
"""
informacion = { 'id_prestamo' : 'RETO02_AB01',
               'casado':'No', 
               'dependientes': 0, 
               'educacion': "No Graduado", 
               'independiente': 'No',
               'ingreso_deudor': 3748,
               'ingreso_codeudor': 1668,
               'cantidad_prestamo': 110,
               'plazo_prestamo': 360,
               'historia_credito' : 2,
               'tipo_propiedad': 'Semiurbano' 
               }
#Elaborado por: Juan David González Mosquera - Reto2
def prestamo (informacion: dict)->dict:
    i_d = informacion['ingreso_deudor']
    i_c = informacion ['ingreso_codeudor']
    c_p = informacion ['cantidad_prestamo']
    
    entero = isinstance (informacion['dependientes'],int)
    
    if  entero:
        dependientes = informacion ['dependientes']
    else :
        dependientes = 3 
    if informacion ['historia_credito'] == 1:    
        if i_c > 0 and i_d / 9 > c_p:
            aprobado = True
        else:
            if dependientes > 2 and informacion['independiente'] == "Si":
                if i_c / 12 > c_p:
                   aprobado = True
                else :
                   aprobado = False 
            else :
                if c_p < 200:
                    aprobado = True
                else:
                    aprobado = False
    else:
        if informacion['independiente'] == "Si":
            if not (informacion ['casado'] == "Si" and dependientes > 1):
                if i_d / 100 > c_p or i_c /100 >c_p:
                    if c_p < 180:
                        aprobado = True
                    else:
                        aprobado = False
                else:
                    aprobado = False
            else:
                aprobado = False
        else:
            if informacion ['tipo_propiedad'] =="Urbana" or informacion ['tipo_propiedad'] =="Rural" and dependientes < 2:
                if informacion ['educacion'] == "Graduado":
                    if i_d/11 > c_p and i_c/11 >c_p:
                        aprobado = True
                    else:
                        aprobado = False
                else:
                    aprobado = False
            else:
                aprobado = False
                        
                                            
              
    retorno_diccionario = {'id_prestamo' : informacion['id_prestamo'],'aprobado' : aprobado}
    return retorno_diccionario
    
               
print (prestamo(informacion))
    
