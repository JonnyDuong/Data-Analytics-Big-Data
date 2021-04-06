# Data-Analytics-Big-Data
Linear classification algorithms

Assignment 1
Question 1 – Using the Excel file dataA.xlsx, which contains a 500x3 data matrix (500 data points with 3 attributes), calculate both the mean and the covariance matrix.
Question 2 - Using the Excel file dataB.xlsx, which contains a 500x10 data matrix (500 data points with 10 attributes), calculate both the mean and the covariance matrix.
Question 3 – The data generated is random and normally distributed with a mean for dataA, dataB and covariance for dataA and dataB given in meanA.xlsx, meanB.xlsx, covarianceA.xlsx and covarianceB.xlsx respectively. Briefly explain why your answers are different from the parameters used to generate the data.

Assignment 3
Question 1:
Calculate the 6 multivariate regression parameters B0, B1, B2, B3 and B4, B5 for the data in RegressionData.xlsx where the input data X is on sheet 1 and the output data y is on sheet 2.

Assignment 4
Question 1. 
Using the multivariate data in the file fld1.xlsx:
(a)	determine the discriminant line found by Fishers Linear Discriminant.

(b)	Plot both the data and the discriminant line on a scatter plot 

(c)	Using this line, determine the class of each of the data points in the dataset, assuming that the threshold is 0 (i.e. positive values are in one class and negative values in the other).  

(d)	Determine what percentage of data points are incorrectly classified. 

NOTE: The first 2 columns in fld1.xlsx are data columns. The third column is the class to which each data point belongs.

Question 2.
Using the multivariate data in the file spam.xlsx, determine the discriminant line found by Fishers Linear Discriminant. Using this line, determine the class of each of the data points in the dataset, assuming that the threshold is 0. 
NOTE: The first 57 columns in spam.xlsx are data columns. The 58th column is the class to which each data point belongs.
Determine what percentage of the data points are incorrectly classified. You will notice that most of the data in the first class is classified correctly while the data in the second class is not. Therefore, it makes sense to adjust the threshold. Try the classification again a few times while adjusting the threshold so that it is a small negative number to see if you can improve the overall classification error rate (percentage of errors in BOTH classes). 
FYI, information about the dataset is given in the folder with the spam dataset. This is a real dataset, from the Machine Learning Repository at UCI (University of California Irvine). I simply made it a bit smaller by only using the first 500 data points from the first class and the first 500 data points from the second. The original database has over 4000 data points and it was awkward to work with that in Excel. I have not, however, reduced the number of attributes. For those that are interested in a real-life example, this is one. It is a dataset with attributes used to try to detect spam from email. 
