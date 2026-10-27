x = [20, 25, 30, 35, 40]
y = [50, 58, 65, 75, 82]

def media(x):
    """Calcula la media aritmética de una lista de valores numéricos.

    Args:
        x (list of float/int): Lista de números de la cual se calculará la media.

    Returns:
        float: El valor promedio de los elementos de la lista.
    """
    return sum(x) / len(x)

def diferencia_cuadrado(x):
    """Calcula la suma de los cuadrados de las diferencias entre cada valor 
    y la media de la lista (suma de cuadrados total o SSxx).

    Args:
        x (list of float/int): Lista de valores numéricos de la variable independiente.

    Returns:
        float: La sumatoria de las desviaciones al cuadrado respecto a la media.
    """
    la_media = media(x)
    la_diferencia = 0
    for i in x:
        la_diferencia = la_diferencia + (i - la_media) * (i - la_media)
    return la_diferencia

def diferencia_xy(x, y):
    """Calcula la sumatoria del producto de las diferencias de cada par de 
    valores respecto a sus respectivas medias (suma de productos cruzados o SPxy).

    Args:
        x (list of float/int): Lista de valores de la variable independiente.
        y (list of float/int): Lista de valores de la variable dependiente.

    Returns:
        float: La sumatoria cruzada de las desviaciones de x e y.
    """
    mediax = media(x)
    mediay = media(y)
    lista_xy = [(a - mediax) * (b - mediay) for a, b in zip(x, y)]
    sumatoria = sum(lista_xy)
    return sumatoria

def obtener_b1(x, y):
    """Calcula la pendiente (b1) de la recta de regresión lineal simple.

    Args:
        x (list of float/int): Lista de valores de la variable independiente.
        y (list of float/int): Lista de valores de la variable dependiente.

    Returns:
        float: El coeficiente de pendiente de la línea de mejor ajuste.
    """
    diferencia = diferencia_xy(x, y)
    diferencia_cuadrados = diferencia_cuadrado(x)
    return diferencia / diferencia_cuadrados

def obtener_b0(x, y):
    """Calcula la intersección con el eje y (b0) de la recta de regresión lineal simple.

    Args:
        x (list of float/int): Lista de valores de la variable independiente.
        y (list of float/int): Lista de valores de la variable dependiente.

    Returns:
        float: El valor de la ordenada al origen de la línea de mejor ajuste.
    """
    mediay = media(y)
    mediax = media(x)
    b1 = obtener_b1(x, y)
    return mediay - (b1 * mediax)

def regresion(x, y):
    """Obtiene los coeficientes de la recta de regresión lineal (y = b0 + b1*x).

    Args:
        x (list of float/int): Lista de valores de la variable independiente.
        y (list of float/int): Lista de valores de la variable dependiente.

    Returns:
        tuple: Una tupla que contiene (b0, b1), donde b0 es la intersección y b1 es la pendiente.
    """
    b1 = obtener_b1(x, y)
    b0 = obtener_b0(x, y)
    return b0, b1

# Ejecuciones y asignaciones
regresion(x, y)
b1 = obtener_b1(x, y)
b0 = obtener_b0(x, y)
