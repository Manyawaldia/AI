import os
from os.path import dirname as up
from os import walk
import glob
import fnmatch
import collections 
import numpy as np
from collections import defaultdict
from collections import Counter
from copy import deepcopy
from pathlib import Path
import math
import numpy as np

def create_bow(vocab, filepath):
    """ Create a single dictionary for the data
        Note: label may be None
    """
    bow = {}
    words = []
    
    with open(filepath, encoding="utf8") as f:
        line = f.read().splitlines()
        words.append(line)

    flat_list = []
    for sublist in words:
        for item in sublist:
            flat_list.append(item)
            
    none_cnt = 0
    vocab1 = dict.fromkeys(vocab, 0)
        
    # print(vocab1)
    for i in range(0, len(flat_list)):
        if flat_list[i] not in vocab1:
            none_cnt += 1
            bow[None] = none_cnt
        else:
            bow[flat_list[i]] = bow.get(flat_list[i], 0) + 1
        
    return bow

def load_training_data(vocab, directory):
    """ Create the list of dictionaries """
    dataset = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = root + '/' + file
            dictionary = {}
            dictionary['label'] = os.path.basename(root) 
            dictionary['bow']= create_bow(vocab, filepath)
            dataset.append(dictionary)
    
    return dataset

def create_vocabulary(directory, cutoff):
    """ Create a vocabulary from the training directory
        return a sorted vocabulary list
    """
    
    vocab = []
    for dirpath, dirnames, filename in os.walk(directory, topdown=True):
        for filename in filename:
            # create full path
            txtfile_full_path = os.path.join(dirpath, filename)
            with open(txtfile_full_path, encoding="utf8") as f:
                # print(txtfile_full_path)
                line = f.read().splitlines()
                vocab.append(line)
                # print(vocab)
    flat_list = []
    for sublist in vocab:
        for item in sublist:
            flat_list.append(item)
            
    dupes = []
    unique = set(flat_list)
    for i in unique:
        if(flat_list.count(i) >= cutoff):
            dupes.append(i)
    vocab = dupes
    # print(vocab)
    vocab.sort()
   
    return vocab

def prior(training_data, label_list):
    """ return the prior probability of the label in the training set
        => frequency of DOCUMENTS
    """ 
    #smooth = 1 # smoothing factor
    logprob = {}
   
    count = [0]*len(label_list)
    
    for i in range(0, len(label_list)):
        for j in training_data:
            if (j['label'] == label_list[i]):
                count[i] += 1
             
    total = 0        
    for i in range(0, len(training_data)):
        total += 1
  
    for i in range(0, len(count)):
        tot = count[i] + 1 
        logtot = np.log(tot)
        tot2 = total + 2
        logtot2 = np.log(tot2)
        logg = logtot - logtot2
        logprob[label_list[i]] = logg
    
    return logprob

def p_word_given_label(vocab, training_data, label):
    word_prob = {}
    size_vocab = len(vocab)
    ## only use data w the good label
    match =[]
    vocab = deepcopy(vocab)

    if(size_vocab>=1 and vocab[size_vocab-1]!=None):
        vocab.append(None)
    # print(vocab)
    for i in training_data:
        if(i['label'] == label):
            match.append(i)
    # total = 0
    # count = 0
    for i in vocab:
        total = 0
        count = 0
        for j in match:
            bow = j['bow']
            # print(bow)
            total += sum(bow.values())
            if(bow.__contains__(i)):
                appears= bow[i]
                # print(bow)
                count += appears
    
        # prob = (count+1)/(total + size_vocab + 1)
        # prob = np.log(prob)
        a = count+1
        b = total + size_vocab + 1
        loga = np.log(a)
        logb = np.log(b)
        prob = loga - logb
        word_prob[i] = prob
    # print(count)
    return word_prob

    
##################################################################################
def train(training_directory, cutoff):
    """ return a dictionary formatted as follows:
            {
             'vocabulary': <the training set vocabulary>,
             'log prior': <the output of prior()>,
             'log p(w|y=2016)': <the output of p_word_given_label() for 2016>,
             'log p(w|y=2020)': <the output of p_word_given_label() for 2020>
            }
    """
    retval = {}
    vocab = create_vocabulary(training_directory, cutoff)
    
    training_data = load_training_data(vocab, training_directory)
    label_list = []
    #find the labels
    for root, dirs, files in os.walk(training_directory):
       for file in files:
           label_list.append(os.path.basename(root)) 
           
    label_list = list(dict.fromkeys(label_list))       
    priorr = prior(training_data, label_list)
 
    retval['vocabulary'] = create_vocabulary(training_directory, cutoff)
    retval['log prior'] = priorr
    
    for i in label_list:
        retval['log p(w|y=' + i +')'] = p_word_given_label(vocab, training_data, i)
    
    return retval


def classify(model, file):
    tot16 = 0
    tot20 = 0
    
    cond_prob = model['log p(w|y=2016)']
    cond_prob1 = model['log p(w|y=2020)']
    priorr = model['log prior']
    
    with open(file, "r") as f: 
        for word in f:
            word = word.rstrip()
            if word in cond_prob:
                tot16 += cond_prob[word]
            if word in cond_prob1:
                tot20 += cond_prob1[word]
            else:
                tot16 += cond_prob[None]
                tot20 += cond_prob1[None]
   
    tot16 += priorr['2016']
    tot20 += priorr['2020']
    
    retval = {}
    retval['log p(y=2016|x)'] = tot16
    retval['log p(y=2020|x)'] = tot20
    
    if tot20 > tot16:
        retval['predicted y'] = '2020'
    else: 
        retval['predicted y'] = '2016'
    
    return retval



























