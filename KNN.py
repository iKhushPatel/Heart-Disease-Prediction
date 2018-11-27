# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:47:11 2018

@author: iKhushPatel
"""

import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from matplotlib import pyplot as plt

df = pd.read_csv("D:\\Semester 7\\ML Lab\\Project\\MLProject\\Heart\\Dataset\\KNN.csv")
y = df.HeartProblem

x_train, x_test, y_train, y_test = train_test_split(df, y, test_size=0.97)
print (x_train.shape, y_train.shape)
print (x_test.shape, y_test.shape)


model1 = KNeighborsClassifier()
model1.fit(x_train,y_train)
pred1=model1.predict(x_test)


from sklearn.metrics import confusion_matrix
#print(confusion_matrix(y_test, pred1))

#print("Pred is ", pred1)

#print(model1.score(x_test,y_test))

from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(y_test, pred1)
print("Mean Absolute Error is : ",1-val_mae)
