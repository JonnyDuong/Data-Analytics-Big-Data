# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:37:56 2020

@author: jonat
"""

import pandas 
import numpy 

def main():
    xdata = pandas.read_excel("C:/Users/jonat/Documents/School/Data Analytics and Big Data/Assignment 3/RegressionData.xlsx",'Sheet1')
    ydata = pandas.read_excel("C:/Users/jonat/Documents/School/Data Analytics and Big Data/Assignment 3/RegressionData.xlsx",'Sheet2')
    x = pandas.DataFrame.to_numpy(xdata)
    # print(x)
    y = pandas.DataFrame.to_numpy(ydata)
    # print(y)
    z = numpy.concatenate((numpy.ones((500,1)), x), axis = 1)
    # print(z)
    beta = numpy.dot(numpy.dot(numpy.linalg.inv(numpy.dot(z.T,z)),z.T),y)
    print(beta)
    
    
main()