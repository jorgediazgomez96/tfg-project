
# coding: utf-8

# In[1]:


get_ipython().magic(u'matplotlib inline')
import pandas as pd
import requests
import os
import plotly.offline as py
from plotly import figure_factory as ff
from PIL import Image
import ipywidgets as widgets
import plotly.graph_objs as go
import json
#Made for displays online aka. not buying the pay version
py.init_notebook_mode(connected=True)


# In[5]:


Piserver = 'http://192.168.1.45:5000/'

#conection to root D-Filesystem
dataService = pd.read_csv(Piserver)
tablaServicios = ff.create_table(dataService)
py.iplot(tablaServicios, filename='tablaServicios')

#Connecton to list archives
data = pd.read_json(Piserver + 'files')
data.to_csv('data.csv',index=False )
df = pd.read_csv('data.csv')

def updateTabla(opciones):
        
        if 'Foto' in opciones:
            table =ff.create_table(df[df['direccion']== '{}/download/image/nameOfImage.extention'])
            py.iplot(table, filename='tablaArchivos')
        elif 'Datos' in opciones:
            table = ff.create_table(df[df['direccion']== '{}/download/data/archiveName.extention'] )
            py.iplot(table,filename = 'tablaArchivos')
        elif 'Buscar' in opciones:     
            display(w)      
            w.observe(buscaUnaImagen,names='value')
        else:
            table = ff.create_table(df)
            py.iplot(table,filename = 'tablaArchivos')

def buscaUnaImagen(change):    
    if w.value in df['archivos'].unique():
        table =ff.create_table(df[df['archivos']== w.value])
        #Abre una pestaña y te muestra el archivo seleccionado
        py.iplot(table, filename='tablaArchivos.html')
        #Request para la direccion de la foto
        response = requests.get(Piserver + 'download/image/{}'.format(w.value),stream=True)
        filename = 'temporal.png'

        #Te recorres todo lo que hay en la respuesta y lo escribes en el archivo abierto
        with open(filename, 'wb') as f:
            for chunk in response:
                f.write(chunk)
        img = Image.open('temporal.png')
        img.show()

options=['Foto','Buscar','Datos','Todo']

w = widgets.Text(value='',description='Name download',disabled=False)
opciones = widgets.SelectMultiple(options=list(options), value=('Todo', ),description='Type')
widgets.interactive(updateTabla,opciones=opciones)


# In[3]:


#Direccion general de la API
#API_URL = 'http://192.168.1.45:5000'
#Request para la direccion de la foto
#response = requests.get('http://192.168.1.45:5000/fotos/{}'.format(w.value),stream=True)
#filename = 'prueba.png'

#Te recorres todo lo que hay en la respuesta y lo escribes en el archivo abierto
#with open(filename, 'wb') as f:
 #   for chunk in response:
 #       f.write(chunk)
#img = Image.open('prueba.png')
#img.show()


# In[4]:


os.remove('temporal.png')
os.remove('tablaArchivos.html')

