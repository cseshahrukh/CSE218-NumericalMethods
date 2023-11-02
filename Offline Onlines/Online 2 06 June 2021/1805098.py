# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 10:54:37 2021

@author: USER
"""


import numpy as np
import matplotlib.pyplot as plt


n = 4


x1=[22, 25,27,30]
y1=[44,43,42,40]

x11=[25, 27, 30]
y11=[43, 42, 40]
x1p = 28
y1p = 0
yss=0

# Implement
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (x1p - x1[j])/(x1[i] - x1[j])

    y1p = y1p + p * y1[i]   
    #fn(x) = sum of   Li * f(xi)

for i in range(n-1):
    p = 1
    for j in range(n-1):
        if i != j:
            p = p * (x1p - x11[j])/(x11[i] - x11[j])

    yss = yss + p * y11[i]   
    #fn(x) = sum of   Li * f(xi)
print('Interpolated value at %.3f is %.3f.' % (x1p, y1p))
#print('Interpolated value at %.3f is %.3f.' % (x1p, yss))


abs_rel= abs((y1p- yss)/y1p)* 100
print("Absolute Error:" , abs_rel)


x2=[30,31,35,37]
y2=[40,35,30,25]

x2p = 32
y2p = 0
x11=[30,31,35]
y11=[40,35,30]
yss=0


for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (x2p - x2[j])/(x2[i] - x2[j])

    y2p = y2p + p * y2[i]   
    #fn(x) = sum of   Li * f(xi)

print('Interpolated value at %.3f is %.3f.' % (x2p, y2p))

for i in range(n-1):
    p = 1
    for j in range(n-1):
        if i != j:
            p = p * (x2p - x11[j])/(x11[i] - x11[j])

    yss = yss + p * y11[i]   
    #fn(x) = sum of   Li * f(xi)
    

abs_rel= abs((y2p- yss)/y2p)* 100
print("Absolute Error:" , abs_rel)




x11= [22,25,27,28,30]
y11 = [44,43, 42, y1p, 40]

plt.plot(x11, y11)
plt.scatter(x11, y11)

x22=[30,31,32, 35,37]
y22=[40,35, y2p, 30,25]

plt.plot(x22, y22)
plt.scatter(x22, y22)




