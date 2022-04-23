import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FixedLocator, ScalarFormatter
import math
sns.set_theme(style="ticks")

datadir = '/content/drive/My Drive/Colab Notebooks/autosleep_data/'
fname = 'AutoSleep-20201118-to-20201215.csv'
print([datadir + fname])
df_data = pd.read_csv('/content/drive/My Drive/Colab Notebooks/autosleep_data/AutoSleep-20201118-to-20201215.csv') 

datadir = '/Users/warrenm/Downloads/'
fname = 'AutoSleep-20220326-to-20220422.csv'
print([datadir + fname])
df_data = pd.read_csv('/Users/warrenm/Downloads/AutoSleep-20220326-to-20220422.csv') 

# This cannot be the most efficient way to do this

hrAsleep = df_data['asleep'].astype(str).str[0:2] # separates hours converts to miutes
minAsleep = df_data['asleep'].astype(str).str[3:5]
hrAsleep = pd.to_numeric(hrAsleep)*60
minAsleep = pd.to_numeric(minAsleep)
df_data['asleep'] = minAsleep + hrAsleep
totAwake = minAsleep + hrAsleep

hrAwakeBed = df_data['inBed'].astype(str).str[0:2] # separates hours converts to miutes
minAwakeBed = df_data['inBed'].astype(str).str[3:5]
hrAwakeBed = pd.to_numeric(hrAwakeBed)*60
minAwakeBed = pd.to_numeric(minAwakeBed)
totBed = minAwakeBed + hrAwakeBed

# Making the axes not awful

boundBed = int(math.ceil(pd.Series([max(totBed)]) / 100.0)) * 100 # maximum number of minutes in bed, rounded up to the nearest 100 and divided by 100
maxBed = round(boundBed/60 + 0.5) # maximum number of hours in bed rounded up to the nearest whole number, also used for hex size and bin size
hoursNums = np.linspace(0,maxBed,maxBed+1) # actual values used for the axes
hourLocs = np.linspace(0,maxBed,maxBed+1)*60

hexSize=dict(gridsize=maxBed)
sns.jointplot(x=totBed, y=totAwake, kind="hex", joint_kws=hexSize, marginal_kws=dict(bins=maxBed))
plt.xticks(hourLocs,hoursNums)
plt.xlabel('Time in Bed')
plt.yticks(hourLocs,hoursNums) # time asleep will never be > than time in bed unless you fall out
plt.ylabel('Time Asleep')

