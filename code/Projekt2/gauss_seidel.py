import time

from dot_product import *

def gaussSeidel(matrix, vector):
    start = time.time()
    matrix1 = copyMatrix(matrix)
    vector1 = copyVector(vector)
    vector_x = zeroVector(len(matrix1[0]))
    iterations = 0

    while True:
        for i in range(len(matrix1)):
            value = vector1[i]
            for j in range(len(matrix1)):
                if i != j:
                    value -= matrix1[i][j] * vector_x[j]
            value /= matrix1[i][i]
            vector_x[i] = value
        res = subVector(dotProduct(matrix1, vector_x), vector1)

        iterations += 1
        if normVector(res) < pow(10, -9):
            end = time.time()
            break

    print("Gauss-Seidel's method")
    print("Time:", end - start)
    print("Iterations:", iterations)
    print()
    return (end - start)