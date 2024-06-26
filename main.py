"""
Módulo principal para procesar datos de gratuidad de libros de texto en Andalucía.
"""

import time

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
    csv_headers = lines[0].strip().split(',')
    csv_data = [line.strip().split(',') for line in lines[1:]]
    return csv_headers, csv_data

# Marcar tiempo de inicio
start_time = time.time()
leidos_headers, leidos_data = leer_csv(FILE_PATH)
# Marcar tiempo de fin y mostrar el tiempo transcurrido
end_time = time.time()
print(f"Tiempo en leer el archivo CSV: {end_time - start_time:.4f} segundos")

def filtrar_datos(datos, tipo_centro):
    """
    Filtra los datos por tipología de centro.
    
    Args:
    datos (list): Lista de datos del CSV.
    tipo_centro (str): Tipo de centro a filtrar ('Público' o 'Concertado').
    
    Returns:
    list: Datos filtrados por el tipo de centro especificado.
    """
    return [row for row in datos if row[2] == tipo_centro]

# Marcar tiempo de inicio
start_time = time.time()
publico = filtrar_datos(leidos_data, 'Público')
concertado = filtrar_datos(leidos_data, 'Concertado')
# Marcar tiempo de fin y mostrar el tiempo transcurrido
end_time = time.time()
print(f"Tiempo en filtrar los datos por tipología: {end_time - start_time:.4f} segundos")

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
        nombre_editorial = row[8]
        if nombre_editorial in conteo:
            conteo[nombre_editorial] += 1
        else:
            conteo[nombre_editorial] = 1
    return conteo

# Marcar tiempo de inicio
start_time = time.time()
editoriales_publico = contar_ocurrencias(publico)
editoriales_concertado = contar_ocurrencias(concertado)
# Marcar tiempo de fin y mostrar el tiempo transcurrido
end_time = time.time()
print(f"Tiempo en contar ocurrencias de editoriales: {end_time - start_time:.4f} segundos")

def obtener_top_3(conteo):
    """
    Obtiene el TOP 3 de editoriales según el conteo.
    
    Args:
    conteo (dict): Diccionario con el conteo de editoriales.
    
    Returns:
    list: Lista de las top 3 editoriales más frecuentes.
    """
    return sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]

# Marcar tiempo de inicio
start_time = time.time()
top_3_publico = obtener_top_3(editoriales_publico)
top_3_concertado = obtener_top_3(editoriales_concertado)
# Marcar tiempo de fin y mostrar el tiempo transcurrido
end_time = time.time()
print(f"Tiempo en obtener el TOP 3 de editoriales: {end_time - start_time:.4f} segundos")

# Mostrar resultados
print("Top 3 Editoriales en Centros Públicos:")
for editorial, count in top_3_publico:
    print(f"{editorial}: {count}")

print("\nTop 3 Editoriales en Centros Concertados:")
for editorial, count in top_3_concertado:
    print(f"{editorial}: {count}")
