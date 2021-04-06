# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:40:59 2020

@author: jonat
"""


import pandas 
import numpy 


def main():
    data = pandas.read_excel("C:/Users/jonat/Documents/School/Data Analytics and Big Data/Assignment 4/fld1.xlsx",'Sheet1')
    # print(data)
    datafr = pandas.DataFrame.to_numpy(data)
    class1 = datafr[:300,:2]
    # print(class1)
    class0 = datafr[300:,:2]
    # print(class0)
    mean1 = numpy.mean(class1,axis=0)
    mean0 = numpy.mean(class0,axis=0)
    meant = mean1-mean0
    # print(meant)
    # print(mean1,mean0)
    submean1 = class1 - mean1
    submean0 = class0 - mean0
    # print(submean1)
    s1 = numpy.dot(numpy.transpose(submean1),submean1)
    s2 = numpy.dot(numpy.transpose(submean0),submean0)
    # print(cov0)
    sw = s1+s2
    # print(sw)
    w = numpy.dot(numpy.linalg.inv(sw),meant)
    # print(w)
    y = numpy.dot(datafr[:,1:],w)-0.0035    
    
    for x in range(len(y)):
        if y[x]>=0:
            print(y[x], 'Class 1')
        else:
            print(y[x],'Class 2')

    
main()
