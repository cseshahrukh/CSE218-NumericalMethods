# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 00:55:41 2021

@author: Md. Shahrukh Islam
BUET
Roll: 1805098
Algorihm : Gauss Elimination Method
"""


import numpy as np
import sys


def GaussElimination (A, B, d):
    n=np.prod(B.shape)
    
    #This is the solution vector 
    #while will be returned 
    x = np.zeros(n)
    
    #this is main gauss to bring multiple zero 
    for i in range(n):
        if A[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        
        for j in range(i+1, n):
            ratio = A[j][i]/A[i][i]
        
            for k in range(n+1):
                if (k<n):
                    A[j][k] = A[j][k] - ratio * A[i][k]
                else:     
                    B[j] = B[j] - ratio * B[i]
            if (d==True):           
                print (A)
                print (B)
                print()

    #ulta vabe calculate korte hobe 
    x[n-1] = B[n-1]/A[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = B[i]
    
        for j in range(i+1,n):
            x[i] = x[i] - A[i][j]*x[j]
    
        x[i] = x[i]/A[i][i]
    return x


#main function
n = int(input())
A=np.zeros((n,n))
B=np.zeros(n)

for i in range(n):
    row=list(map(float,input().split()))
    j=0
    for value in row:
        A[i][j]=float(value)
        j=j+1
        
for i in range(n):
    B[i]=float(input())

x=GaussElimination(A, B, True)

#printing the solution vector 
for i in range(n):
        print('%0.4f' %(x[i]), end = '\t')
