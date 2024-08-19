# import pandas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ignore this code entirely
plt.rcParams['figure.figsize'] = [8, 6]
plt.rcParams['figure.dpi'] = 100


# results url
url1 = 'https://docs.google.com/spreadsheets/d/e/'
url2 = '2PACX-1vRkK73xD192AdP0jZe6ac9cnVPSeqqbYZmSPnhY2hnY8ANROAOCS'
url3 = 'tRFdvjwFoapv3j2rzMtZ91KXPFm/pub?output=csv'

# create data frame from url
df = pd.read_csv(url1 + url2 + url3)
print(df)
# assign original headers to list
survey_questions = df.columns.to_list()

# replace with column names easier to work with
renamelist = ['Timestamp', 'musicartist', 'height', 'city', '30min', 'travel',
              'likepizza', 'deepdish', 'sport', 'spell', 'hangout', 'talk',
              'year', 'quote', 'area-code', 'home-pet', 'superpower', 'shoes-have']
df.columns = renamelist

# using .isna() with a series
not_available = df.loc[:, '30min'].isna().head(10)
print('values that are not available in the dataset')
print(not_available)

# using .notna() with a series
not_missing = df.loc[:, '30min'].notna().head(10)
print('values that are not missing in the dataset')
print(not_missing)

# drop the rows that have mmissing values
print('drop row missing value')
df.dropna(axis='index')

# drop the colums that have missing values
print('drop column missing value')
drop_column_missing_value = df.dropna(axis='columns')



column_name = '30min'

count_missing_value = df.isna().sum()
count_available_value = df.notna().sum()

print('\n - The amount of data missing is {}'.format(count_missing_value))
print('\n - The number of value that are not null is {}'.format(count_available_value))

# print(df.isna().head(10))
# print(df.info())
# print(df.describe())

# counts missing values by summing booleans (True = 1, False = 0)
missing_count = df.isna().sum()
print("Missing valuse by summing")
print(missing_count)

# counts not missing values using .count()
not_missing_count1 = df.count()
print('not missing count1')
print(not_missing_count1)

# counts not missing values using .notna().sum() (True = 1, False = 0)
# same result as previous
not_missing_count2 = df.notna().sum()
print(not_missing_count2.info())

# count rows in series (including missing)
total_count = len(df.loc[:, column_name])

# print summary
print(f'{df}\n-missing values: {missing_count}'
      f'\n-not missing values: {not_missing_count1}'
      f'\n-total count: {total_count}')

# calculate the mean replacement value by first dropping missing values
mean_replacement_value = df.loc[:, 'likepizza'].dropna().mean()

# use the calculated mean to replace the missing values (assigned to a new series)
df.loc[:, 'likepizza_w_replace'] = df.loc[:, 'likepizza'].fillna(mean_replacement_value)

# check the result
result = df.loc[:, ['likepizza', 'likepizza_w_replace']].info()

print(result)