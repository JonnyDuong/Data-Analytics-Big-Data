# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 19:22:51 2020

@author: jonat
"""
import pandas 
import numpy 

def main():
    
    data = pandas.read_excel("C:/Users/jonat/Documents/School/Data Analytics and Big Data/Assignment 1/dataA.xlsx")
    datanpy = pandas.DataFrame.to_numpy(data)
    print (data)
    data.plot(kind='hist')
   
    mean = numpy.mean(datanpy, axis = 0)
    submean = datanpy - mean 
    cov = numpy.dot(numpy.transpose(submean),submean)/(len(datanpy)-1)
    
    print('\n',"mean",mean)
    print('\n',"Cov",cov)
    
main()

