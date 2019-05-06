# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:02:43 2019

@author: yubin
"""

import numpy as np
from math import exp

def Calc_K(ki,kf,t,a):	     #t is the time after the change
    tau=0.75*a				 #0.75s is the tau for Ca consentration
    if(t<tau*100):
        return kf+(ki-kf)*exp(-t/tau)
    else:
        return kf

def Simulate(a,k_20,k_50):
    # simulate the first 5 seconds when changing from 50Hz to 20Hz
        
    # Initialization
    print("k_50",k_50)
    RP=300000
    inv_k_20=[1/x for x in k_20]
    Sim={
           'RRP':np.zeros(251), #RRP_init
           'RPP':np.zeros(251),
           'PEP':np.zeros(251),
           'SP':np.zeros(251),
           'time':np.zeros(251),
           }
    
    Sim['RRP'][0]=RP*inv_k_20[0]/sum(inv_k_20)
    Sim['RPP'][0]=RP*inv_k_20[1]/sum(inv_k_20)
    Sim['PEP'][0]=RP*inv_k_20[2]/sum(inv_k_20)
    Sim['SP'][0] =RP*inv_k_20[3]/sum(inv_k_20)
    
    # Simulation
    dt=1/50
    k=np.copy(k_50)
    for i in range(250):
        k[1]=Calc_K(k_20[1],k_50[1],Sim['time'][i],a)
        Sim['RRP'][i+1]=Sim['RRP'][i]+dt*(-k[0]*Sim['RRP'][i]+k[1]*Sim['RPP'][i])
        Sim['RPP'][i+1]=Sim['RPP'][i]+dt*(-k[1]*Sim['RPP'][i]+k[2]*Sim['PEP'][i])
        Sim['PEP'][i+1]=Sim['PEP'][i]+dt*(-k[2]*Sim['PEP'][i]+k[3]*Sim['SP'][i] )
        Sim['SP'][i+1] =Sim['SP'][i]+ dt*(-k[3]*Sim['SP'][i]+ k[0]*Sim['RRP'][i])
        Sim['time'][i+1]=Sim['time'][i]+dt
    return Sim



a=4
k_20=np.array([1.844,0.018,0.013,0.051])   #k0,k1,k2,k3
k_50=np.array([4.309,0.051,0.020,0.066])

Sim=Simulate(a,k_20,k_50)

import matplotlib.pyplot as plt

plt.plot(Sim['RRP'])
plt.show()

