import mode
import mean
import median
import countList
import sumaList

def find_value_by_path(data, path):
    """
    Navega a través de un diccionario anidado usando una lista de claves.

    Args:
        data (dict): El diccionario en el cual navegar.
        path (list): Lista de claves para acceder a los valores.

    Returns:
        El valor encontrado o None si la clave no existe.
    """
    current = data
    try:
        for key in path:
            current = current[key]
        return current
    except (KeyError, IndexError, TypeError):
        return None

def pick(df,metric):
    """
    Obtiene la moda de una o varias columnas de un dataset

    Args:
        df (dict): data frame filtrado o transformado
        metric (dict): metrica que se esta operando

    Returns:
        list: lista de todas las operaciones solicitadas

    Examples:
        [{'MEAN': [{'ENG_SPEED': np.float64(1277.7505285412262)}, {'DEF_LEVEL': np.float64(98.94291754756871)}, {'ENG_COOLANT_TEMP': np.float64(82.65327695560254)}]}]

    """
     # Llamar a la función para obtener el valor
    name = find_value_by_path(metric, ['response', 'type', 'name'])
    
    columns = find_value_by_path(metric, ['response', 'type', 'params'])
    
    res_op = []
    params = {"df":df,"columns":columns}
    
    if isinstance(name, list):
        operations = name
        for operation in operations:
            res_op.append(choose_option(operation,params))
    else:
        res_op.append(choose_option(name,params))

    return res_op

def optionSUM(param):
    return sumaList.get(param['df'],param['columns'])

# la misma que la media aritmetica
def optionAVG(param):
    return mean.get(param['df'],param['columns'])

def optionMEAN(param):
    return mean.get(param['df'],param['columns'])

def optionMEDIAN(param):
    return median.get(param['df'],param['columns'])


def optionMODE(param):
    return mode.get(param['df'],param['columns'])

def optionCOUNT_AVG(param):
    return f"Opción COUNT_AVG {param}"

def optionCOUNT(param):
    return countList.get(param['df'],param['columns'])




# Diccionario de opciones
options = {
    "SUM": lambda param: optionSUM(param),
    "AVG": lambda param: optionAVG(param),
    "MEAN":  lambda param: optionMEAN(param),
    "MEDIAN": lambda param: optionMEDIAN(param),
    "MODE": lambda param: optionMODE(param),
    "COUNT_AVG": lambda param: optionCOUNT_AVG(param),
    "COUNT": lambda param: optionCOUNT(param),
}

# Función para ejecutar la opción deseada
def choose_option(choice,param):
    return options.get(choice, lambda param: "Opción no válida")(param)