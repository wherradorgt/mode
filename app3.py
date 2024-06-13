import pandas as pd

# Reemplazar "data.json" con la ruta real del archivo JSON
data_path = "data.json"

# Cargar el archivo JSON en un DataFrame de Pandas
json = pd.read_json(data_path)
df = pd.read_excel('new_df.xlsx')

# Especificar las columnas para calcular la moda
column_names = json.iloc[0].columns  # Reemplazar con las nombres de las columnas reales

# Calcular la moda para cada columna especificada
for col in column_names:
    mode_value = df[col].mode()[0]
    print(f"La moda de la columna '{col}' es: {mode_value}")