# -*- coding: utf-8 -*-
"""Numerical Dataset Pre-Processing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IZEi7aFEUEQkXt_zFccXvrY7m3I7S0n5
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

"""Data collection and preprocessing"""

diabetes=pd.read_csv('diabetes.csv')

diabetes.head()

diabetes.shape

diabetes.describe()

#split it into feature and target
X=diabetes.drop(columns='Outcome',axis=1)
Y=diabetes['Outcome']

print(Y)

#standardising the data
scaler=StandardScaler()
std_data=scaler.fit_transform(X)

std_data.std()

x= std_data

y=Y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)

print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)
