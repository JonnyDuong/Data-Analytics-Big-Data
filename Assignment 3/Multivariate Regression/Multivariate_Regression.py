import numpy
import random
import sklearn.linear_model

#x = numpy.array([-1, -1, 1, 1, 1])
#y = numpy.array([1, 1, 1, -1, -1])
#error = sum(x != y)

# what am I doing with b and X?
b = numpy.array([5.2, 2, 3, 4, 5, 6])

X = 10*numpy.random.random((5000,5)) - 5

Z = numpy.concatenate((numpy.ones((5000,1)), X), axis = 1)

e = numpy.random.normal(0,3,5000)

y = numpy.dot(Z,b) + e

bhat = numpy.dot(numpy.dot(numpy.linalg.inv(numpy.dot(Z.T,Z)),Z.T),y) 
print(bhat)

skregress = sklearn.linear_model.LinearRegression().fit(X,y)
print(skregress.coef_)
print(skregress.intercept_)

print("done")