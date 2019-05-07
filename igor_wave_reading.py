import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def read(filename):
    exp_data=pd.read_csv(filename)
    data_array=np.array(exp_data)
    return data_array

