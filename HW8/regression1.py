# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:25:35 2020

@author: Manya
"""

import csv
import math
from numpy import matrix as np
import numpy as numpy
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import pandas as pd
from copy import deepcopy
from numpy.linalg import inv

def get_dataset(filepath):

    with open(filepath, newline='') as iris:
        # returning from 2nd row
        data = list(csv.reader(iris, delimiter=','))[1:]
        result = numpy.array(data).astype("float")

    b = numpy.delete(result, 0, axis=1)

    return b


# 1 = density etc.
def print_stats(dataset, col):

    i = 0
    tot = 0
    # for the std
    arr = numpy.zeros(shape=(252, 1))
    print(len(dataset))

    while i < len(dataset):
        tot += dataset[i][col]
        i += 1

    answer = tot/len(dataset)
    answer = str(round(answer, 2))
    print(answer)

    i = 0
    while i < len(dataset):
        arr[i] = float(dataset[i][col])
        i += 1

    arr1 = numpy.array(arr)

    std = numpy.std(arr1)
    answer1 = str(round(std, 2))
    print(answer1)


def regression(dataset, cols, betas):
   
    tot = 0

    for row in range(len(dataset)):
        s_e = betas[0]
        i = 1
        for col in cols:
            
            s_e += betas[i] * dataset[row][col]
            i += 1

        s_e = s_e - dataset[row][0]
        s_e = numpy.square(s_e)
        tot += s_e

    m_s_e = tot/(len(dataset))

    return m_s_e


def gradient_descent(dataset, cols, betas):

    num = len(dataset)
    tot = 0

    arr = []
    arr1 = []

    index = 0
    a = 0

    # go upto the beta which is at the last index of cols array
    while a <= cols[(len(cols)-1)]:
        tot = 0
        if (index == 0):

            for row in range(num):
                s_e = betas[0]
                i = 1
                for col in cols:
                    s_e += betas[i] * dataset[row][col]
                    i += 1

                s_e = s_e - dataset[row][0]
                tot += s_e

                g_d = (2*tot)/num
            arr1.append(g_d)

        # MULTIPLY Xij
        else:
            for row in range(num):
                s_e = betas[0]
                i = 1
                for col in cols:
                    s_e += betas[i] * dataset[row][col]
                    i += 1

                s_e = s_e - dataset[row][0]
                s_e = s_e * dataset[row][index]
                tot += s_e

                g_d = (2*tot)/num

        index += 1
        a += 1
        arr.append(g_d)

    # the betas that are needed are col indices
    b = 0
    while b < len(cols):

        arr1.append(arr[cols[b]])
        b += 1

    ret = numpy.array(arr1)

    return ret


def iterate_gradient(dataset, cols, betas, T, eta):

    size = int(T)
    ret = numpy.empty(shape=(size, 5))
    ret.fill(1)

    i = 0
    while i < T:
        # 0 is the indices upto T
        # f"{num:.9f}"
        index = i + 1
        ret[i][0] = index

        # 1 is current MSE
        grads = gradient_descent(dataset, cols, betas)
        a = 0
        while a < len(betas):
            betas[a] = betas[a] - (eta*grads[a])
            a += 1
        mse = float(regression(dataset, cols, betas))
        ret[i][1] = str(float(round(mse, 2)))
        ret[i][2] = float(betas[0])
        ret[i][3] = float(betas[1])
        ret[i][4] = float(betas[2])
        i += 1

    i = 0
    while i < T:
        print(str(int(ret[i][0])),
              "{:.2f}".format(ret[i][1]),
              "{:.2f}".format(ret[i][2]),
              "{:.2f}".format(ret[i][3]),
              "{:.2f}".format(ret[i][4]))

        i += 1

def compute_betas(dataset, cols) :

    data_copy = deepcopy(dataset)
    ones = numpy.ones( (len(dataset), 1)) 
    
    extractedData = data_copy[:,[cols[0],cols[1]]]
    x = numpy.hstack( (ones, extractedData) ) 

    x_copy = deepcopy(x)
    transpose = x.transpose()
    
    dot = np.dot(transpose, x)
    inverse = inv(dot)
    
    betas = np.dot(inverse, transpose)
    
    i = 0
    y = numpy.empty( (len(data_copy), 1) )
  
    # # bodyfat column
    while i < len(data_copy):
        y[i] = data_copy[i][0]
        i += 1
        
    betas = np.dot(transpose,y)
    ret_betas = np.dot(inverse, betas)
    
    in_betas = ret_betas.ravel()
   
    mse = regression(dataset, cols, in_betas)


    tup = (mse, in_betas[0], in_betas[cols[0]], in_betas[cols[1]])
    return tup
 
    
def predict(dataset, cols, features):
    
    betas = []*(len(cols)+1)
    
    tup = compute_betas(dataset, cols)
    
    i = 1
    while i < len(tup):
        betas.append(tup[i])
        i += 1

    pred = betas[0]
    i = 1
    while i < len(betas):
        pred += betas[i]*features[i-1]
        i +=1
        
    return pred
    
    





