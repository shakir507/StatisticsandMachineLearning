import numpy as np
import pandas as pd
import scipy.stats as stats
import os
path='./../../practical-statistics-for-data-scientists/data/'
data=pd.read_csv(os.path.join(path,'state.csv'))

#Evaluating relative crime rates in different states
Poppulation=data['Population']
MurderRate=data['Murder.Rate']
Pop_mean=Poppulation.mean()
Pop_var=Poppulation.var()
MurderRate_mean=MurderRate.mean()
MurderRate_var=MurderRate.var()

Z_score=stats.zscore(MurderRate)
states=[st for st in data['State']]
#Identifying states that perform poorly on murder rate
for i in range(len(data)):
    p_value = stats.norm.sf(abs(Z_score[i])) 
    if(p_value<0.05):
        print(states[i],Pop_mean,MurderRate_mean,Z_score[i],p_value)# these states score poorly on the murder rate