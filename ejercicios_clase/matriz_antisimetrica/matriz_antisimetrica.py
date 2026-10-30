# Define una rutina que devuelve True si una matriz es
# atisimetrica y False en otro caso.
# Una matriz n*n es antisimetrica si se verifica que
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i]
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.


def esAntisimetrica(matriz):

    for fila in matriz:
        if len(fila) != len(matriz):
            return False

    antisimetrica = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != - matriz[j][i]:
             antisimetrica = False
    return antisimetrica


if __name__ == "__main__":


    assert esAntisimetrica([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]) == True

    assert esAntisimetrica([
    [0, 1, 2],
    [-1, 0, 3],
    [-2, -3, 0]
]) == True


    assert esAntisimetrica([
    [0, 1, 2],
    [-1, 0, -2],
    [2, 2, 3]
]) == False

    assert esAntisimetrica([
    [1, 2, 5],
    [0, 1, -9],
    [0, 0, 1]
]) == False

# Matrices no cuadradas
    matriz4 = [
    [1, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1]
]

    assert esAntisimetrica(matriz4) == False

    matriz5 = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0]
]

    assert esAntisimetrica(matriz5) == False