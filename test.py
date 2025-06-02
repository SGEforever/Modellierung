import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

c_ozone = pd.Series(data=(1, 0.786, 0.649, 0.482, 0.381), index=(0, 50, 100, 200, 300))
c_no = pd.Series(data=(8.13, 5.07, 2.41, 0.78, 0.36), index=(0, 50, 100, 200, 300))


plt.plot(c_ozone.index, c_ozone.values, label='ozon')
plt.plot(c_no.index, c_no.values, label='no')
plt.plot(c_ozone.index, np.power(c_ozone.values - c_no.values), label="zusammen")
plt.legend()
plt.show()