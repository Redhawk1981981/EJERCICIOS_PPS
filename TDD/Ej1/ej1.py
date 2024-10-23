# Escribir un programa que pida al usuario una palabra 
# y muestre por pantalla si es un palíndromo.

def palindromo(palabra):    
    palabra_inv = palabra
    palabra = list(palabra)
    palabra_inv = list(palabra_inv)
    palabra_inv.reverse()
    if palabra == palabra_inv:
        return True
    else:
        return False

if __name__ == "__main__":
    palabra = input("Introduce una palabra: ")