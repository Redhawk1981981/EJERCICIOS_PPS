def obtener_numeros():
    numeros = []
    while len(numeros) < 6:
        try:
            numero = int(input("Introduce un número ganador (entre 1 y 49): "))
            if 1 <= numero <= 49 and numero not in numeros:
                numeros.append(numero)
            else:
                print("Número inválido o repetido. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    return sorted(numeros)

if __name__ == "__main__":
    numeros_ganadores = obtener_numeros()
    print("Los números ganadores ordenados son:", ", ".join(map(str, numeros_ganadores)))