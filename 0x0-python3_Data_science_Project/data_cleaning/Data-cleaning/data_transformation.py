import pandas as pd
import numpy as np


df = pd.read_csv('data/weather-weka.csv')
print(df)

try:
    mean = df.groupby('outlook').get_group('rainy').agg(np.mean)
    temp = df.groupby('play')['temperature'].mean()
    nthgroup = df.groupby('temperature').ngroups
    hum = df.groupby('outlook').humidity.mean()
    many = df.groupby(['outlook', 'windy']).temperature.std().reset_index()
    col = df.groupby('outlook').nth(1)
    agg = df.groupby('outlook').humidity.agg(np.mean)
    lot = df.groupby('outlook').temperature.agg([np.count_nonzero, np.mean, np.std])
    stat1 = df.groupby('outlook').describe()
    serve = df.groupby('outlook').filter(lambda d: d['temperature'].max() >= 80 and d['humidity'].max() >= 80)
    print('The temperature above 80 degree')
    print(serve)
    # print('temperature statistics \n')
    # print(lot)
    # print('statistics \n')
    # print(stat1)
    # print(agg)
    # print(nthcol)
    # print(many)
    # print(hum)
    # print(nthgroup)
    # print(temp)
    # print(mean)
except Exception as e:
    print(e)

def z_score(values):
    m = np.mean(values)
    s = np.std(values)
    zscore = (values - m)/s
    return zscore


zscore = df.groupby('outlook').transform(z_score)
zscore2 = df.transform(z_score)
# df['play'].astype(np.number)
print('Z score that is grouped by outlook')
print(zscore)
print('Zscore that is based on the whole dataset')
print(zscore2)

df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(df)

print(df.loc['k':'n'])
# print(df.iloc[1]['a'])
print(df.iloc[:2][['outlook', 'temperature']])
