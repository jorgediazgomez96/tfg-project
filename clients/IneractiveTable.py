
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import os
import plotly.offline as py
from plotly import figure_factory as ff
import ipywidgets as widgets
import plotly.graph_objs as go

import json
#Made for displays online aka. not buying the pay version
py.init_notebook_mode(connected=True)


# In[2]:


Piserver = 'http://192.168.1.50:5000/'
#conection to root D-Filesystem
#dataService = pd.read_csv('http://192.168.1.39:5000/')
dataService = pd.read_csv(Piserver)


tablaServicios = ff.create_table(dataService)
py.iplot(tablaServicios, filename='tablaServicios')


# In[3]:


#Connecton to list archives
data = pd.read_json(Piserver+'files')
data.to_csv('data.csv',index=False )


# In[4]:



df = pd.read_csv('data.csv')
print(df)


# In[9]:


def updateTabla(opciones):

        if 'Foto' in opciones:
            table =ff.create_table(df[df['direccion']=='{}/download/image/nameOfImage.extention'])
            py.iplot(table, filename='tablaArchivos')
        elif 'Datos' in opciones:
            table = ff.create_table(df[df['direccion']== '{}/download/data/archiveName.extention'] )
            py.iplot(table,filename = 'tablaArchivos')
        elif 'Buscar' in opciones:     
            display(w)      
            w.observe(buscaUnFichero,names='value')
        else:
            table = ff.create_table(df)
            py.iplot(table,filename = 'tablaArchivos')

def buscaUnFichero(change):    
    if w.value in df['archivos'].unique():
        table =ff.create_table(df[df['archivos']== w.value])
        #Abre una pestaña y te muestra el archivo seleccionado
        py.iplot(table, filename='tablaArchivos.html')
        response = requests.get(Piserver+'download/data/{}'.format(w.value),stream=True)
        filename = w.value
        with open(filename, 'wb') as f:
            f.write(response.text)
        print("Se ha descargado el archivo " + w.value)
        
options=['Foto','Buscar','Datos','Todo']            

w = widgets.Text(value='',description='Nombre del fichero',disabled=False)           
opciones = widgets.SelectMultiple(options=list(options), value=('Todo', ),description='Type')
widgets.interactive(updateTabla,opciones=opciones)     
       



# In[6]:


os.remove('data.csv')


# In[7]:


#Direccion general de la API
API_URL = Piserver
#Request para la direccion de la foto
response = requests.get('{}download/image/anaconda.png'.format(API_URL),stream=True)
filename = 'prueba.png'

with open(filename, 'wb') as f:
    for chunk in response:
        f.write(chunk)


# In[8]:


os.remove('prueba.png')
os.remove('data.csv')
#os.remove('tablaArchivos.html')

