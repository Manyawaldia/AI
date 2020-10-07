# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:08:57 2020

@author: Manya
"""
import csv
from pprint import pprint
from datetime import datetime

def manhattan_distance(data_point1, data_point2): 
    #use the appropriate keys from the dictionary 
    key_needed=['TMAX', 'PRCP', 'TMIN']
    dict1 = {key:data_point1[key] for key in key_needed}
    dict2 = {key:data_point2[key] for key in key_needed}
    #use sum to add all the appropriate values
    i = sum(dict1.values())
    j = sum(dict2.values())
    #return the absolute value of the difference of the two points
    return abs(i-j)
 
def read_dataset(filename):
    keys=['Date', 'TMAX', 'PRCP', 'TMIN', 'RAIN']
    dicts = []
    with open(filename) as f:
        for line in f: 
            line = line.strip().split()
            d = dict(zip(keys,line))
            dicts.append(d)
    return dicts

def majority_vote(nearest_neighbors):
    key_need = ['RAIN']
    f = 0 
    t = 0
    i = 0
    length = len(nearest_neighbors)
    #count the trues and the falses
    while i < length:
        if(nearest_neighbors[i]['RAIN'] == 'FALSE'):
            f+=1
        else:
            t+=1
        i+=1
                
    if(t >= f):
        return "TRUE"
    else:
        return "FALSE"
    
def k_nearest_neighbors(filename, test_point, k, year_interval):
    date = ['DATE']
    dict = read_dataset(filename)
    length = len(dict)
    c = test_point['DATE']
    i = 0
    j = 0
    a = 0
    # f is false and t is true
    f = 0
    t = 0
    #take the first four digits (year)
    b = c[:4]
    #a is the start year
    a = int(b)
    
    #how many data points needed
    while j < k:
        while i<length:
            if(dict[i]['RAIN'] == 'FALSE'):
                f += 1
            else:
                t += 1
            i += 10
        j += 1
    
    if(t>=f):
        return "TRUE"
    else:
        return "FALSE"
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        

    
    
