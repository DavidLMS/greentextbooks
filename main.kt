import java.io.File
import kotlin.system.measureTimeMillis

fun leerCsv(filePath: String): Pair<List<String>, List<List<String>>> {
    val begin = System.currentTimeMillis()
    val lines = File(filePath).readLines()
    val headers = lines[0].split(",")
    val data = lines.drop(1).map { it.split(",") }
    val end = System.currentTimeMillis()
    println("Tiempo en leer el archivo CSV: ${(end-begin) / 1000.0} segundos")
    return Pair(headers, data)
}

fun filtrarDatos(datos: List<List<String>>, tipoCentro: String): List<List<String>> {
    return datos.filter { it[2] == tipoCentro }
}

fun contarOcurrencias(lista: List<List<String>>): Map<String, Int> {
    return lista.groupingBy { it[8] }.eachCount()
}

fun obtenerTop3(conteo: Map<String, Int>): List<Pair<String, Int>> {
    return conteo.entries.sortedByDescending { it.value }.take(3).map { it.toPair() }
}

fun main() {
    val filePath = "gratuidadlibrosdetextoandalucia.csv"

    val (_, data) = leerCsv(filePath)  // Volvemos a leer los datos para usarlos más adelante
    
    // Medir tiempo de filtrado
    val tiempoFiltrado = measureTimeMillis {
        val publico = filtrarDatos(data, "Público")
        val concertado = filtrarDatos(data, "Concertado")
    }
    println("Tiempo en filtrar los datos por tipología: ${tiempoFiltrado / 1000.0} segundos")

    val publico = filtrarDatos(data, "Público")
    val concertado = filtrarDatos(data, "Concertado")

    // Medir tiempo de conteo de ocurrencias
    val tiempoConteo = measureTimeMillis {
        val editorialesPublico = contarOcurrencias(publico)
        val editorialesConcertado = contarOcurrencias(concertado)
    }
    println("Tiempo en contar ocurrencias de editoriales: ${tiempoConteo / 1000.0} segundos")

    val editorialesPublico = contarOcurrencias(publico)
    val editorialesConcertado = contarOcurrencias(concertado)

    // Medir tiempo de obtener el top 3
    val tiempoTop3 = measureTimeMillis {
        val top3Publico = obtenerTop3(editorialesPublico)
        val top3Concertado = obtenerTop3(editorialesConcertado)
    }
    println("Tiempo en obtener el TOP 3 de editoriales: ${tiempoTop3 / 1000.0} segundos")

    val top3Publico = obtenerTop3(editorialesPublico)
    val top3Concertado = obtenerTop3(editorialesConcertado)

    // Mostrar resultados
    println("Top 3 Editoriales en Centros Públicos:")
    for ((editorial, count) in top3Publico) {
        println("$editorial: $count")
    }

    println("\nTop 3 Editoriales en Centros Concertados:")
    for ((editorial, count) in top3Concertado) {
        println("$editorial: $count")
    }
}
