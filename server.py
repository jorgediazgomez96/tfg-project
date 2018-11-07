from flask import Flask, send_from_directory, jsonify, send_file, render_template,abort,request
import os
import csv

import socket
from stat import *
import datetime

#Sacar la direccion IP en uso actual
nombreEquipo = socket.gethostname()
#nombreEquipo = "163.117.148.69"
direccionEquipo = socket.gethostbyname(nombreEquipo)

app = Flask(__name__)
app.config["DEBUG"] = True

#Ruta por defecto para ir a buscar los archivos tanto de datos como fotos
DATA_DIR='/home/pi/tfg/tfg-v2/directorios/ficheroDatos'
FOTO_DIR='/home/pi/tfg/tfg-v2/directorios/fotos'

@app.route('/')
def obtenerDatos():

	return send_from_directory('/home/pi/tfg/tfg-v2/directorios',"servicios.csv",as_attachment=True)

#Con esto se obtien un archivo de una ruta que especificas a partir de la
#ruta por defecto UPLOAD_DIR

@app.route('/download/data/<path:path>')
def obtenerDato(path):

	return send_from_directory(DATA_DIR,path,as_attachment=True)

@app.route('/download/images/<path:path>')
def obtenerFoto(path):
	return send_from_directory(FOTO_DIR,path,as_attachment=True)


@app.route('/upload/data/<filename>', methods=['POST'])
def subidaDatos(filename):
	if '/' in filename:
		abort(400,'solo se admiten archivos')

	with open(os.path.join(DATA_DIR,filename),'wb')as fp:
		fp.write(request.data)

	return '', 201


#Listar todos los archivos que hay en el sistema
@app.route('/files')
def obtenerJson():

	files=[]
	tamanyo=[]
	creacion=[]
	direccion=[]

	#primero los datos
	for filename in os.listdir(DATA_DIR):
		path = os.path.join(DATA_DIR,filename)
		if os.path.isfile(path):

			files.append(filename)
			st = os.stat(path)
			tamanyo.append(st.st_size)
			numero = os.path.getctime(path)
			creacion.append(datetime.datetime.fromtimestamp(numero))
			direccion.append('{}/datos/nombreArchivo')
	#luego las fotos
	for fotoname in os.listdir(FOTO_DIR):
		path = os.path.join(FOTO_DIR,fotoname)
		if os.path.isfile(path):
			files.append(fotoname)
			st=os.stat(path)
			tamanyo.append(st.st_size)
			numero = os.path.getctime(path)
			creacion.append(datetime.datetime.fromtimestamp(numero))
			direccion.append('{}/fotos/nombreFoto');

	return jsonify(archivos=files,tamanyo=tamanyo,creacion=creacion,direccion=direccion)

app.run(host = direccionEquipo)

