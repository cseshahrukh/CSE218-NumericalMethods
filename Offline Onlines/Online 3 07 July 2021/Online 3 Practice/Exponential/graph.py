import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    i = f1 = f2 = f3 = f4 = 0
    while i < n:
        p = xL[i]
        q = yL[i]
        e = math.exp(x * p)
        eSq = e ** 2

        f1 += p * q * e
        f2 += q * e
        f3 += eSq
        f4 += p * eSq
        i += 1
    return f1 - ((f2 * f4) / f3)


xL = []
yL = []

# File related things
file = open("input.txt", "r")
n = int(file.readline())
s = file.read().split("\n")

for dum in s:
    dummy = dum.split(" ")
    xL.append(float(dummy[0]))
    yL.append(float(dummy[1]))

print(xL)
print(yL)

xList = np.linspace(-0.5, 0, 1000)
yList = []
for xl in xList:
    yList.append(f(xl))

fig, ax = plt.subplots()
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.plot(xList, yList)
plt.show()
