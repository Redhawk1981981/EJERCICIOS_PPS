from ej3 import *

def test_escalar_longitud_diferente():
    vector1 = [1, 2, 3]
    vector2 = [1, 2]
    assert calcular_producto_escalar(vector1, vector2) is None

def test_producto_escalar():
    vector1 = [1, 2, 3]
    vector2 = [-1, 0, 2]
    assert calcular_producto_escalar(vector1, vector2) == 5