# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     if request.method == 'POST':
#         # Get the JSON data from the request body
#         data = request.get_json()

#         # Check if JSON data is valid
#         if data is None:
#             return jsonify({'error': 'No JSON data found in request body'}), 400

#         # Access JSON data using keys
#         command = data.get('operator')
#         columns = data.get('columns')

#         # Process the data
#         message = f"Hello, {command}! You are {header} years old."

#         return jsonify({'message': message})  # Return JSON response

#     else:
#         return 'This endpoint only accepts POST requests.2'

# if __name__ == '__main__':
#     app.run(debug=True)

import pandas as pd

# Reemplazar "data.json" con la ruta real del archivo JSON
data_path = "data.json"

# Cargar el archivo JSON en un DataFrame de Pandas
json = pd.read_json(data_path)
df = pd.read_excel('new_df.xlsx')

# Especificar las columnas para calcular la moda
column_names = json.iloc[0].columnHeaders  # Reemplazar con las nombres de las columnas reales

# Calcular la moda para cada columna especificada
for col in column_names:
    mode_value = df[col].mode()[0]
    print(f"La moda de la columna '{col}' es: {mode_value}")