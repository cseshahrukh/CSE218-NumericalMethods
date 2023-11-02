# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:05:21 2021

@author: USER
"""

import math
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd


a=0.001129241
b=0.0002341077
c=0.00000008775468
t=19+273.15
savedRoot=0.6 

def function(r): 
    global a, b, c
    save=math.log(r,math.e)
    return a+b*save+c*save*save*save -1/t





savedLowerBound=10000
savedUpperBound=20000
expectedError=0.5

def graph():
    fig, ax=plt.subplots()
    #x=np.linspace(-2,  2, 5000)
    x=np.arange(10000, 20000, 1)
    anotherFunction=np.vectorize(function)
    y=anotherFunction(x)
    #y=function(x)
    plt.plot(x,y)
    plt.show()
    

def bisect( LowerBound, UpperBound, Error, count): 
    global savedRoot, savedLowerBound, savedUpperBound
    global iterations, error, roots
    
    
    while(count<=100):
        
        currentRoot=(UpperBound+LowerBound)/2
        if count==1 : 
            thisError='First Iteration'
    
        else :
            if (currentRoot==0) :
                thisError=(abs(currentRoot-savedRoot)/(currentRoot+.0001))*1000
            else:   
                    thisError=(abs(currentRoot-savedRoot)/currentRoot)*100
        

    
        if (count>1 and thisError<=Error): 
            #print(currentRoot)
            return currentRoot 
        
        if(function(currentRoot)*function(LowerBound)<0): 
            UpperBound=currentRoot 
            savedRoot=currentRoot
        
        else :
            LowerBound=currentRoot
            savedRoot=currentRoot 
        
        count=count+1
        
    #print(savedRoot)
    return savedRoot


graph()
print(bisect(savedLowerBound, savedUpperBound, expectedError, 1))
#print(function(2000000000000))
#print(function(0.0006))
#print(function(13213.1396))