# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 23:44:38 2021

@author: USER
"""

import numpy as np
import pandas as pd
#Toki Vaia
def createtable(x,y):
    
  
    n=y.shape[0]
    ara=np.zeros((n,n))
    for i in range(n):
        ara[i,0]=y[i]
    
    i=0
    for col in range(1,n):
        for row in range(n-col):
            ara[row,col]=(ara[row+1,col-1]-ara[row,col-1])/(x[col+i]-x[i])
            i=i+1
        i=0
    
    
    return ara
def takepoints(x,y,val,n):
  xs=[]
  ys=[]
  tempx=x
  tempy=y
  for i in range(n):
    idx=(np.abs(tempx-val)).argmin()
    xs.append(tempx[idx])
    ys.append(tempy[idx])
    tempx=np.delete(tempx,idx)
    tempy=np.delete(tempy,idx)
    
  tempx=np.array(xs)
  tempy=np.array(ys)

  return tempx,tempy

def plot(x,y):
    
    fig, ax = plt.subplots(figsize=(10,10))
    plt.rc('xtick', labelsize=15) 
    plt.rc('ytick', labelsize=15) 
    
    ax.plot(x,y,linewidth=2)

    ax.grid(True, which='both')    
    ax.axhline(y=0, color='green',linewidth=3)
    ax.axvline(x=0, color='green',linewidth=3)
    
    plt.show()
    



def compute(ara,x,val):
    res=0
    n=x.shape[0]
    
    for i in range(n):
        temp=1
        for j in range(i):
            temp=temp*(val-x[j])
        
        
        res=res+(temp*ara[0,i])
       
        
        
    return res  


def main(): 
    
    
    
    x=np.array([0,5,9,12,19,22,26,28,30,33,40])
    yv=np.array([1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,60000])
    ym=np.array([1011,1255,1347,1101,1203,1245,1378,1315,1475,1547,1689])
    value=25
    d=5 # 4th order 
    x_,ym_=takepoints(x,ym,value,d)
    x_,yv_=takepoints(x,yv,value,d)
    ara_m=createtable(x_,ym_)
    ara_v=createtable(x_,yv_)
    aram=ara_m
    arav=ara_v
    
    #d=derivative(ara_m,ara_v,x_)
    res_m=compute(ara_m,x_,value)
    res_v=compute(ara_v,x_,value)
    print("Computed mass at t=25s using 4th order is:" + str(res_m))
    print("Computed velocity at t=25s using 4th order is:" + str(res_v))
    
    print("---------Calculating Relative error:------- ")
    
    d=2 # 1st order 
    x_,ym_=takepoints(x,ym,value,d)
    x_,yv_=takepoints(x,yv,value,d)
    ara_m=createtable(x_,ym_)
    ara_v=createtable(x_,yv_)
    res_m_2=compute(ara_m,x_,value)
    res_v_2=compute(ara_v,x_,value)
        
    d=3 # 2nd order 
    x_,ym_=takepoints(x,ym,value,d)
    x_,yv_=takepoints(x,yv,value,d)
    ara_m=createtable(x_,ym_)
    ara_v=createtable(x_,yv_)
    res_m_3=compute(ara_m,x_,value)
    res_v_3=compute(ara_v,x_,value)
    
    d=4 # 3rd order 
    x_,ym_=takepoints(x,ym,value,d)
    x_,yv_=takepoints(x,yv,value,d)
    ara_m=createtable(x_,ym_)
    ara_v=createtable(x_,yv_)
    res_m_4=compute(ara_m,x_,value)
    res_v_4=compute(ara_v,x_,value)
    
    
    error1v=(res_v_3-res_v_2)/res_v_3
    error1m=(res_m_3-res_m_2)/res_m_3
    
    error2v=(res_v_4-res_v_3)/res_v_4
    error2m=(res_m_4-res_m_3)/res_m_4
    
    error3v=(res_v-res_v_4)/res_v
    error3m=(res_m-res_m_4)/res_m
    
    
    
    
    error1m=np.abs(error1m)
    error1v=np.abs(error1v)
    error2m=np.abs(error2m)
    error2v=np.abs(error2v)
    error3m=np.abs(error3m)
    error3v=np.abs(error3v)
    
    mass=['-',error1m,error2m,error3m]
    val=['-',error1v,error2v,error3v]
    
    
    
    

    df=pd.DataFrame(list(zip(mass,val)),columns=['Mass Error','Velocity Error'])
    print(df) 
    
    print("Velocity vs time:")
    plt.plot(x,yv)
    plt.plot(25,res_v,'ro')
    plt.show()
    
    print("Mass vs time")
    plt.plot(x,ym)
    plt.plot(25,res_m,'ro')
    plt.show()
    
    
    from sympy import *
    x = Symbol('x')
    f1 = aram[0,0] + aram[0,1]*(x-x_[0]) +aram[0,2]*(x-x_[1])*(x-x_[0])  +aram[0,3]*(x-x_[2])*(x-x_[1])*(x-x_[0]) + aram[0,3]*(x-x_[3])*(x-x_[2]) * (x-x_[1]) * (x-x_[0])
    f2 = arav[0,0] + arav[0,1]*(x-x_[0]) +arav[0,2]*(x-x_[1])*(x-x_[0])  +arav[0,3]*(x-x_[2])*(x-x_[1])*(x-x_[0]) + arav[0,3]*(x-x_[3])*(x-x_[2])*(x-x_[1])*(x-x_[0])
    f=f1*f2
    f_prime = f.diff(x)
    f_prime = lambdify(x, f_prime)
    print(f_prime(25))
    
    
       
    
   
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from sympy import *
    import numpy as np
    import math
    import pandas as pd
    main()
        
    













