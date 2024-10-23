from ej4 import *

def test_estadisticas():
    numeros = [1, 2, 3, 4, 5]
    media, desviacion_tipica = calcular_estadisticas(numeros)
    assert round(media, 2) == 3.00
    assert round(desviacion_tipica, 2) == 1.58

def test_estadisticas_negativos():
    numeros = [-1, 0, 1]
    media, desviacion_tipica = calcular_estadisticas(numeros)
    assert media == 0
    assert round(desviacion_tipica, 2) == 1.00