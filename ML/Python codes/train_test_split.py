# -*- coding: utf-8 -*-
"""Train test split.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QvnS0CHdryRDU8_4utMYDXrtj9-Vk0AO

Train data :- 80-90%  
test data :- 10-20%
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

diabetes = pd.read_csv('/content/diabetes.csv')

diabetes.head()

diabetes['Outcome'].value_counts()

"""1 --> diabetic  
0 --> non diabetic
"""

diabetes.groupby('Outcome').mean()

"""we will break it in 2  
i.e one dataset with feature names and one with outcome
"""

#seperating the data labels
X= diabetes.drop(columns='Outcome',axis=1)
Y = diabetes['Outcome']

print(X)

print(Y)

"""Splitting into training and test"""

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

print(X_train.shape,X_test.shape,X.shape)
