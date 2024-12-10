# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:05:48 2024

@author: HUAWEI
"""

1 + 1

import numpy as np
import os

data_path = 'C:\Users\HUAWEI\Desktop\Programming_for_Data_Science\repo\hudm5001\warm_ups\Coffee'
file_name = 'Coffee_TRAIN.txt'
full_path = os.path.join(data_path, file_name)

data = np.loadtxt(full_path)

#10/01/2024
import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

?pd.read_csv

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data",header=None)
#add a hearder to the data

df.head()
df.tail()
