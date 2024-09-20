# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pwq2yyUzqmeXYKO0GtAi_cY171L56VsE

Pandas tutorial
"""

import pandas as pd

#from sklearn.datasets import load_boston
#boston=load_boston
#boston_df=pd.DataFrame(boston.data,columns=boston.featurename)
#by a csv file
boston_df=pd.read_csv('/content/BostonHousing.csv')

type(boston_df)

boston_df.head()

boston_df.tail()

boston_df.shape

diabetes_df=pd.read_csv('/content/diabetes.csv')

diabetes_df.head()

diabetes_df.shape

#to read excel
#pd.read_excel('')

"""to export df to csv"""

boston_df.to_csv('boston.csv')

diabetes_df.to_excel('diabetes.xlsx')

"""df with random values"""

import numpy as np

#random_df=pd.DataFrame(np.random.rand(rows,columns))
random_df=pd.DataFrame(np.random.rand(20,10))

random_df.head()

"""inspecting a df"""

#no of rows n columns
boston_df.shape

#first 5 rows
boston_df.head()

#last 5 rows
boston_df.tail()

#information about the dataframe
boston_df.info()

#number of missing values
boston_df.isnull().sum()

diabetes_df.head()

#count the values based on labels
diabetes_df.value_counts('Age')

#group the values based on the mean
diabetes_df.groupby('Outcome').mean()

"""statistical measures"""

#count number of values
boston_df.count()

#columnwise mean values
boston_df.mean()

#std deviation
boston_df.std()

#min value
boston_df.min()

#max values
boston_df.max()

#all stats in one go
boston_df.describe()

"""manipulating a dataframe"""

#adding a column
#boston_df['Price']=boston_dataset.target

boston_df.head()

#removing a row
boston_df.drop(index=1,axis=0)
#for column removal axis=1

#to drop a column
boston_df.drop(columns = 'zn',axis=1)

#locate a row using index
boston_df.iloc[2]

#locate a column
print(boston_df.iloc[:,2])

"""Correlation: positive n negative(direct and indirect variation)"""

diabetes_df.corr()
