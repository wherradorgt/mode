
import json

def get(df,columns):
    """
    Obtiene la moda de una o varias columnas de un dataset

    Args:
        df (dict): data frame filtrado o transformado
        columns (list): lista de las columnas a operar

    Returns:
        dict: diccionario con lista de columnas con su respuesta

    Examples:
        [{'ENG_SPEED': np.float64(0.0)}, {'DEF_LEVEL': np.int64(100)}, {'ENG_COOLANT_TEMP': np.int64(83)}]

    """
   
    # Especificar las columnas para calcular la moda
    column_names = columns # Reemplazar con las nombres de las columnas reales

    # Calcular la moda para cada columna especificad
    res_list = []
    if isinstance(columns, list):
        if len(column_names) > 1:
            
            for col in column_names:
                mode_value = df[col].mode()[0]
                #print(f"La moda de la columna '{col}' es: {mode_value}")
                res_list.append({col : mode_value})
        else:
            mode_value = df[column_names[0]].mode()[0]
            res_list.append({column_names[0]: mode_value })
    else:
        # Cuando es el caso que ingrese un solo columna como str
        mode_value = df[columns].mode()[0]
        res_list.append({columns : mode_value})
    return {"MODE":res_list}
    

