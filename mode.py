import pandas as pd
import json

def getMode(json):
    df = pd.read_excel('new_df.xlsx')

    # Especificar las columnas para calcular la moda
    column_names = json[0]['columns'] # Reemplazar con las nombres de las columnas reales

    # Calcular la moda para cada columna especificad
    res_list = []
    if len(column_names) > 1:
        
        for col in column_names:
            mode_value = df[col].mode()[0]
            #print(f"La moda de la columna '{col}' es: {mode_value}")
            res_list.append({col : mode_value})
    else:
        mode_value = df[column_names[0]].mode()[0]
        res_list.append({column_names[0]: mode_value })
    return res_list