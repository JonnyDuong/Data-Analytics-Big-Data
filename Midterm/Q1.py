# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:57:06 2020

@author: jonat
"""

import numpy as npy

def main():
    x = npy.random.uniform(-10,11,(1000,30))
    # print(x.shape)
    error = npy.random.normal(0,3,1000)
    # print(error)
    beta = npy.random.uniform(-10,11,31)
    npy.savetxt('betas.txt',beta,delimiter=' ')
    # print(beta.shape)
    z = npy.concatenate((npy.ones((1000,1)), x), axis = 1) 
    # print(z.shape)
    y = npy.dot(z,beta) + error
    # z = npy.concatenate((x,y), axis=1)
    npy.savetxt('datay.txt',y,delimiter = ' ')
    npy.savetxt('datax.txt',z,delimiter= ' ')
    # datax = npy.concatenate
    # print(datax)
main()