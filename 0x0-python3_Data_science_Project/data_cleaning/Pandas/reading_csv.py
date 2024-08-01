import random

import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/araastat/BIOF085/master/data/mtcars.csv'
data = pd.read_csv(url)
print(data)

# data types
print(data.dtypes)
# data structure
print(data.info())
# shape of the data
print(data.shape)
# summary of each variable
print(data.describe())

"""
data type in pandas are
a) series
b) Dataframe
"""

# series
data_series = pd.Series(np.random.normal(1, 5, 20))
print(data_series)

# Dataframe
rng = np.random.RandomState(25)
data_1 = rng.normal(0, 1, (4,5))
dh = pd.DataFrame(data_1, columns=['first', 'second', 'third', 'fourth', 'fifth'], index=['a', 'b', 'c', 'd'])
print(dh)

# dataframe implementing with the format of a dictionary
df = pd.DataFrame({
    'A': 3.,
    'B': rng.random_sample(5),
    'C': pd.Timestamp('20200512'),
    'D': np.array([np.nan] * 5),
    'E': pd.Categorical(['yes', 'no', 'no', 'yes', 'no']),
    'F': 'NIH'})
print(df)
print(dh.second)

""" 
using loc and iloc for slicing the data 
"""
# using loc
print('using loc in slicing the data ==> dh')
print(dh.loc[:, 'first':'second'])
print('extracting data using the row index')
print(dh.loc['a':'d',:])

# using iloc function
print('using iloc in slicing the data ==> dh')
print(dh.iloc[1:4])
print(dh.iloc[1:3, 1:4])

"""
To extract a single element in the dataframe i can use 
at and iat
"""
# usint iat
print("using iat to extract single element at this position dh[2,3]: {}".format(dh.iat[2,3]))
# using at
print("using at to extract single element at dh[b, 'third']: {}".format(dh.at['b','third']))

# create a new column
dh['sixth'] = [int(x) for x in rng.normal(1, 2, 4)]
print(dh)

# replace function
print(df)
# print(df.replace(df['D'], rng.normal(1, 2, 5)))
print( df.replace(df['D'], -9)) # replace 0 with -9
print(df)

# Categorical data
"""A list of dataframe using list in  a dictionary"""
df2 = pd.DataFrame({'A': list('abcd'), 'B': list('bdca')})

"""converting the df2 data type to catagery using astype"""
df2_cat = df.astype('category')
""" value_counts() count the values that exists in column A and the number of occurrence"""
A_D = df2['A'].value_counts()
"""describe() function is use to show the statistics of A"""
print(A_D)
B = df2_cat['A'].describe()
print(B)
"""reorder_categories is used to reoganize the data"""
# C = df2_cat['A'] = df2_cat.A.cat.reorder_categories(['a','b','c','d'])
# print(C)