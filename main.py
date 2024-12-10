import os
from flask import Flask, send_file
import plotly.express as px
import pandas as pd
app = Flask(__name__)
@app.route("/")
def index():
    return send_file('src/index.html')
@app.route("/cargarfuentedatos")
def cargarfuentedatos():
    with open("shareelectricityrenewables.csv",'r') as archivo:
        mitabla="<table id='t_datos' class='table table-hover'>"
        mitabla=mitabla+ "<thead>"
        mitabla=mitabla+ "<tr>"
        mitabla=mitabla+"<th>Pais</th>"
        mitabla=mitabla+"<th>Codigo</th>"
        mitabla=mitabla+"<th>Año</th>"
        mitabla=mitabla+"<th>Ahorro</th>"
        mitabla=mitabla+"</tr>"
        mitabla=mitabla+"</thead>"
        mitabla=mitabla+"<tbody>"
        paises = set()
        for linea in archivo:
            elemento=linea.split(",")
            paises.add(elemento[0])
            mitabla=mitabla+"<tr>"
            mitabla=mitabla+"<td>"+elemento[0]+"</td>"
            mitabla=mitabla+"<td>"+elemento[1]+"</td>"
            mitabla=mitabla+"<td>"+elemento[2]+"</td>"
            mitabla=mitabla+"<td>"+elemento[3]+"</td>"
            mitabla=mitabla+"</tr>"
        return mitabla+"</tbody></table>"


def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
