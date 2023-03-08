from math import sin


class Matrix:
    def __init__(self, index):  # index = 184788
        self.d = index % 10     # 18478[8]
        index = int(index / 10) # 18478
        self.c = index % 10     # 1847[8]
        index = int(index / 10) # 1847
        self.e = index % 10     # 184[7]
        index = int(index / 10) # 184
        self.f = index % 10     # 18[4]

        self.n = 9 * self.c * self.d
        
    def getMatrix(self, a1, a2, a3):
        A = []
        for i in range(self.n):
            A.append([])
            for j in range(self.n):
                A[i].append(0)
        for i in range(self.n):
            A[i][i] = a1
            if i + 1 < self.n:
                A[i + 1][i] = A[i][i + 1] = a2
            if i + 2 < self.n:
                A[i + 2][i] = A[i][i + 2] = a3
        return A

    def getVectorB(self):
        b = []
        for i in range(self.n):
            b.append(sin((i + 1) * (self.f + 1)))
        return b

    def zadA(self):
        return self.getMatrix(5 + self.e, -1, -1)