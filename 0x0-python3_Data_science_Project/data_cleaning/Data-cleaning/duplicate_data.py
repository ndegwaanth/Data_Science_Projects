# import pandas
import numpy as np
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
# assign original headers to list
survey_questions = df.columns.to_list()

# replace with column names easier to work with
renamelist = ['Timestamp', 'musicartist', 'height', 'city', '30min', 'travel',
              'likepizza', 'deepdish', 'sport', 'spell', 'hangout', 'talk',
              'year', 'quote', 'area-code', 'home-pet', 'superpower', 'shoes-have']
df.columns = renamelist

# missing values
print("missing values in the index")
missing_row = df.iloc[1:17].isna()
mean_na = df.loc[:].isna().mean()
df.loc[:].fillna(mean_na)
missing_row.dropna(axis='index')
pet = df.loc[:, 'home-pet'].isna()
drp_pet = df.loc[:, 'home-pet'].dropna()
df['drop_pet'] = df.loc[:, 'home-pet'].dropna()

print(df['drop_pet'])
# print(df['home-pet'])

print("length of pet with null value {}".format(len(pet)))
print("length of the pet that have being dropped {}".format(len(drp_pet)))

l_before = len(df)
l_after  = len(df.drop_duplicates(subset = df.columns[1:]))

print(f'Dataframe length before drop: {l_before}')
print(f'Dataframe length after drop: {l_after}')

print(df.loc[df.loc[:, 'quote'] == "Dream bigger"])

# check the values of year before using pd.to_numeric()
year_count = df.loc[:, 'year'].value_counts()
print("The count values of the years are")
print(year_count)

# check for entries longer than 4 characters
year_long_than_4chr = df.loc[:, 'year'] \
  .loc[df.loc[:, 'year'].str.len() > 4] \
  .head(15)
print("checking the year with more than 4 characters")
print(year_long_than_4chr)

# assign only first four character to series
print("assign only first four character to series")
year_series = df.loc[:, 'year'].str[:4]
print(year_series.value_counts())

# creating a new series using pd.to_numeric()
print("creating a new series using pd.to_numeric()")
year_series_numeric = pd.to_numeric(year_series, errors = 'coerce')
print(year_series_numeric)

# check the values of year after using pd.to_numeric()
print("check the values of year after using pd.to_numeric()")
print(year_series_numeric.value_counts())

# getting some descriptive stats with the numeric version of year
print("The mean of year_series_numeric is {}".format(year_series_numeric.mean()), "\n",
      "The minimum value if year_series_numeric is {}".format(year_series_numeric.min()), "\n",
      "The maximum value of year_series_numeric is {}".format(year_series_numeric.max()), "\n",
      "The mode of year_series_numeric is {}".format(year_series_numeric.mode()))


# histogram of somewhat cleaned time machine question restricted to 1900-2100
sns.histplot(year_series_numeric \
             .loc[year_series_numeric \
             .isin(range(1900, 2100))])

print(df.columns)