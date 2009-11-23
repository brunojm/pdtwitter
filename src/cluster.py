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
        clusters[z] = []
        
    for j in range(n_i):
        # 2.1. allocation
        for data in dataset:
            dist = {}
            for k in prototypes.keys():
                dist[k] = distance(data, prototypes[k])
            # get the minimun of dist
            dst = dict(map(lambda item: (item[1],item[0]),dist.items()))
            min_k = dst[min(dst.keys())]
            # set this data to prototype (clusters)
            clusters[min_k].append(data)
            
        # 2.2. representation
        for z in range(k):
            c = {}
            for elem_base in clusters[z]:
                dist = 0
                for elem_for in clusters[z]:
                    dist += distance(elem_for, elem_base)
                c[elem_base] = dist
        