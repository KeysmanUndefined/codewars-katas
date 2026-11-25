numeros = [10, 20, 30, 40, 50]


def calcular_estadisticas(numeros):
    media = sum(numeros) / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)

    return media, maximo, minimo


def mostrar_estadisticas():
    resultados = calcular_estadisticas(numeros)
    print("Resultados:", resultados)


for indice in range(len(numeros)):
    print("Elemento", indice, ":", numeros[indice])


mostrar_estadisticas()