# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:44:09 2020

@author: Manya
"""

from copy import deepcopy
import numpy as np
import random

def succ_help(state, x, y):
    list = []
    # print(state);
    
    length = len(state)
    #max up or down you can move
    max = length
    # print(len(state))
   
    arr= [None]*length

    i = 0
    j = 0
    f_s = []
    if(state[x] != y):
        list = []
    else:
       while i < length:
          
            if(state[i] == y and i == x):
                # print(state[i])
                i+=1;
                continue;
            else:
                #move to the next index over
                if(state[i] + 1 < max):
                    # state[i] = state[i] + 1
                    state2 = deepcopy(state)
                    # print(state2)
                    state2[i] = state[i] + 1
                    # f_s.append(f(state2))
                
                    list.append(state2)
                    # print('max')
                if(state[i] - 1 >= 0):
                    # state[i] = state[i] - 1
                    state3 = deepcopy(state)
                    state3[i] = state[i] - 1
                    # f_s.append(f(state3))
                    
                    list.append(state3)
                    
                i+=1      
    list = sorted(list)
    # print(list)
    # print(f_s)
    return list


def succ(state, static_x, static_y):
    
    state2 = deepcopy(state);
    
    return succ_help(state2, static_x, static_y)


def f(state):
    
    attacc = 0
    length = len(state)
 
    outer = 0
    inner = 0
    
    for outer in range(length):
        row1 = state[outer]
        
        for inner in range(length):
            if(outer == inner):
                continue
            row2 = state[inner]
            
            if row1 == row2:
                attacc += 1
                break
            elif abs(row1-row2) == abs(outer-inner):
                attacc += 1
                break
            
    return attacc

def choose_next(state, x, y):
    if (succ(state, x, y) == []):
        return None 
    list1 = succ(state, x, y)
    list1.append(state) ## add staying this way to the candidate list
    list1 = sorted(list1) ## sort the candidates list in ascending order
    ret = state
    score = 1000
    for i in range(len(list1)):
        # print 'Current candidate: ', candidates[i], ' f-score: ', f(candidates[i])
        curr = f(list1[i])
        if (curr < score) :
            score = curr
            ret = list1[i]
    return ret


def n_queens(initial_state, static_x, static_y):
    
    init_copy = deepcopy(initial_state)
    next_s = []
    
    print(init_copy, ' - f=', f(init_copy) ,sep='' )

    for i in range(len (succ(init_copy, static_x, static_y) ) ):
        
        if(init_copy == choose_next(init_copy, static_x, static_y)):
            return init_copy
        
        next_s = choose_next(init_copy, static_x, static_y)
        print(next_s, ' - f=', f(next_s), sep='')
     
        if(f(init_copy) == f(next_s)):
            return next_s
        else:
            init_copy = next_s 

    return init_copy


#return true or false depending on if the puzzle is solved or not
def n_queen_restart_helper(list1, static_x, static_y):
      # got = n_queens(randomlist, static_x, static_y)
      got = []
      if(len(list1) == 0):
          return False
      got = n_queens(list1, static_x, static_y)
      # n_queens(list1, static_x, static_y)
        
      if(f(got) == 0):
          return True
        
      return False


def n_queens_restart(n, k, static_x, static_y):
   random.seed(1)
   randomlist = [0]*n
  
   for i in range(0,n):
       if(i == static_x):
            randomlist[i] = static_y    
       else:
           randomlist[i] = random.randint(0,n)
      
   print(randomlist)
    
   while i < k:
       if(n_queen_restart_helper(randomlist, static_x, static_y)):
           break;
    # make a new list
       randomlist = [0]*n
       
       for j in range(0,n):
           if(j == static_x):
               randomlist[j] = static_y    
           else:
               randomlist[j] = random.randint(0,n)
       i += 1
  



































