import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    i = f1 = f2 = f3 = f4 = 0
    while i < n:
        p = xList[i]
        q = yList[i]
        e = math.exp(x * p)
        eSq = e ** 2

        f1 += p * q * e
        f2 += q * e
        f3 += eSq
        f4 += p * eSq
        i += 1
    return f1 - (f2 / f3) * f4


def a(x):
    i = f2 = f3 = 0
    while i < n:
        p = xList[i]
        q = yList[i]
        e = math.exp(x * p)
        eSq = e ** 2

        f2 += q * e
        f3 += eSq
        i += 1
    return f2 / f3


def bisection(lowerBound, upperBound, errorBound=0.5, maxIteration=20):
    midValue = 0
    for i in range(maxIteration):
        midValue = (lowerBound + upperBound) / 2
        temp = f(lowerBound) * f(midValue)
        # print(temp)

        if temp < 0:
            upperBound = midValue
        elif temp > 0:
            lowerBound = midValue
        else:
            break

        newMidValue = (lowerBound + upperBound) / 2
        error = abs((newMidValue - midValue) / newMidValue) * 100
        if error < errorBound:
            break
    return midValue


xList = []
yList = []

# File related things
file = open("input.txt", "r")
n = int(file.readline())
s = file.read().split("\n")

for dum in s:
    dummy = dum.split(" ")
    xList.append(float(dummy[0]))
    yList.append(float(dummy[1]))

lamb = bisection(-0.2, 0)
A = a(lamb)
print(lamb)
print(A)

# Time for the graph #
# Creating vectors for variable x & y in eqn: y = Ae^(lambda * x)
xEq = np.linspace(-2, 12, 100)
yEq = []
for xl in xEq:
    yEq.append(A * math.exp(lamb * xl))

# Idk why fig was written in the internet code
fig = plt.figure(figsize=(10, 5))

# Plotting equation
plt.plot(xEq, yEq, label="y = Ae^(lambda * x)")

# Plotting points
plt.scatter(xList, yList, color="green")

# Plotting graph
plt.title('Curve Fitting')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid()
plt.legend()
plt.show()
