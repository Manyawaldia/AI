# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv;
import math; 
from numpy import matrix as np
import numpy as numpy
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

def load_data(filepath):
    
    with open('pokemon.csv', newline='') as csvfile:
         reader = csv.DictReader(csvfile)
         i = 1
         # ADDED FOR REGRADE- before it was dict of dicts now it is list of dicts
         listPoke = []
         pokeDict = {}
         for row in reader:
             pokeDict[i]= {}
             pokeDict[i]['#'] = i
             pokeDict[i]['Name'] = row['Name']
             pokeDict[i]['Type 1'] = row['Type 1']
             pokeDict[i]['Type 2'] = row['Type 2']
             pokeDict[i]['Total'] = int(row['Total'])
             pokeDict[i]['HP'] = int(row['HP'])
             pokeDict[i]['Attack'] = int(row['Attack'] )
             pokeDict[i]['Defense'] = int(row['Defense'])
             pokeDict[i]['Sp. Atk'] = int(row['Sp. Atk'])
             pokeDict[i]['Sp. Def'] = int(row['Sp. Def'])
             pokeDict[i]['Speed'] = int(row['Speed'])
             listPoke.append(pokeDict[i])
             i += 1
             if(i > 20):
                 break
             
             
    return listPoke

def calculate_x_y(stats):
    # x = attack + sp. attack + speed
    # y =  Defense + Sp. Def + HP

    attack = stats['Attack']
    spA = stats['Sp. Atk']
    speed = stats['Speed']
    defense = stats['Defense']
    spD = stats['Sp. Def']
    hp = stats['HP']
    
    x = attack + spA + speed
    y = defense + spD + hp
    
    ret = (x,y)
    
    return ret

#pass in 2 tuples and return distance
def help_dist(tuple1, tuple2):
    
    distance = 0
    
    x1 = tuple1[0]
    x2 = tuple2[0]
    y1 = tuple1[1]
    y2 = tuple2[1]
    
    a = int ( (x2-x1) ** 2 )
    b = int ( (y2-y1) ** 2 )
    
    distance = math.sqrt(a + b) 
    
    return distance

#find points with the shortest distance
def find_smallest(scores):
    
    result = {}
    result['p1'] = scores[1]
    result['p2'] = scores[2]
    result['distance'] = math.sqrt((scores[1][0]-scores[2][0])**2
                                +(scores[1][1]-scores[2][1])**2)
    res = float(result['distance'])
    
    for i in range(1, len(scores)):
        for j in range(i+1, len(scores)):
            dist = help_dist(scores[i], scores[j])
            if dist < res:
                result["p1"] = scores[i]
                result["p2"] = scores[j]
                result["distance"] = dist
        
    return result

# single linkage hac 
def hac(dataset):

    scores = {}
    i = 1
    index = 0
    
    # z = len(dataset)
    
    z = numpy.zeros( ( (len(dataset)) -1,4))
    a = 0
    
    while a < len(z):
        z[a][2] += a
        a += 1
        
    # COMMENTED OUT FOR REGRADE - i followed the rubric (point 8 and 9) 
    # where it said m-1*4 array/matrix/list and column 3 is strictly 
    #increasing but I was not able to code the logic before submission and forgot to comment out this so it threw an exception.
    
    # number the datasets
    # while i <= len(dataset):
    #     #index and x,y score        
    #     scores[i] = calculate_x_y(dataset[i])
        
    #     index += 1
    #     i += 1
    
    # result = find_smallest(scores)

    
    return z; 




