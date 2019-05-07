# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:29:05 2019

@author: yubin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import time
#import multiprocessing

from igor_wave_reading import read
from MSE import MSE,get_real_X
from simulation import Simulate

def Bound(f_new, x_new, f_old, x_old):
    
    #Non-negative
    #if x_new[0])<=0:
    #    return False
    
    #Within reasonable range
    lowest=np.full((1, 9), 0.5)
    lowest[0]=0
    highest=np.full((1, 9), 1.5)
    highest[0]=2
    
    buffer=x_new-lowest
    if np.size(buffer[buffer<0])!=0:
        return False
    
    buffer=highest-x_new
    if np.size(buffer[buffer<0])!=0:
        return False
    
    return True
        
        #if x_
        #    return "force accept"

def main():
    t=time.process_time()
    data_array=read("dupEPSC.txt")
    #a=4
    #k_20=np.array([1.844,0.018,0.013,0.051])   #k0,k1,k2,k3
    #k_50=np.array([4.309,0.051,0.020,0.066])
    X0=np.array([1,1,1,1,1,1,1,1,1])
    
    minimizer_kwargs={'args':data_array}
    res = optimize.basinhopping(MSE,X0,minimizer_kwargs=minimizer_kwargs,accept_test=Bound)
    print(res)
    print("time used:"+str(time.process_time()-t))
    
    plt.plot(data_array)
    bestX = get_real_X(np.array(res.x))
    a=bestX[0]
    k_20=bestX[1:5]
    k_50=bestX[5:9]
    bestSim = Simulate(a,k_20,k_50)
    
    print("-------------------------------------------")
    print("------------------results------------------")
    print("a:"+str(a))
    print("20Hz K0-3:"+str(k_20))
    print("50Hz K0-3:"+str(k_50))
    print("Best Fitting:")
    plt.plot(bestSim['EPSC'])
    plt.show()

main()
#p=Pool(6)
#p.map(main)

