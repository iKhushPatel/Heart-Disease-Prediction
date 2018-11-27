# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd

df = pd.read_csv("Dataset.csv");
df.dropna()
columnlist = df.columns
uniquevalues = []

for i in columnlist:
    print(i)
    uniquevalues.append(df[i].unique())

dictval = dict(zip(columnlist, uniquevalues))
print(dictval)

keys = list(dictval.keys())
#print(keys)
#print(dictval.values())

inputlist = []
for key, value in dictval.items():
    valstring = str(value)
    string = "Enter " + key + " " + valstring + " :: ";
    inputtext = input(string)
    inputlist.append(inputtext.lower())
inputlist = inputlist[0:len(inputlist) - 1]
index = 0
predictyes = []
predictno = []

prob = df.groupby(keys[-1]).HeartProblem.count()

probyes = prob.yes
probno = prob.no


for i in range(len(keys) -1):
    predictyes.append(sum(np.logical_and(df[keys[i]] == inputlist[i], df[keys[len(keys) - 1]] == 'yes')))
    predictno.append(sum(np.logical_and(df[keys[i]] == inputlist[i], df[keys[len(keys) - 1]] == 'no')))
    
finalprobyes = 1
for i in predictyes:
    finalprobyes = finalprobyes * (i/probyes)
    
finalprobno = 1
for i in predictno:
    finalprobno = finalprobno * (i/probno)

if(finalprobyes > finalprobno):
    print("Last few years... May god saves you... Heart Diseases Found")
else:
    print("Hurray... You Are totally safe... Enjoy Your Life... Heart Diseases Not Found")
