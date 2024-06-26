import cProfile
# Paso 1: Leer el archivo CSV
file_path = 'gratuidadlibrosdetextoandalucia.csv'

def leer_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return headers, data

cProfile.run("headers, data = leer_csv(file_path)")

# Paso 2: Filtrar los datos por tipología de centro
publico = [row for row in data if row[2] == 'Público']
concertado = [row for row in data if row[2] == 'Concertado']

# Paso 3: Contar las ocurrencias de cada editorial por tipología de centro
def contar_ocurrencias(lista):
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
