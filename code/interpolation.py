import csv
import os

from matplotlib import pyplot


def interpolation(func, k, scale="lin"):
    for file in os.listdir('./height_profiles'):
        f = open('./height_profiles/' + file, 'r')
        data = list(csv.reader(f))

        interpolation_data = data[1::k]

        F = func(interpolation_data)

        distance = []
        height = []
        interpolated_height = []
        for point in data[1:]:
            x, y = point
            distance.append(float(x))
            height.append(float(y))
            interpolated_height.append(F(float(x)))

        train_distance = []
        train_height = []
        for point in interpolation_data:
            x, y = point
            train_distance.append(float(x))
            train_height.append(F(float(x)))

        if scale == "log":
            # skala logarytmiczna
            pyplot.semilogy(distance, height, 'g.', label='Dane z pliku')
            pyplot.semilogy(train_distance, train_height, 'r^', label='Punkty interpolacji')
            pyplot.semilogy(distance, interpolated_height, color='blue', label='Interpolacja')
        else:
            # skala liniowa
            pyplot.plot(distance, height, 'g.', label='Dane z pliku')
            pyplot.plot(train_distance, train_height, 'r^', label='Punkty interpolacji')
            pyplot.plot(distance, interpolated_height, color='blue', label='Interpolacja')

        pyplot.legend()
        pyplot.title('Aproksymacja profilu wysokościowego: ' + file[:-4] + '\n' +
                     'Interpolacja ' + func.__name__.capitalize() + ' dla ' + str(len(interpolation_data)) + ' punktów')
        pyplot.ylabel('Wysokość [m]')
        pyplot.xlabel('Odległość [m]')
        pyplot.grid()
        pyplot.show()
