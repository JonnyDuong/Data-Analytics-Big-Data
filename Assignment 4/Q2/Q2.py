import matplotlib.pyplot
import numpy
import pandas


allData = pandas.read_excel("spam.xlsx")
data = allData.to_numpy()
x1 = data[0:500,0:57]
x2 = data[500:1000,0:57]
X = numpy.concatenate((x1,x2),0)
Xc = data[:,57]

u1 = numpy.mean(x1,0)
u2 = numpy.mean(x2,0)

x1mc = x1 - u1
x2mc = x2 - u2

S1 = numpy.dot(x1mc.T, x1mc)
S2 = numpy.dot(x2mc.T, x2mc)
Sw = S1 + S2

w = numpy.dot(numpy.linalg.inv(Sw),(u1 - u2))

threshold = -0.0025
prediction = (numpy.sign(numpy.dot(X,w) + threshold)+1)/2
y = numpy.dot(X,w) + threshold
# print(y)
# print(prediction)
# print (numpy.dot(X,w))
print("percent error = ", 100*sum(prediction != Xc)/1000)
# print(100*sum(prediction != Xc)/1000)

# print("done")







