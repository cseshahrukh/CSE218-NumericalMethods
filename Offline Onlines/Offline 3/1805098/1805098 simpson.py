# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:23:07 2021

@author: USER
"""


import math
u=2000
m=140000
q=2100
g=9.8


def f(x):
    return  u*math.log(m/(m-q*x), math.e)-g*x


def simpson13(l,r,n):
    h = (r - l) / n
    
    #sum 
    integration = f(l) + f(r)
    
    for i in range(1,n):
        k = l + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    
    integration = integration * h/3
    
    return integration
    

l = 8
r = 30



prevValue=0
currentValue=0
def solve(n):
    global prevValue, currentValue
    for i in range(2, n+1, 2): 
        
        currentValue=simpson13(l, r, i)
        if (i==2):
            error='First Iteration'
        else:
            error=(abs(currentValue-prevValue)/currentValue)*100
        
        print(i,"            ", currentValue,"        ", error)
        prevValue=currentValue
        i=i+1
    



n = int(input("Enter number of sub intervals: "))
solve(2*n)
result = simpson13(l, r, 2*n)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result) )