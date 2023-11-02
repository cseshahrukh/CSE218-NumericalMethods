# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 11:06:49 2021

@author: Asus
"""

import matplotlib.pyplot as plt
import numpy as np
from math import e

def func(x, y, b):
    n=len(x)
    sum1, sum2, sum3, sum4, sum5, sum6 = 0, 0, 0, 0, 0, 0
    for i in range(n):
        ex=e**(x[i])
        sum1+=ex*y[i]
        sum2+=x[i]**2
        sum3+=x[i]*y[i]
        sum4+=b*x[i]*ex
        sum5+=b*(ex**2)
        sum6+=x[i]*ex
    value=sum1-(((sum3-sum4)*sum6)/sum2)-sum5
    return value

def bisect(xl, xu, itmax, x, y):
    i = 0
    root = xl
    while(i<=itmax):
        xm=(xl+xu)/2
        if func(x,y, xl)*func(x,y,xm)==0:
            return xm
        elif func(x,y, xl)*func(x,y,xm)<0:
            xu=xm
        else:
            xl=xm
        root= xm
        i+=1
    return root

def exponentialRegression(x, y):
    n = len(x)
    sum1, sum2, sum3 = 0, 0, 0
    b=bisect(-1, 1, 100, x, y)
    for i in range(n):
        ex=e**x[i]
        sum1+=y[i]*x[i]
        sum2+=b*x[i]*ex
        sum3+=x[i]**2
    a=(sum1-sum2)/sum3
    return a, b

dt = open("data.txt", "r")
x=[]
y=[]

for i in dt:
    for j in [i.split()]:
        x.append(float(j[0]))
        y.append(float(j[1]))

(a, b)=exponentialRegression(x, y)
print("a =", a)
print("b =", b)

yp=[]
x_points=np.arange(0, 2, 0.01)

for i in x_points:
    ex=e**i
    value=(a*i)+(b*ex)
    yp.append(value)

plt.plot(x, y, '.', label='data points')
plt.plot(x_points, yp, label='exponential regression')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

dt.close()