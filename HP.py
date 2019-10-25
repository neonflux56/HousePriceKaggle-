
import numpy as np
import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns


#####################################################################################
# FETCH DATA

data = pd.read_csv("train.csv",encoding = 'utf-8')

Ytrain = data['SalePrice']
Xtrain = data.drop("SalePrice", axis=1)
Xtest = pd.read_csv("test.csv",encoding = 'utf-8')

#####################################################################################
# VISUALISE

#separate the integer and str values in train

N = range(0, 80 , 1)
dataheader = list(data.columns.values)

intcols = []
strcols = []
for i in N:
    if type(Xtrain.iloc[0][i]) == np.int64:
        intcols.append(dataheader[i])
    else:
        strcols.append(dataheader[i])

#Plot the integer feature graphs wrt salary price

fig1 = plt.figure()
fig1.subplots_adjust(hspace=0.4, wspace=0.4)
for i,val in enumerate(intcols[:20]):
    ax = fig1.add_subplot(4, 5, i+1)
    ax.scatter(Xtrain[val],Ytrain)
    plt.ylabel("Sale Price")
    plt.xlabel(val)

fig2 = plt.figure()
fig2.subplots_adjust(hspace=0.4, wspace=0.4)
for i,val in enumerate(intcols[20:]):
    ax = fig2.add_subplot(4, 4, i+1)
    ax.scatter(Xtrain[val],Ytrain)
    plt.ylabel("Sale Price")
    plt.xlabel(val)

#Plot the graph for categorical features

#
#   #sns.set(style="ticks", color_codes=True)
#   fig3 = plt.figure()
#   fig3.subplots_adjust(hspace=0.4, wspace=0.4)
#   for i,val in enumerate(strcols[:16]):
#       ax = fig3.add_subplot(4, 4, i+1)
#       ax.boxplot(list(Ytrain), str(list(Xtrain[val])), patch_artist = True )
#   #  #   g = sns.catplot(x=val, y="SalePrice", data=data,height=2.5, aspect=.8)
#