# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:56:18 2021

@author: USER
Md. Shahrukh Islam 

"""
import math
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
#from tabulate import tabulate
K=0.05
pt=3.00

iterations=[]
error=[]
roots=[]


savedLowerBound=-0.1
savedUpperBound=0.1
expectedError=0.5
savedRoot=0.6; 

def function(x): 
    
    return ((x/(1-x))*math.sqrt(6/(2+x)))-0.05

def graph():
    fig, ax=plt.subplots()
    #x=np.linspace(-2,  2, 5000)
    x=np.arange(-0.5, 0.9, 0.01)
    anotherFunction=np.vectorize(function)
    y=anotherFunction(x)
    #y=function(x)
    plt.plot(x,y)
    plt.show()



savedLowerBound=-0.5
savedUpperBound=0.5
expectedError=0.5


def bisect( LowerBound, UpperBound, Error, count): 
    global savedRoot, savedLowerBound, savedUpperBound
    global iterations, error, roots
    if (count==21):
        return savedRoot
    currentRoot=(UpperBound+LowerBound)/2
    
    if count==1 : 
        thisError='First Iteration'
    
    else :
        if (currentRoot==0) :
            thisError=(abs(currentRoot-savedRoot)/(currentRoot+.0001))*100
        else:   
            thisError=(abs(currentRoot-savedRoot)/currentRoot)*100
        
    #if count ==2: 
        #print(" jfjfjff  ")
        #print(currentRoot, " ", savedRoot)
    #print("Iteration is ", count)
    #print("Error is ", thisError, "% ")
    
    iterations.append(count)
    roots.append(currentRoot)
    error.append(thisError)
    
    
    if (count>1 and thisError<=Error):
        #count >1 as only error possible in 2nd count
        #got very low error 
        return currentRoot 
    
    
        
    if(function(currentRoot)*function(LowerBound)<0): 

        savedUpperBound=currentRoot 
        savedRoot=currentRoot
        #print("iteration is ", count, "and here between L and Mid")
        
    else :
        savedLowerBound=currentRoot
        savedRoot=currentRoot 
    
    

    return bisect(savedLowerBound, savedUpperBound, expectedError, count+1)

def createTable():
     global iterations, error, roots
     i=np.array(iterations)
     e=np.array(error)
     r=np.array(roots)
     i=np.reshape(i,(-1,1))
     e=np.reshape(e,(-1,1))
     r=np.reshape(r,(-1,1))
     
     tv=np.concatenate((i,e,r), axis=1)
     data=pd.DataFrame(tv, columns=["iterations", "error", "root"])
     print(data)
     
     
    
graph()



print(bisect(savedLowerBound, savedUpperBound, expectedError, 1))
createTable()


    



