import time

from dot_product import *

def jacobi(matrix, vector):
    start = time.time()
    matrix1 = copyMatrix(matrix)
    vector1 = copyVector(vector)
    vector_x = zeroVector(len(vector1))
    tmp_x = zeroVector(len(vector1))
    iterations = 0

    while True:
        for i in range(len(matrix1)):
            value = vector1[i]
            for j in range(len(matrix1)):
                if i != j:
                    value -= matrix1[i][j] * vector_x[j]
            value /= matrix1[i][i]
            tmp_x[i] = value
        vector_x = copyVector(tmp_x)
        res = subVector(dotProduct(matrix1, vector_x), vector1)

        iterations += 1
        if normVector(res) < pow(10, -9):
            end = time.time()
            break

    print("Jacobi's method")
    print('Time:', end - start)
    print('Iterations:', iterations)
    print()
    return (end - start)