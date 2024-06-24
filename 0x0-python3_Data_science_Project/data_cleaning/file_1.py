import numpy as np
import  pandas as pd
from pandas import RangeIndex
#
# # creating an array with numpy
# data = np.array([[1,4], [2,5],[3,6]])
#
# #creating a dataframe with pandas
# # index is used to define the the rows
# # columns used to name the columns
# dh = pd.DataFrame(data, index=['row1', 'row2', 'row3'], columns=['col1', 'col2'])
#
# # lists of data
# states = ['Kenya', 'Uganda', 'Tanzania', 'Somalia']
# population = [50000000, 40000000, 30000000, 20000000]
#
# # sorting the lists within a dictionary
# dict_states = {'States':states, 'Population':population}
#
# # creating the dataframe
# df_population = pd.DataFrame(dict_states)
#
# # reading the csv file
data_2 = pd.read_csv('NBA_2021.csv')
#
# #showing the first 5 rows in a dataframe
# data_2.head()
#
# # showing the last 5 rows in a dataframe
# data_2.tail()
#
# # showing the last n rows in a dataframe
# data_2.head(20)
# #showing the first 20 rows starting from the last
# data_2.tail(704)
#
# #getting the shape attribute
# # the first one is the number f rows and the second is the number of column
# data_2.shape
#
# # display the n rows
# data_3 = pd.set_option('display.max_rows', 700)
#
# # getting the index attribute
# data_2.index
#
# #getting the column attribute
# data_2.columns
#
# #getting the data type of each colums
# data_2.dtypes
# type(data_2)
#
# #showing the info of the dataframe
# data_2.info()
#
# # describing the basic statistics of the dataframe
# data_2.describe()
#
# # obtaining the highest index of the dataframe
# max(data_2.index)
#
# # obtaining the lowest index of the dataframe
# min(data_2.index)
#
 # #roundin the data in 2 decimal place
# round(data_2, 2)
#
# print(data_2)
#
# # select a column with []
# print(data_2['Player'])
#
# # check the data type of a column
# print(type(data_2['Player']))
#
# # selecting a column with '.'
# print(data_2.Player)

# selecting 2 column s using [[]]
# print(data_2[['Player', 'FGA']])

# check out the data types of the selection
print(data_2.columns)
print(type(data_2[['Player', 'FGA']]))

# select 2 or more columns using [[]]
print(data_2[['DRB', 'TRB', 'AST', 'STL', 'BLK']])
data_4 = data_2[['DRB', 'TRB', 'AST', 'STL', 'BLK']]

# adding new colum to dataframe
# data_4['language'] = 'kikuyu'

# create an array of 704 elements
language_s = np.arange(0, 705)
print(len(language_s))

data_4['language'] = language_s
print(data_4)

# create random integers numbers between 1 and 100
rand = np.random.randint(1, 100, size=705)
len(rand)
print(min(rand))
print(max(rand))

data_4['language'] = rand
print(data_4)

# creating random float numbers between 1 and 100
rand_2 = np.random.uniform(1, 100, size=705)
print(rand_2)
data_4['language'] = rand_2
print(data_4)

# Math operations
# select a column and calculate total sum
total = data_4['AST'].sum()
print("The sum of AST is {}".format(total))

# count, mean, std, max and min
count = data_4['AST'].count()
print("The total of AST is {}".format(count))
mean = data_4['AST'].mean()
print("The mean of AST is {}".format(mean))
std = data_4['AST'].std()
print("The standard deviation of AST is {}".format(std))
max = data_4['AST'].max()
print("The maximum of AST is {}".format(max))
min = data_4['AST'].min()
print("The minimum of AST is {}".format(min))
# or
print(data_4.describe())

# calculating the sum in a row
sum = data_4['DRB'] + data_4['TRB'] + data_4['AST'] + data_4['STL']
print(sum)

# calculate the average
avg = (data_4['DRB'] + data_4['TRB'] + data_4['AST'] + data_4['STL'])/3
print("The average of the 3 data are {}".format(avg))
data_4['average'] = avg
data_4['sum'] = sum
print(data_4)

# counting the categorical data
data_4['gender'] = 'male'
print(data_4)
count_cat = data_4['gender'].value_counts()
print(count_cat)

# return the relative frequency (devive all the value by the sume of valuea) = percentage
rel_frq = data_2['Tm'].value_counts(normalize=True).round(2)
print(rel_frq)

# counting the Tm element by element
Tm = data_2['Tm'].value_counts(normalize=True).round(2)
print(Tm)

# sort by one column
sort = data_2.sort_values(by='Tm')
print(sort)

# sort descending by one column
sort_by_col = data_4.sort_values('AST', ascending=False)
print(sort_by_col)

# sort descending by multiple column
sort_by_mul_col = data_4.sort_values(['AST', 'STL'], ascending=False)
print(sort_by_mul_col)

# sort descending by multiple columns and update dataframe
sort_by_mul_col_upd = data_4.sort_values(['AST', 'STL'], ascending=False, inplace=True)
print(data_4)

# sort descending with a key function
data_4.sort_values('gender', ascending=True, key=lambda col:col.str.lower())
print(data_4)