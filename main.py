"""
Este módulo realiza un análisis de un archivo CSV que contiene información sobre
editoriales de libros de texto en Andalucía, clasificando los datos por tipología de centro y
mostrando el top 3 de editoriales más comunes en centros públicos y concertados.
"""

import cProfile

# Paso 1: Leer el archivo CSV
FILE_PATH = 'gratuidadlibrosdetextoandalucia.csv'

def leer_csv(path):
    """
    Lee un archivo CSV y retorna los encabezados y datos.

    Args:
        path (str): La ruta del archivo CSV.

    Returns:
        tuple: Una tupla que contiene una lista de encabezados y una lista de datos.
    """
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return headers, data

# Marcar tiempo de inicio
headers, data = leer_csv(FILE_PATH)

# Paso 2: Filtrar los datos por tipología de centro
publico = [row for row in data if row[2] == 'Público']
concertado = [row for row in data if row[2] == 'Concertado']

# Paso 3: Contar las ocurrencias de cada editorial por tipología de centro
def contar_ocurrencias(lista):
    """
    Cuenta las ocurrencias de cada editorial en la lista proporcionada.

    Args:
        lista (list): Una lista de filas de datos donde cada fila es una lista de valores.

    Returns:
        dict: Un diccionario con el nombre de la editorial como clave y su conteo como valor.
    """
    conteo = {}
    for row in lista:
        editorial = row[8]
        if editorial in conteo:
            conteo[editorial] += 1
        else:
            conteo[editorial] = 1
    return conteo

editoriales_publico = contar_ocurrencias(publico)
editoriales_concertado = contar_ocurrencias(concertado)

# Paso 4: Obtener el TOP 3 de editoriales para cada tipología
def obtener_top_3(conteo):
    """
    Obtiene el top 3 de elementos en un diccionario basado en sus valores.

    Args:
        conteo (dict): Un diccionario con elementos y sus conteos.

    Returns:
        list: Una lista de tuplas con los 3 elementos con mayor conteo.
    """
    return sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]

top_3_publico = obtener_top_3(editoriales_publico)
top_3_concertado = obtener_top_3(editoriales_concertado)

# Mostrar resultados
print("Top 3 Editoriales en Centros Públicos:")
for editorial, count in top_3_publico:
    print(f"{editorial}: {count}")

print("\nTop 3 Editoriales en Centros Concertados:")
for editorial, count in top_3_concertado:
    print(f"{editorial}: {count}")

cProfile.run("headers, data = leer_csv(FILE_PATH)")
