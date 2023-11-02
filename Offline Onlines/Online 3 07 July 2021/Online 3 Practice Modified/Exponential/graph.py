import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    i = s1 = s2 = s3 = s4 = 0
    for i in range(n):
    #while i < n:
        p = xL[i]
        q = yL[i]
        e = math.exp(x * p)
        eSq = e ** 2

        s1 += p * q * e
        s2 += q * e
        s3 += eSq
        s4 += p * eSq
        i += 1
    return s1 - ((s2 * s4) / s3)

#data gula rakhar jonno[input]
xL = []
yL = []

#Just taking input from file 
file = open("input.txt", "r")
n = int(file.readline())
s = file.read().split("\n")

for line in s:
    lineArray = line.split(" ")
    xL.append(float(lineArray[0]))
    yL.append(float(lineArray[1]))



        
        
#printing the inputs to check if it has read correctly
print(xL)
print(yL)

xGraph = np.linspace(-0.5, 0, 1000)
yGraph = []
for xl in xGraph:
    yGraph.append(f(xl))

fig, ax = plt.subplots()
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
#ax.axvline(x=0, color='k')

plt.plot(xGraph, yGraph)
plt.show()
