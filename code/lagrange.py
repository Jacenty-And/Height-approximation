def lagrange(points):
    def f(x):
        sum = 0
        n = len(points)
        for i in range(n):
            x_i, y_i = points[i]
            product = 1
            for j in range(n):
                if i != j:
                    x_j, y_j = points[j]
                    product *= (float(x) - float(x_j)) / (float(x_i) - float(x_j))
            sum += float(y_i) * product
        return sum
    return f
