from Projekt2.dot_product import dotProduct
from Projekt2.matrix_methods import copyMatrix, diagToSqrMatrix, zeroMatrix
from Projekt2.vector_methods import oneVector, copyVector, zeroVector, subVector, normVector


def luFactorization(matrix, vector):
    m = len(matrix)

    matrix1 = copyMatrix(matrix)
    matrix_l = diagToSqrMatrix(oneVector(m))
    matrix_u = zeroMatrix(m, m)

    vector1 = copyVector(vector)
    vector_x = oneVector(m)
    vector_y = zeroVector(m)

    # Create L and U matrices
    # LUx = b
    for j in range(m):
        for i in range(j + 1):
            matrix_u[i][j] += matrix1[i][j]
            for k in range(i):
                matrix_u[i][j] -= matrix_l[i][k] * matrix_u[k][j]

        for i in range(j + 1, m):
            for k in range(j):
                matrix_l[i][j] -= matrix_l[i][k] * matrix_u[k][j]
            matrix_l[i][j] += matrix1[i][j]
            matrix_l[i][j] /= matrix_u[j][j]

    # Ly = b
    for i in range(m):
        value = vector1[i]
        for j in range(i):
            value -= matrix_l[i][j] * vector_y[j]

        vector_y[i] = value / matrix_l[i][i]

    # Ux = y
    for i in range(m - 1, -1, -1):
        value = vector_y[i]
        for j in range(i + 1, m):
            value -= matrix_u[i][j] * vector_x[j]
        vector_x[i] = value / matrix_u[i][i]

    res = subVector(dotProduct(matrix1, vector_x), vector1)
    return vector_x