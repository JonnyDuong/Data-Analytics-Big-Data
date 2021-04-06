import numpy
import matplotlib.pyplot

data = numpy.loadtxt('fld1.txt', delimiter = ',')

X = data[:,0:2]
Xc = data[:,2]
print(data)
x1 = X[Xc==1]
x2 = X[Xc==0]
# print (x2.shape)
print(x1)


u1 = numpy.mean(x1,0)
u2 = numpy.mean(x2,0)

x1mc = x1 - u1
x2mc = x2 - u2

S1 = numpy.dot(x1mc.T, x1mc)
S2 = numpy.dot(x2mc.T, x2mc)
Sw = S1 + S2
# print(Sw)
# print(S1)

w = numpy.dot(numpy.linalg.inv(Sw),(u1 - u2))

prediction = (numpy.sign((numpy.dot(X,w))+0.000067)+1)/2
print("percent error = ", 100*sum(prediction != Xc)/500)
# print(w)

slope = -w[0]/w[1]
intercept = 0

xline = numpy.linspace(-10,10)
yline = slope*xline + intercept
matplotlib.pyplot.scatter(x1[:,0], x1[:,1],c = 'r', marker = '.')
matplotlib.pyplot.scatter(x2[:,0], x2[:,1],c = 'b', marker = '.')
matplotlib.pyplot.plot(xline,yline, 'g')
matplotlib.pyplot.show()

