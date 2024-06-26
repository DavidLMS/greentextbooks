"""
Módulo principal para procesar datos de gratuidad de libros de texto en Andalucía.
"""

# Constante para el path del archivo CSV
FILE_PATH = 'gratuidadlibrosdetextoandalucia.csv'

def leer_csv(file_path):
    """
    Lee un archivo CSV y devuelve sus encabezados y datos.
    
    Args:
    file_path (str): Ruta del archivo CSV a leer.
    
    Returns:
    tuple: Una tupla conteniendo los encabezados y los datos del CSV.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return headers, data

headers, data = leer_csv(FILE_PATH)

def filtrar_datos(data, tipo_centro):
    """
    Filtra los datos por tipología de centro.
    
    Args:
    data (list): Lista de datos del CSV.
    tipo_centro (str): Tipo de centro a filtrar ('Público' o 'Concertado').
    
    Returns:
    list: Datos filtrados por el tipo de centro especificado.
    """
    return [row for row in data if row[2] == tipo_centro]

publico = filtrar_datos(data, 'Público')
concertado = filtrar_datos(data, 'Concertado')

def contar_ocurrencias(lista):
    """
    Cuenta las ocurrencias de cada editorial en una lista de datos.
    
    Args:
    lista (list): Lista de datos del centro específico.
    
    Returns:
    dict: Un diccionario con el conteo de ocurrencias por editorial.
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

def obtener_top_3(conteo):
    """
    Obtiene el TOP 3 de editoriales según el conteo.
    
    Args:
    conteo (dict): Diccionario con el conteo de editoriales.
    
    Returns:
    list: Lista de las top 3 editoriales más frecuentes.
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