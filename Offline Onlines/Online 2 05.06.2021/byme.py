# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:10:52 2021

@author: USER
"""
#Done 
# Newton divided difference formula 
  
# Finding the product term 
def proterm(i, value, x): 
    pro = 1; 
    for j in range(i): 
        pro = pro * (value - x[j]); 
    return pro; 
  
# Function for calculating 
# divided difference table 
def dividedDiffTable(x, y, n):
  
    for i in range(1, n): 
        for j in range(n - i): 
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
  
# Function for applying Newton's 
# divided difference formula 
def applyFormula(value, x, y, n): 
  
    sum = y[0][0]; 
  
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]); 
      
    return sum; 
  

  
# Driver Code
  
# number of inputs given 
n = 5; 
y = [[0 for i in range(10)] 
        for j in range(10)]; 

z=  [[0 for i in range(10)] 
        for j in range(10)]; 
x = [ 19,22,26,28,30 ]; 
  
# y[][] is used for divided difference 
# table where y[][0] is used for input 
y[0][0]= 1203
y[1][0]= 1245
y[2][0]= 1378
y[3][0]= 1315
y[4][0]= 1475

 
  
# calculating divided difference table 
y=dividedDiffTable(x, y, n); 
  

  
# value to be interpolated 
value = 25; 
  
# printing the value 
print("\nValue at", value, "is",
        round(applyFormula(value, x, y, n), 2))
  
