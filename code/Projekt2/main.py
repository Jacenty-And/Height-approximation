from matplotlib import pyplot

from matrix_class import *
from jacobi import *
from gauss_seidel import *
from lu_factorization import *

if __name__ == '__main__':

    # A
    mat = Matrix(184788)
    # A = mat.zadA()
    # for i in range(6):
    #     print(A[i])
    # print(mat.getVectorB())

    # B
    jacobi(mat.zadA(), mat.getVectorB())
    gaussSeidel(mat.zadA(), mat.getVectorB())

    # C
    C = mat.getMatrix(3, -1, -1)
    # for i in range(6):
    #     print(C[i])
    # jacobi(mat.getMatrix(3, -1, -1), mat.getVectorB())
    # gaussSeidel(mat.getMatrix(3, -1, -1), mat.getVectorB())
    # dla wartości a1=3 a2=a3=-1 metody iteracyjne się nie zbiegają

    # D
    luFactorization(mat.getMatrix(3, -1, -1), mat.getVectorB())

    # E
    N = [100, 500, 1000, 2000, 3000]
    time_j = []
    time_gs = []
    time_lu = []
    for n in N:
        print("N = ", n)
        mat.n = n
        A = mat.zadA()       # matrix A
        b = mat.getVectorB() # vector b

        time_j.append(jacobi(A, b))
        time_gs.append(gaussSeidel(A, b))
        time_lu.append(luFactorization(A, b))

    pyplot.plot(N, time_j, label="Jacobi", color="red")
    pyplot.plot(N, time_gs, label="Gauss-Seidl", color="green")
    pyplot.plot(N, time_lu, label="LU", color="blue")
    pyplot.legend()
    pyplot.grid(True)
    pyplot.ylabel('Czas (s)')
    pyplot.xlabel('Liczba niewiadomych')
    pyplot.title('Zależność czasu trwania algorytmów od liczby niewiadomych')
    pyplot.show()