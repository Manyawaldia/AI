# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:01:12 2020

@author: Manya
"""
import scipy
from scipy.linalg import eigh  
import numpy as np
import matplotlib.pyplot as plt  
import math

def load_and_center_dataset(filename):
    
    x = np.load(filename)
    x = np.reshape(x, (2000,784))
    arr = x - np.mean(x, axis=0)
    
    return arr;

def get_covariance(dataset):
    
    x = np.array(dataset)
    np.transpose(x)
    arr = np.dot(np.transpose(x), x)
    arr = arr/(len(x)-1)
    
    return arr

def get_eig(S, m):
    
    eigs = scipy.linalg.eigh(S)
    eig_vals = eigs[0]
    eig_vecs = eigs[1]
    
    sort_val = np.sort(eig_vals)[::-1]
       
    val_ret = []
    vec_ret = []
    
    for i in range(len(sort_val) - 1, len(sort_val)-1-m, -1):
        vec_ret.append(eig_vecs[:,i])
        val_ret.append(eig_vals[i])

    vec_ret = np.array(vec_ret)
    Lambda = np.diag(val_ret)
    vec_ret = np.transpose(vec_ret)

    return Lambda, vec_ret
   
    
def get_eig_perc(S, perc): 
      
    eigs = scipy.linalg.eigh(S)
    eig_vals = eigs[0]
    eig_vecs = eigs[1]
    
    arr_vals = []
    ret_vec = []
    
    val_tot = np.sum(eig_vals)
    
    for i in range(len(eig_vals)):
        if( eig_vals[len(eig_vals)-i-1]/val_tot >= perc):
            arr_vals.append(eig_vals[len(eig_vals)-i-1])
            ret_vec.append(eig_vecs[:,len(eig_vals)-i-1])

    Lambda = np.diag(arr_vals)

    ret_vec = np.array(ret_vec)
    ret_vec = np.transpose(ret_vec)
   
    return Lambda, ret_vec

def project_image(image, U):
    
    x = np.transpose(U)
    prod = np.dot(x, image)
    ret = np.matmul(U, prod)

    return ret

def display_image(orig, proj):
    
    orig_size =  int (math.sqrt(len(orig)))
    proj_size = int (math.sqrt(len(proj)))
    original = np.reshape(orig,(orig_size, orig_size))
    projection = np.reshape(proj,(proj_size,proj_size))

    figure,(img, img_1) = plt.subplots(1, 2, sharex=True, sharey=False, figsize=(9,3))
    img.plot(orig_size,orig_size)
    img_1.plot(proj_size,proj_size)
    
    img.set_title('Original')
    img_1.set_title('Projection')

    orig_plot = img.imshow(original, aspect='equal', cmap='gray')
    proj_plot = img_1.imshow(projection, aspect='equal', cmap='gray')

    figure.colorbar(orig_plot, ax=img)
    figure.colorbar(proj_plot, ax=img_1)

    plt.show()





