import statistics

def calcular_estadisticas(numeros):
    media = statistics.mean(numeros)
    desviacion_tipica = statistics.stdev(numeros)
    return media, desviacion_tipica

if __name__ == "__main__":
    entrada = input("Introduce una muestra de números, separados por comas: ")
    numeros = [float(x) for x in entrada.split(",")]
    media, desviacion_tipica = calcular_estadisticas(numeros)
    print(f"La media es: {media}")
    print(f"La desviación típica es: {desviacion_tipica}")