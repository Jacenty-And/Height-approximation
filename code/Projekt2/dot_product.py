from Projekt2.matrix_methods import copyMatrix
from Projekt2.vector_methods import copyVector, zeroVector


def dotProduct(matrix, vector):
    copyMatrix1 = copyMatrix(matrix)
    copyVector1 = copyVector(vector)
    dotProd = zeroVector(len(copyMatrix1))

    for i in range(len(copyMatrix1)):
        for j in range(len(copyVector1)):
            dotProd[i] += copyMatrix1[i][j] * copyVector1[j]
    return dotProd