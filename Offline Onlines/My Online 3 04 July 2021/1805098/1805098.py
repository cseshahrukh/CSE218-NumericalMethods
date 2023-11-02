# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:01:31 2021

@author: Md. Shahrukh Islam
"""

import matplotlib.pyplot as plt
import numpy as np
import math

cList = []
kList = []
n=0
# File related things
f = open("data.txt", "r")
#n = int(f.readline())
s = f.read().split("\n")

for dum in s:
    dummy = dum.split(" ")
    cList.append(float(dummy[0]))
    kList.append(float(dummy[1]))
    n=n+1

# Setting initial values
i = x = y = xy = xSq = 0

# Calculation
while i < n:
    xt=1/(cList[i]*cList[i])
    yt=1/(kList[i])
    xy += xt*yt
    x += xt
    y += yt
    xSq += (xt) ** 2
    i += 1

a1 = (n * xy - x * y) / (n * xSq - x ** 2)
a0 = (y - a1 * x) / n
#print(a0, a1)


kmax=1/a0
cs=a1*kmax

print("Kmax is ", kmax)
print("Cs is", cs)

# Time for the graph #
# Creating vectors for variable x & y in eqn: y = mx + c
cEq=[]
xEq = np.linspace(0.001, 1, 100)
for x in xEq:
    cEq.append(math.sqrt(1/(x)))
yEq = a0 + a1 * xEq
kEq=1/yEq

# Idk why fig was written in the internet code
#fig = plt.figure(figsize=(10, 5))

# Plotting equation
plt.plot(cEq, kEq, label="growth vs concentration")

# Plotting points
plt.scatter(cList, kList, color="green")

# Plotting graph
plt.title('Curve Fitting')
plt.xlabel('C')
plt.ylabel('growth of bacteria')
plt.grid()
plt.legend()
plt.show()