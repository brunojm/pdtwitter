#!/usr/bin/python
# -*- coding: utf-8 -*-
# Bruno Melo (bjmm@acm.org)
import random

n_r = 200 # number of repetitions
n_i = 100 # number of maximum iterations
k = 7 # number of clusters

dataset = [['python', 'robots', 'russell'], ['psicologia', 'python'], ['javascript', 'web'], ['psicologia', 'estatistica']]
prototypes = {}
clusters = {}

def distance(data, prototype):
    pass

for i in range(n_r):
    # 1. initialization
    for z in range(k):
        prototypes[z] = dataset[random.randint(0, len(dataset) - 1)]
        
    for j in range(n_i):
        # 2.1. allocation
        for data in dataset:
            dist = {}
            for k in prototypes.keys():
                dist[k] = distance(data, prototypes[k])
            # get the minimun of dist
            # set this data to prototype (clusters)
        
        # 2.2. representation
        for z in range(k):
            # for all elements in cluster z
            # 
            pass
