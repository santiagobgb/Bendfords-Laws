# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas_datareader as pdr
from datetime import datetime
import pandas as pd

accion = pdr.get_data_yahoo(symbols='BIMBOA.MX', start=datetime(2000, 8, 14), end=datetime(2020, 8, 14))

#%%

accion['Adj Close'] = accion['Adj Close'].apply(str)

adjustado =  accion['Adj Close']



#%%
ajustadoprimero = np.zeros(shape=(len(adjustado),1))
ajustadoprimero =  ajustadoprimero.astype(str)

for i in range(0, len(adjustado)):
    ajustadoprimero[i] = adjustado[i][0] 

#%%

unique = np.unique(ajustadoprimero, return_counts = True)


zero_data = np.zeros(shape=(len(unique[1]),3))
lista = pd.DataFrame(zero_data, columns = ["Numero", 'Incidencias', 'Frequencia'])


for i in range(0, len(lista)):
    if i == 0 :
        
        lista["Numero"][i] = 1
        
    else: 
        lista["Numero"][i] = lista["Numero"][i-1] + 1 
        


lista["Incidencias"] = unique[1]

total = sum(lista["Incidencias"])

#%%

for i in range(0, len(lista)):
    lista["Frequencia"][i] = (lista["Incidencias"][i] * 100)/ total
    
#%%
    

import matplotlib.pyplot as plt

x = lista["Numero"]
y = lista["Incidencias"]
plt.plot(x, y)
plt.show()








