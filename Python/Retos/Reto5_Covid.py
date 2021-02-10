# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:57:03 2020

@author: user
"""

import pandas as pd
def caso_who(ruta_archivo_csv: str)-> dict:

    if ruta_archivo_csv[-4:] != '.csv':
        return "Extensión inválida."
        
    try:
        data = pd.read_csv(ruta_archivo_csv)
    except:
        return "Error al leer el archivo de datos."
                
    data['total_beds']= data['hospital_beds_per_thousand'] * data['population'] / 1000
    data['total_cases'] = data['total_cases_per_million'] * data['population'] / 1000000
    data['ratio'] = data['total_cases']/data['total_beds'] 
    data['date'] = pd.to_datetime(data['date'])
    diccionario = data.groupby(['date','continent'])['ratio'].mean().unstack()
            
   
    return diccionario.to_dict()
        
               
print(caso_who('owid-covid-data.csv'))