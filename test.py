# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:28:48 2019

@author: yubin
"""

import numpy as np

X0=np.array([4,1.844,0.018,0.013,0.051,4.309,0.051,0.020,0.066])
X0.reshape(9,1)
m=np.array([1,1,1,1,1,1,1,1,1])
print(np.multiply(X0,m))