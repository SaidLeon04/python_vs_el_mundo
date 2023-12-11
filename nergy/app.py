from flask import Flask, render_template
import mysql.connector
from bd import conexion

conexion = conexion()
if conexion:
    cursor = conexion.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    cursor = conexion.cursor()
    consulta = "SELECT * FROM dispositivos WHERE id_usuario = 56789"

    cursor.execute(consulta)
    resultados = cursor.fetchall()

    columnas = [i[0] for i in cursor.description]
    
    return render_template('index.html', columnas=columnas, resultados=resultados)

@app.route('/consumo')
def consumo():
    cursor = conexion.cursor()
    consulta = "SELECT * FROM consumo WHERE id_usuario = 56789"

    cursor.execute(consulta)
    resultados = cursor.fetchall()

    columnas = [i[0] for i in cursor.description]
    
    return render_template('index.html', columnas=columnas, resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
