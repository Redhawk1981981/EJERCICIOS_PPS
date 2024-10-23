from ej1 import *

palabra = "ala"
def test_palindromo():
    assert palindromo("ala") == True
    assert palindromo("ola") == False

test_palindromo()