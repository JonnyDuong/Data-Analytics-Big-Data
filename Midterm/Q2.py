# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:50:00 2020

@author: jonat
"""

import numpy as npy

def main():
    std1 = npy.sqrt(npy.random.uniform(2,6,2))
    m1 = npy.random.uniform(-3,1,2)
    
    std2 = npy.sqrt(npy.random.uniform(1,4,2))
    m2 = npy.random.uniform(0,4,2)
    # print(std,m1)
    
    c1 = npy.random.normal(m1,std1,(1000,2))
    c1 = npy.concatenate((npy.ones((1000,1),dtype = int),c1), axis = 1)  
    
    c2 = npy.random.normal(m2,std2,(1000,2))
    c2 = npy.concatenate((npy.zeros((1000,1),dtype = int),c2), axis = 1)
    # print(c1.shape)
    
    c1 = npy.concatenate((c1,c2))
    # print(c1.shape)
    npy.savetxt('data2.txt',c1,delimiter = ' ')
main()

