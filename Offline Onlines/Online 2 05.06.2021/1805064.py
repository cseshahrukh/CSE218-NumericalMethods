# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:11:05 2021

@author: ASUS
"""
import matplotlib.pyplot as plt
#from sympy import *

def product(value, x, i):
    pro= 1;
    for j in range(i):
        pro= pro* (value- x[j])
    return pro

def calculate_value(value, x, y, n):
    sum= y[0][0]
    for i in range(1, n):
        sum= sum+ y[0][i]* product(value, x, i)
    return sum

def datatable(x, y, n):
    for i in range(1, n):
        for j in range(n-i):
            y[j][i]= (y[j][i-1]- y[j+1][i-1])/(x[j]- x[j+i])
    return y

def print_table(y, n):
    for i in range(n):
        for j in range(n-i):
            print(y[i][j], "\t", end= " ")
        print("")
    

#Mass
n= 5
y= [[0 for i in range(10)] for j in range(10)]
x= [19, 22, 26, 28, 30]

y[0][0]= 1203
y[1][0]= 1245
y[2][0]= 1378
y[3][0]= 1315
y[4][0]= 1475

y= datatable(x, y, n)
#print_table(y, n)
value= 25

value1= calculate_value(value, x, y, 5)
print("Mass at:" , value, "is", round(value1, 4))
abs_rel= abs((value1- calculate_value(value, x, y, 4))/value1)* 100
print("Absolute Error:" , abs_rel)

#Velocity
n=5
y1= [[0 for i in range(10)] for j in range(10)]
x= [19, 22, 26, 28, 30]


y1[0][0]= 3000
y1[1][0]= 3500
y1[2][0]= 4000
y1[3][0]= 4500
y1[4][0]= 5000
y1= datatable(x, y1, n)

value2= calculate_value(value, x, y1, 5)
print("Velocity at:" , value, "is", round(value2, 4))
abs_rel= abs((value2- calculate_value(value, x, y1, 4))/value2)* 100
print("Absolute Error:" , abs_rel)

#graph

j1 = [1203, 1245, value1, 1378, 1315, 1475]
x1= [19, 22, 25, 26, 28, 30]
plt.plot(x1, j1)
plt.scatter(x1, j1)

z1= [3000, 3500, value2, 4000, 4500, 5000]

plt.plot(x1, z1)
plt.scatter(x1, z1)

'''c=Symbol( 'x')
f= calculate_value(c, x, y, n)* calculate_value(c, x, y, n)
f_prime= f.diff(c)'''

