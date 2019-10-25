
import numpy as np
import pandas as pd
import matplotlib as plt

data = pd.read_csv("train.csv",encoding = 'utf-8')

Ytrain = data['SalePrice']
Xtrain = data.drop("SalePrice", axis=1)

Xtest = pd.read_csv("test.csv",encoding = 'utf-8')



