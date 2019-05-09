# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:05:48 2019

@author: yubin

Project Note:
    
    2019/5/6 
    [Talk with Liang Xiao]
    Gradient Descent requires a derivable mathematical cost function
    My model is numeral not analytical
    Can only use “随机算法”
    Best current option is Genetic Algorithm(GA)
    Alternative is “模拟退火”
    
"""

import time

import random as rd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,exp

def cost_function(X):
    #should input variable vector X, output cost y
    
    return X**2

def new_X(oldX,T):
    #should input old variable vector X, and temperature T
    #should output a random new variable vector
    
    w2=0.05
    dX = rd.uniform(-w2*sqrt(T),w2*sqrt(T))
    newX = oldX + dX
    return newX

def annealing_simulation(Xi,Ti,Tm,a):
    #should input initial variable vector, initial temperature, minimum temperature,
    #   cooling rate
    
    X=np.copy(Xi)
    y=cost_function(Xi)
    T=Ti
    
    bestX = np.copy(X)
    besty = y
    
    ylist=[y]
    
    while(T>Tm):
        newX = new_X(X,T)
        newy = cost_function(newX)
        
        if(newy<y):
            X=np.copy(newX)
            y=newy
            if(y<besty):
                besty=y
                bestX=np.copy(X)
        elif(rd.random()<exp((y-newy)/T)):
            X=np.copy(newX)
            y=newy
        ylist.append(y)
        T=T*a
    return bestX,besty,ylist

test_flag=0
if(test_flag==0):
    #my own annealing function
    t=time.process_time()
    
    bestX,besty,ylist = annealing_simulation(1,1,0.00001,0.95)
    
    print("time:")
    print(time.process_time()-t)
    
    
    plt.plot(ylist)
    print(bestX)
    print(besty)



#scipy annealing function
from scipy import optimize

t=time.process_time()

#minimizer_kwargs={'args':1}
res = optimize.basinhopping(cost_function,1)

print("time:")
print(time.process_time()-t)
print(res)







