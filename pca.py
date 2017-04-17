# !/usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd
import numpy
from numpy import *


def cal_contribution(w):
    contribution = []
    total_sum = sum(w)
    for item in w:
        contribution.append( (float(item))/ total_sum)
    return contribution


def cal_cumulative_contribution(w):
    cumulative_contribution = []
    total_sum = sum(w)
    cumulative_sum = 0.0
    for item in w:
        cumulative_sum += item
        cumulative_contribution.append(cumulative_sum / total_sum)
    return cumulative_contribution


def cal_principal_component_loading(w, v):
    result = []
    row = len(w)
    for i in range(0, row):
        result.append(list(sqrt(w[i]) * v[i]))
    return result



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

    R = numpy.corrcoef(x)

    print u"相关系数矩阵\n",R
    w, v = numpy.linalg.eig(R)
    print "特征值\n", w
    print "特征向量\n", v
    contribution = cal_contribution(w)
    print "贡献值\n", contribution
    cumulative_contribution = cal_cumulative_contribution(w)
    print "累计贡献值\n", cumulative_contribution
    loading = cal_principal_component_loading(w, v)
    print "主成分载荷\n", loading


