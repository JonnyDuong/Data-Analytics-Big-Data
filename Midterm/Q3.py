# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:06:22 2020

@author: jonat
"""

import numpy as npy

def main():
    x = npy.loadtxt('datax.txt',delimiter=' ')
    y = npy.loadtxt('datay.txt',delimiter=' ')
    betaAct = npy.loadtxt('betas.txt', delimiter=' ')
    # print(betaAct)
    # print(x.shape,y.shape)
    
    betatest = npy.dot(npy.linalg.pinv(x),y)
    # print(betatest)
    
    xtest = npy.random.uniform(-10,11,(500,30))
    error = npy.random.normal(0,3,500)
    ztest = npy.concatenate((npy.ones((500,1)), xtest), axis = 1)
    
    ytest = npy.dot(ztest,betaAct) + error
    # print(ytest.shape)
    
    ypred = npy.dot(ztest,betatest)
    
    error = ytest - ypred 
    MSE = npy.sum(npy.square(error))/500
    print(MSE)
main()
