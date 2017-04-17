# !/usr/bin/env python
import xlrd
import sys
import numpy
from numpy import *


def nondimensionalize1(x):
    row = len(x)
    col = len(x[0])
    for i in range(0, row):
        avg_x = float(sum(x[i])) / len(x[i])
        print 'avg_x', avg_x
        for j in range(0, col):
            x[i][j] /= avg_x


def nondimensionalize2(x):
    row = len(x)
    col = len(x[0])

    for i in range(0, row):
        x0 = x[i][0]
        for j in range(0, col):
            x[i][j] /= x0


def cal_delta(x):
    deltas = []
    row = len(x)
    col = len(x[0])
    for i in range(1, row):
        delta = []
        for j in range(0, col):
            delta.append(abs(x[0][j]-x[i][j]))
        deltas.append(delta)
    return deltas


def cal_a_and_b(deltas):
    row = len(deltas)
    col = len(deltas[0])
    a = 0
    b = sys.maxint
    for i in range(0, row):
        for j in range(0, col):
            a = a if a > deltas[i][j] else deltas[i][j]
            b = b if b < deltas[i][j] else deltas[i][j]
    return a, b


def cal_coefficient(deltas, a, b, p=0.5):
    row = len(deltas)
    col = len(deltas[0])
    coefficients = []
    for i in range(0, row):
        coefficient = []
        for j in range(0, col):
            val = (b + p * a) / (deltas[i][j] + p * a)
            print b ,'+', p, '*', a , '/(', deltas[i][j], '+', p , '*', a ,') = ', val
            coefficient.append(val)

        coefficients.append(coefficient)
        print coefficient, '-'
    return coefficients


def cal_correlation(coefficients):
    row = len(coefficients)
    col = len(coefficients[0])
    correlation = []
    for i in range(0, row):
        val = float(sum(coefficients[i])) / col
        correlation.append(val)
    return correlation


def print_x(x):
    row = len(x)
    for i in range(0, row):
        print x[i]
    print


if __name__ == '__main__':
    filename = '/Users/yunweiguo/Desktop/test3.0.xlsx'
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name("Sheet1")
    result = []
    nrows = sh.nrows
    ncols = sh.ncols
    x = []
    cols = []
    for i in range(0, ncols):
        cols.append([])
    for i in range(1, nrows):
        for j in range(0, ncols):
            cols[j].append(float(sh.cell_value(i, j)))

    for i in range(0, ncols):
        x.append(cols[i])
    # x = [[2045.3, 1942.2, 1637.2, 1884.2, 1602.3],
    #      [34374.0, 31793.0, 27319.0, 32516.0, 16297.0],
    #      [14.6792, 14.8449, 1.4774, 46.604, 9.4959],
    #      [120.9, 100.1, 65.9, 80.52, 54.22],
    #      [0.3069, 0.7409, 0.361, 3.7, 2.0213],
    #      [49.4201, 34.8699, 50.974, 50.4325, 40.8828]]
    x = [[14.44, 12.92, 13.6, 11.9],
         [3.15, 3.59, 2.64, 3.38],
         [14.50, 14.85, 14.17, 14.92],
         [0.78, 0.76, 0.81, 0.77],
         [2.26, 2.70, 2.66, 2.52]]


    print_x(x)
    nondimensionalize1(x)
    print 'nondimensionalize2'
    print_x(x)
    deltas = cal_delta(x)
    print 'deltas'
    print_x(deltas)
    a, b = cal_a_and_b(deltas)
    print a, b
    coefficients = cal_coefficient(deltas, a, b)
    print_x(coefficients)
    correlations = cal_correlation(coefficients)
    print_x(correlations)


    x0 = [41.0, 206.0, 199.0, 29.0, 0.0, 0.0, 23.0, 0.0, 0.0, 199.0, 471.0, 707.0, 730.0, 659.0, 704.0, 121.0, 0.0, 0.0, 0.0, 0.0, 11.0, 500.0, 593.0, 641.0, 735.0, 621.0, 587.0, 0.0, 0.0, 0.0, 0.0, 0.0, 154.0, 358.0, 574.0, 743.0, 639.0, 661.0, 427.0, 0.0, 0.0, 0.0, 0.0, 0.0, 19.0, 223.0, 433.0, 511.0, 694.0, 451.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 309.0, 693.0, 702.0, 713.0, 541.0]
    x1 = [5894.064516129032, 4347.25, 4376.1612903225805, 6406.299999999999, 11329.354838709678, 17624.666666666668, 12198.387096774195, 9995.16129032258, 10206.0, 3535.709677419355, 3063.2, 2455.838709677419, 2254.741935483871, 2200.7241379310344, 2388.612903225807, 3082.0666666666666, 9205.741935483871, 10379.333333333334, 22484.838709677417, 11556.451612903227, 6587.6, 2424.4193548387098, 2134.2999999999997, 2008.1290322580644, 2399.467741935484, 2733.642857142857, 3061.741935483871, 4484.3, 12338.935483870968, 32240.0, 14059.032258064515, 9373.870967741936, 5703.766666666666, 3195.1612903225805, 2764.1333333333337, 2123.709677419355, 1842.3225806451615, 1759.0142857142857, 3421.3548387096776, 5284.2, 11316.774193548386, 22323.666666666668, 32847.74193548387, 19658.064516129034, 6586.166666666667, 3788.4193548387093, 3937.3, 3008.9032258064517, 2774.967741935484, 2860.428571428571, 3922.516129032258, 4427.2, 6246.774193548387, 17198.0, 10861.612903225807, 10037.419354838708, 10633.133333333333, 3582.935483870968, 2894.233333333333, 2380.3225806451615, 2953.3548387096776, 4003.0344827586205]
    x2 = [2.102, 2.112, 2.112, 2.052, 2.112, 2.062, 1.992, 2.142, 2.292, 2.362, 2.302, 2.192, 2.042, 1.992, 2.102, 2.042, 2.092, 2.142, 2.032, 2.122, 2.152, 2.352, 2.192, 2.132, 2.132, 2.072, 2.101143107065286, 1.982, 2.022, 2.042, 2.002, 2.012, 2.292, 2.312, 2.242, 2.222, 2.1015291213142446, 2.182, 2.072, 2.052, 2.112, 2.042, 2.012, 2.202, 2.242, 2.292, 2.252, 2.272, 2.112, 1.982, 2.122, 2.062, 2.022, 1.962, 1.962, 2.032, 2.242, 2.332, 2.372, 2.192, 2.212, 2.162]

    R = numpy.corrcoef([x0, x1, x2])


