import os
from os import walk
import glob
import fnmatch
import collections 
import numpy as np
from collections import defaultdict
from collections import Counter
from copy import deepcopy


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
    cnter = Counter()
    cnt = 0
    vocab1 = dict.fromkeys(vocab, 0)
        
    print(vocab1)
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
    # TODO: add your code here


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
    # flat_list.sort()
    dupes = []
    unique = set(flat_list)
    for i in unique:
        if(flat_list.count(i) >= cutoff):
            dupes.append(i)
    vocab =dupes
    flat_list2=[]
    for item in vocab:
        flat_list2.append(item)
  
    vocab = flat_list2
    # print(len(vocab))
    return vocab

def prior(training_data, label_list):
    """ return the prior probability of the label in the training set
        => frequency of DOCUMENTS
    """
    
    
    smooth = 1 # smoothing factor
    logprob = {}
    # TODO: add your code here


    return logprob

def p_word_given_label(vocab, training_data, label):
    """ return the class conditional probability of label over all words, with smoothing """
    
    smooth = 1 # smoothing factor
    word_prob = {}
    # TODO: add your code here
    
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
    # TODO: add your code here


    return retval


def classify(model, filepath):
    """ return a dictionary formatted as follows:
            {
             'predicted y': <'2016' or '2020'>, 
             'log p(y=2016|x)': <log probability of 2016 label for the document>, 
             'log p(y=2020|x)': <log probability of 2020 label for the document>
            }
    """
    retval = {}
    # TODO: add your code here


    return retval


