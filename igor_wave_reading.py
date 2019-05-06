import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

exp_data=pd.read_csv("dupEPSC.txt")

plt.plot(exp_data['dupEPSC'])
plt.show()

print(exp_data['dupEPSC'])