# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:27:07 2020

@author: jonat
"""

import numpy as npy
import matplotlib.pyplot

def main():
    ct = npy.loadtxt('data2.txt',delimiter=' ')
    c1 = ct[:100,:]
    c2 = ct[100:,:]
    cAct = ct[:,0]
    # print(c2)
    
    u1 = npy.mean(c1)
    u2 = npy.mean(c2)

    subu1 = c1 - u1
    subu2 = c2 - u2
    
    s1 = npy.dot(subu1.T,subu1)
    s2 = npy.dot(subu2.T,subu2)
    sw = s1 + s2
    
    threshold = 0
    
    w = npy.dot(npy.linalg.inv(sw),(u1-u2))
    yz = npy.dot(ct,w) + threshold
    # print(yz)
    pred = (npy.sign(npy.dot(ct,w) + threshold)+1)/2
    # print(pred)
    error = 0
    
    for i in range(len(pred)):
        if pred[i] != cAct[i]:
            error = error + 1
        else:
            return 
  
    print ("Error %: ",(error/2000)*100)
    
    # error = 100*(sum(pred != cAct)/2000)
    # print(error)
    
    # b = w[0]/w[1]
    # x = npy.linspace(-10,10)
    # y = b*x 
    
    # matplotlib.pyplot.scatter(c1[:,0], c1[:,1],c = 'r', marker = '.')
    # matplotlib.pyplot.scatter(c1[:,0], c2[:,1],c = 'b', marker = '.')
    # matplotlib.pyplot.plot(x,y, 'g')
    # matplotlib.pyplot.show()

main()