# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:32:37 2019

@author: yubin
"""

import numpy as np
from sklearn.metrics import mean_squared_error

from simulation import Simulate
from igor_wave_reading import read


#a=4
#k_20=np.array([1.844,0.018,0.013,0.051])   #k0,k1,k2,k3
#k_50=np.array([4.309,0.051,0.020,0.066])

def get_real_X(nX):
    #input normalized X, output real X
    Orig=np.array([4,1.844,0.018,0.013,0.051,4.309,0.051,0.020,0.066])
    Orig.reshape(9,1)
    
    Xreal = np.multiply(Orig,nX)
    
    return Xreal

def MSE(X,data_array):
    #input: X vector, experimental data

    Xreal = get_real_X(X)
    
    a=Xreal[0]
    k_20=Xreal[1:5]
    k_50=Xreal[5:9]
    
    Sim=Simulate(a,k_20,k_50)
    
    return mean_squared_error(data_array,Sim['EPSC'])

def test():
    data_array=read("dupEPSC.txt")
    X0=np.array([1,1,1,1,1,1,1,1,1])
    print(MSE(X0,data_array))