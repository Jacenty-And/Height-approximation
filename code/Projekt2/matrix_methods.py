def zeroMatrix(x, y):
    matrix = []
    for i in range(x):
        matrix.append([])
        for j in range(y):
            matrix[i].append(0)
    return matrix


def copyMatrix(matrix):
    copy = []
    for row in matrix:
        newRow = []
        for value in row:
            newRow.append(value)
        copy.append(newRow)
    return copy


def addMatrix(matrix1, matrix2):
    matrix = copyMatrix(matrix1)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += matrix2[i][j]
    return matrix


def subMatrix(matrix1, matrix2):
    matrix = copyMatrix(matrix1)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] -= matrix2[i][j]
    return matrix

def diagToSqrMatrix(vector):
    square = zeroMatrix(len(vector), len(vector))
    for i in range(len(vector)):
        square[i][i] = vector[i]
    return square