def calcular_producto_escalar(vector1, vector2):
    if len(vector1) != len(vector2):
        return None
    producto = 0
    for i in range(len(vector1)):
        producto += vector1[i] * vector2[i]
    return producto

if __name__ == "__main__":
    vector1 = [1, 2, 3]
    vector2 = [-1, 0, 2]
    resultado = calcular_producto_escalar(vector1, vector2)
    print(f"El producto escalar de {vector1} y {vector2} es: {resultado}")