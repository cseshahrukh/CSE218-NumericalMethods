import matplotlib.pyplot as plt
import numpy as np

xList = []
yList = []

# File related things
f = open("input.txt", "r")
n = int(f.readline())
s = f.read().split("\n")

for dum in s:
    dummy = dum.split(" ")
    xList.append(float(dummy[0]))
    yList.append(float(dummy[1]))

# Setting initial values
i = x = y = xy = xSq = 0

# Calculation
while i < n:
    xy += xList[i] * yList[i]
    x += xList[i]
    y += yList[i]
    xSq += (xList[i]) ** 2
    i += 1

a1 = (n * xy - x * y) / (n * xSq - x ** 2)
a0 = (y - a1 * x) / n
print(a0, a1)

# Time for the graph #
# Creating vectors for variable x & y in eqn: y = mx + c
xEq = np.linspace(0, 5, 10)
yEq = a0 + a1 * xEq

# Idk why fig was written in the internet code
#fig = plt.figure(figsize=(10, 5))

# Plotting equation
plt.plot(xEq, yEq, label="y = a0 + a1 * x")

# Plotting points
plt.scatter(xList, yList, color="green")

# Plotting graph
plt.title('Curve Fitting')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid()
plt.legend()
plt.show()

# Debugging things
# print(x, y, xy, xSq)
# print(xList)
# print(yList)
