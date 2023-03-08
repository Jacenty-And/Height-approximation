from Projekt2 import matrix_methods, vector_methods, lu_factorization


def spline(points):
    def calculate_params():
        n = len(points)

        A = matrix_methods.zeroMatrix(4 * (n - 1), 4 * (n - 1))
        b = vector_methods.zeroVector(4 * (n - 1))

        # Sj(xj) = f(xj)
        for i in range(n - 1):
            x, y = points[i]
            row = vector_methods.zeroVector(4 * (n - 1))
            row[4 * i + 3] = 1
            A[4 * i + 3] = row
            b[4 * i + 3] = (float(y))

        # Sj(xj+1) = f(xj+1)
        for i in range(n - 1):
            x1, y1 = points[i + 1]
            x0, y0 = points[i]
            h = float(x1) - float(x0)
            row = vector_methods.zeroVector(4 * (n - 1))
            row[4 * i] = h ** 3
            row[4 * i + 1] = h ** 2
            row[4 * i + 2] = h ** 1
            row[4 * i + 3] = 1
            A[4 * i + 2] = row
            b[4 * i + 2] = float(y1)

        # Dla węzłów wewnętrznych Sj-1'(xj) = Sj'(xj)
        for i in range(n - 2):
            x1, y1 = points[i + 1]
            x0, y0 = points[i]
            h = float(x1) - float(x0)
            row = vector_methods.zeroVector(4 * (n - 1))
            row[4 * i] = 3 * (h ** 2)
            row[4 * i + 1] = 2 * h
            row[4 * i + 2] = 1
            row[4 * (i + 1) + 2] = -1
            A[4 * i] = row
            b[4 * i] = float(0)

        # Dla węzłów wewnętrznych Sj-1''(xj) = Sj''(xj)
        for i in range(n - 2):
            x1, y1 = points[i + 1]
            x0, y0 = points[i]
            h = float(x1) - float(x0)
            row = vector_methods.zeroVector(4 * (n - 1))
            row[4 * i] = 6 * h
            row[4 * i + 1] = 2
            row[4 * (i + 1) + 1] = -2
            A[4 * (i + 1) + 1] = row
            b[4 * (i + 1) + 1] = float(0)

        # Na krawędziach S0''(x0) = 0 and Sn-1''(xn) = 0
        row = vector_methods.zeroVector(4 * (n - 1))
        row[1] = 2
        A[1] = row
        b[1] = float(0)

        row = vector_methods.zeroVector(4 * (n - 1))
        x1, y1 = points[-1]
        x0, y0 = points[-2]
        h = float(x1) - float(x0)
        row[1] = 2
        row[-4] = 6 * h
        A[-4] = row
        b[-4] = float(0)

        result = lu_factorization.luFactorization(A, b)
        return result

    params = calculate_params()

    def f(x):
        param_array = []
        row = []
        for param in params:
            row.append(param)
            if len(row) == 4:
                param_array.append(row.copy())
                row.clear()

        for i in range(1, len(points)):
            xi, yi = points[i-1]
            xj, yj = points[i]
            if float(xi) <= x <= float(xj):
                a, b, c, d = param_array[i - 1]
                h = x - float(xi)
                return (a * (h ** 3)) + (b * (h ** 2)) + (c * h) + d

        return None

    return f
