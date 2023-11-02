import matplotlib.pyplot as plt
import numpy as np

xList = []
yList = []

i = x = y = xy = xSq = 0
n = int(input())

for m in range(n):
    dum = input().split(" ")
    xList.append(int(dum[0]))
    yList.append(int(dum[1]))

while i < n:
    xy += xList[i] * yList[i]
    x += xList[i]
    y += yList[i]
    xSq += (xList[i]) ** 2
    i += 1

a1 = (n * xy - x * y) / (n * xSq - x ** 2)
a0 = (y - a1 * x) / n
print(a0, a1)


# Creating vectors X and Y
xEq = np.linspace(0, 5, 10)
yEq = a0 + a1 * xEq

fig = plt.figure(figsize=(10, 5))
# Create the plot
plt.plot(xEq, yEq, label="y = mx + c")
plt.scatter(xList, yList, color="green")

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.show()
# print(x, y, xy, xSq)
# print(xList)
# print(yList)

