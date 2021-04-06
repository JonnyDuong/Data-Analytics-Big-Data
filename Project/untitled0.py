# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:23:57 2020

@author: jonat
"""

import pandas as pd
import numpy as npy
import time
import operator
import qpsolvers

data = pd.read_excel('default of credit card clients.xls')
data_np = pd.DataFrame.to_numpy(data)
data_all = npy.array(data_np[1:5001,:24])
# print(data_all)

data_sort = npy.array(sorted(data_all, key = operator.itemgetter(23)))
data_class = npy.array(data_sort[:,-1])
npy.savetxt('class_data.txt',data_class)
data_adj_class = -npy.ones(3893)
data_adj_class = npy.append(data_adj_class,npy.ones(1107))
# print(-npy.diag(data_adj_class))
# print(data_adj_class.shape)
# print(data_sort[:,:-1])
data_sort = data_sort[:,:-1]
# print(data_sort.shape)

P = npy.eye(23)
P = npy.append(P, npy.zeros((23,1)),axis = 1)
P = npy.append(P,npy.zeros((1,24)),axis = 0) + 0.00001*npy.eye(24)
q = npy.zeros(24)
G = npy.dot(-npy.diag(data_adj_class),npy.append(data_sort, npy.ones((5000,1)),axis = 1))
G2 = G.astype(npy.float64)
# print(G)
h = -npy.ones(5000)

w = qpsolvers.solve_qp(P, q, G2, h)
print("QP solution:", w)