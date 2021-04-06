# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:32:11 2020

@author: jonat
"""

import pandas 
import numpy 

def main():
    data1 = pandas.read_excel("C:/Users/jonat/Documents/School/Data Analytics and Big Data/Assignment 1/multNormal.xlsx")
    offdiag = []
    var = []
    datanpy = pandas.DataFrame.to_numpy(data1)
    # print (data1)
    # print(datanpy)
    z = 2
    xz = 1
    # vrows,vcols = ()
    col = 0
    # print(datanpy[:1000,0])
    
    for i in range(0,19,2):
        # print(i)    
        # plots first column and second then iterates through dataset. 
        data1.plot.scatter(x = i, y = xz,c = "Red",s=0.25)
        
        # selects all data attributes. 1st iteartion uses columns i = 0 and z = 1.
        newdf = datanpy[:,i:z]
        # print(datanpy[:,i:z])
        # print(i,z)
        # print (newdf[:,i:z])
        mean = numpy.mean(newdf,axis=0) 
        # print (mean)
        
        # computes variance for each column in iteration for all data attributes.
        # variance1 = numpy.var(datanpy[:1000,col], axis = 0, ddof = 1)
        # variance2 = numpy.var(datanpy[:1000,col+1], axis = 0, ddof = 1)
        # print(variance1, variance2)
        
        # computes selected columns less new calculated mean for cov calculation
        submean = newdf - mean 
        # print(submean)
        
        # covariance calculation
        cov = numpy.dot(numpy.transpose(submean),submean)/(len(newdf)-1)
        # print(cov)
        #creates 2x2 array
        offdiag.append((cov[0][1],cov[1][0]))
        var.append((cov[0][0],cov[1][1]))

        # offdiag.append(cov[0][1])
        # offdiag.append(cocv[1][0])
        # print(cov)
        # print(variance1,variance2)
        # matplotlib.pyplot.scatter(cov[0],cov[1],c="Blue",s=0.25)
        # print()
        z = z + 2
        xz= xz + 2
        col = col + 1
    # print(covarray,'\t',var1,'\t',var
    #create 2x2 array send to pandas
    covframe = pandas.DataFrame.from_records(offdiag)
    varframe = pandas.DataFrame.from_records(var)
    
    # Covaraince:Blue, Shows positive linear relationship across pairs of columns. 
    covframe.plot.scatter(x=0,y=0,c='Blue',s=0.25)
    
    # Variance: Red, 1st point y axis shows high variance indicating points are differ greatly from mean. X axis shows low variance indiacting points are close to mean. 
    # Looking at scatter plot this directly correlates to the transformation. As variance across y axis approaches 0 data is more dense across the y.
    # Similarily, points across the x axis are less disperse are points form around x=0. 
    varframe.plot.scatter(x=0,y=1,c='Red',s=0.25)
    print('Covariance')
    print(covframe)
    print('\n')
    print("Variance")
    print(varframe)
    
main()

