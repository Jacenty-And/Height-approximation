def zeroVector(length):
    vector = []
    for _ in range(length):
        vector.append(0)
    return vector


def oneVector(length):
    vector = []
    for _ in range(length):
        vector.append(1)
    return vector


def diagVector(matrix):
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
    return diagonal


def copyVector(vector):
    copy = []
    for value in vector:
        copy.append(value)
    return copy


def addVector(vector1, vector2):
    vector = copyVector(vector1)
    for i in range(len(vector)):
        vector[i] += vector2[i]
    return vector


def subVector(vector1, vector2):
    vector = copyVector(vector1)
    for i in range(len(vector)):
        vector[i] -= vector2[i]
    return vector


def normVector(vector):
    counter = 0
    for value in vector:
        counter += (value ** 2)
    return (counter ** 0.5)