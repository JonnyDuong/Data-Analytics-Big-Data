# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:03:13 2020

@author: jonat
"""

import pandas 
import numpy 

def main():
    data = pandas.read_excel("C:/Users/jonat/Documents/School/Data Analytics and Big Data/Assignment 1/dataB.xlsx")
    datanpy = pandas.DataFrame.to_numpy(data)
    print (data)
    data.plot(kind='hist')
    mean = numpy.mean(datanpy, axis = 0)
    
    submean = datanpy - mean 
    cov = numpy.dot(numpy.transpose(submean),submean)/(len(datanpy)-1)
    print("mean",mean)
    print('\n',"Cov",cov)
    # print(len(datanpy))
main()
