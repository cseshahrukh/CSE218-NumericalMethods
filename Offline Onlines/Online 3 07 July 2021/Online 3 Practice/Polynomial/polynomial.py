import matplotlib.pyplot as plt
import numpy as np


def GaussianElimination(A, B, d=False):
    for i in range(p - 1):
        for j in range(i + 1, p):
            pivot = A[j][i] / A[i][i]

            temp_1 = A[i] * pivot
            A[j] = A[j] - temp_1

            temp_2 = B[i] * pivot
            B[j] = B[j] - temp_2

            if d:
                print(np.around(A, 4))
                print(np.around(B, 4))

    for i in range(p - 1, -1, -1):
        temp_3 = A[i][i+1:] * answer[i+1:]
        answer[i] = (B[i] - np.sum(temp_3)) / A[i][i]

    #return answer.reshape(p, 1)
    return answer
#p is order of polynomial + 1


xList = []
yList = []

# File related things
file = open("polynomial.txt", "r")
n = int(file.readline())
s = file.read().split("\n")

for dum in s:
    dummy = dum.split(" ")
    xList.append(float(dummy[0]))
    yList.append(float(dummy[1]) * pow(10, -6))

m = int(input("Order of polynomial: "))
entries = [n]
for i in range(1, 2 * m + 1):
    entries.append(sum(x ** i for x in xList))
# print(entries)

p = m + 1 #m is order of polynomial
coefficient = np.zeros(p ** 2).reshape(p, p)
constant = np.zeros(p).reshape(p, 1)
answer = np.zeros(p)

for i in range(p):
    j = p + i
    coefficient[i] = entries[i:j]
    constant[i] = sum((x ** i) * y for x, y in zip(xList, yList))

# print(coefficient)
# print(constant)
a = GaussianElimination(coefficient, constant)

for i in range(p):
    print(a[i])
    
# Time for the graph #
# Creating vectors for variable x & y in eqn: y = a0 + a1 * x + a2 * x^2 + .... + am * x^m
xEq = np.linspace(-400, 100, 1000)
yEq = []
for xl in xEq:
    y = 0
    for i in range(p):
        y += a[i] * (xl ** i)
    yEq.append(y)

# Idk why fig was written in the internet code
fig = plt.figure(figsize=(10, 5))

# Plotting equation
plt.plot(xEq, yEq, label="y = a0 + a1 * x + a2 * x^2")

# Plotting points
plt.scatter(xList, yList, color="green")

# Plotting graph
plt.title('Curve Fitting')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid()
plt.legend()
plt.show()
