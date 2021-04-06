# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:25:25 2020

@author: jonat
"""

import pandas as pd
import numpy as npy
import time
import operator

def main():
    data = pd.read_excel('default of credit card clients.xls')
    data_np = pd.DataFrame.to_numpy(data)
    data_all = npy.array(data_np[1:,:22])
    data_class = data_np[1:,-1]
    # print(data_all[0])
    # print(data_class.shape)
    
    data_slice = npy.array(data_np[1:5000,:])
    # print(data_slice)
    data_train = data_slice[:3750,:23]
    # print(data_train)
    
    data_sort = npy.array(sorted(data_train, key = operator.itemgetter(22)))
    
    # print(data_sort)
    
    # print(data_class)
    # npy.savetxt('data_sort.txt',data_sort)
    
    class_neg = npy.array(data_sort[:2917,:22])
    # print(class_neg.shape)
    class_pos = npy.array(data_sort[2917:,:22])
    # print(class_pos[0])
    
    u0 = npy.mean(class_neg,0)
    u1 = npy.mean(class_pos,0)
    u2 = u0-u1
    # print(u2)
    
    class0_less_u0 = class_neg - u0 
    class1_less_u1 = class_pos - u1
    # print(class0_less_u0.shape)
    
    s1 = npy.dot(class0_less_u0.T,class0_less_u0)
    s2 = npy.dot(class1_less_u1.T,class1_less_u1)
    sw = s1 + s2
    sw = sw.astype(npy.float64)
    # print(sw.shape))
    w = npy.dot(npy.linalg.inv(sw),u2)
    # print(w)
    
    initial = npy.dot(data_all,w)
    # npy.savetxt('prediction.txt',initial)
    # print(initial)
    prediction = (npy.sign(npy.dot(data_all,w) - 0.00068)+1)/2
    comparison = npy.vstack((prediction, data_class)).T
    print(comparison)
    # npy.savetxt('compare.txt',comparison)
    # print(prediction)
    print("percent error = ", 100*sum(prediction != data_class)/30000)
main()