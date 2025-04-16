from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)
url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'

@app.route('/')
def home():
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")

    lista = requests.get(url)
    data = lista.text
    data_lines = data.split('\n')

    filto_data = [] # Lista con los datos filtrados: id = 3, 4, 5, 7
    for line in data_lines[1:]:
        if line.strip():
            # Dividir cada línea en columnas
            columns = line.split('|')
            # Obtener el id (primer valor) y verificar si comienza con 3, 4, 5 o 7
            person_id = columns[0]
            if person_id.startswith(('3', '4', '5', '7')):
                # Agregar a la lista
                filto_data.append(columns)

    tabla = '<table border="1">\n' # Creación de la tabla
    tabla += '  <tr>\n'
    for header in filto_data[0]:
        tabla += f'    <th>{header.strip()}</th>\n'
    tabla += '  </tr>\n'

    # Añadir las filas a la tabla
    for row in filto_data:
        tabla += '  <tr>\n'
        for cell in row:
            tabla += f'    <td>{cell.strip()}</td>\n' # Eliminar espacios extra
        tabla += '  </tr>\n'
    
    tabla += '</table>'

    return f'¡Hola, Loja! <b>{fecha_formateada}</b> \n {tabla}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
