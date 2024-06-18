
import json
import numpy as np
import pandas as pd

def get(df,columns):
    """
    Obtiene la media de una o varias columnas de un dataset si estan son columnas numericas no categoricas

    Args:
        df (dict): data frame filtrado o transformado
        columns (list): lista de las columnas a operar

    Returns:
        dict: Diccionario con lista de columnas con su respuesta, si son cetegoricas la respuesta de None

    Examples:
        [{'ENG_SPEED': np.float64(0.0)}, {'DEF_LEVEL': np.int64(100)}, {'ENG_COOLANT_TEMP': np.int64(83)}, {'IDLE_REASON': None}]

    """
    # Especificar las columnas para calcular la moda
    column_names = columns # Reemplazar con las nombres de las columnas reales

    # Calcular la moda para cada columna especificad
    res_list = []
    if type(columns) is list: 
        if len(column_names) > 1:
            
            for col in column_names:
                value = operand(df[col])
                #print(f"La moda de la columna '{col}' es: {mode_value}")
                res_list.append({col : value})
        else:
            col = column_names[0]
            value =  operand(df[col])
            res_list.append({col: value })
    else:
        # Cuando es el caso que ingrese un solo columna como str
        col = columns
        value = operand(df[col])
        res_list.append({col : value})
    return {"SUM":res_list}

def operand(column_list):
    """
    Operar lista de columna 

    Args:
        column_list (list): lista de columna del data frame
    
    Returns:
        (int | float): devuelme la suma de la lista de la columna y si es categorica devuelve None
    """
    if pd.api.types.is_categorical_dtype(column_list) or pd.api.types.is_string_dtype(column_list):
        return None
    else:
       return np.sum(column_list)
        
    

