from ejercicio1 import *

palabra = "ala"
def test_palindromo(palabra):

    assert palindromo(palabra) == True
    assert palindromo("ola") == False