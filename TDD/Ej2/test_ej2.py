from ej2 import *

def test_obtener_numeros():
    assert sorted([5, 2, 8, 1, 9, 3]) == [1, 2, 3, 5, 8, 9]
    assert sorted([10, 20, 30]) == [10, 20, 30]
    assert sorted([49, 1, 25]) == [1, 25, 49]