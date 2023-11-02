# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:36:19 2021

@author: Md. Shahrukh Islam
"""
import math

u=2000
m=140000
q=2100
g=9.8

def y( x ):
    return  u*math.log(m/(m-q*x), math.e)-g*x
     
def trapezoidal (a, b, n):
     
    h = (b - a) / n
     
    s = (y(a) + y(b))
 
    #middle term
    i = 1
    while i < n:
        s += 2 * y(a + i * h)
        i += 1
         
    # h/2 actually (b-a)/2n.
    # Multiplying h/2 with sum
    return ((h / 2) * s)
 

l = 8
r = 30
 
n = 0
prevValue=0
currentValue=0
def solve(n):
    global prevValue, currentValue
    for i in range(1, n+1): 
        
        currentValue=trapezoidal(l, r, i)
        if (i==1):
            error='First Iteration'
        else:
            error=(abs(currentValue-prevValue)/currentValue)*100
        
        print(i,"            ", currentValue,"        ", error)
        prevValue=currentValue
    
n = int(input("Enter an Integer: "))
solve(n)
result = trapezoidal(l, r, n)
print("Integration result by Trapezoidal method is: %0.6f" % (result) )
