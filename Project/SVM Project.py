# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:45:20 2020

@author: jonat
"""

import pandas as pd
import numpy as npy
import time
import operator
import qpsolvers
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split

data = pd.read_excel('default of credit card clients.xls')
data_np = pd.DataFrame.to_numpy(data)
data_all = npy.array(data_np[1:5001,:23])
# print(data_all)
# print(data_np[:,:-1])

data_sort = npy.array(sorted(data_all, key = operator.itemgetter(22)))
data_class = npy.array(data_sort[:,-1])
npy.savetxt('class_data.txt',data_class)
data_adj_class = -npy.ones(3893)
data_adj_class = npy.append(data_adj_class,npy.ones(1107))
# print(-npy.diag(data_adj_class))
# print(data_adj_class.shape)
# print(data_sort[:,:-1])
data_sort = data_sort[:,:-1]
# print(data_sort.shape)

""" P = npy.eye(22)
P = npy.append(P, npy.zeros((23,1)),axis = 1)
P = npy.append(P,npy.zeros((1,23)),axis = 0) + 0.00001*npy.eye(23)
q = npy.zeros(23)
G = npy.dot(-npy.diag(data_adj_class),npy.append(data_sort, npy.ones((5000,1)),axis = 1))
G2 = G.astype(npy.float64)
# print(G)
h = -npy.ones(5000)

w = qpsolvers.solve_qp(P, q, G2, h)
print("QP solution:", w) """ 

X_train = data_sort
Xtest = data_np[5001:5501,:-1]
y_train = data_adj_class
yTest = data_np[5001:5501,-1]
# print(Xtest.shape)

clf = svm.SVC(kernel='linear') 
clf.fit(X_train, y_train)
y_pred = clf.predict(Xtest)
print("Accuracy:",metrics.accuracy_score(yTest, y_pred))