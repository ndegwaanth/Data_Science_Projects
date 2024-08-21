import pandas as pd
import numpy as np

print("The weather-weka data : df")
df = pd.read_csv('data/weather-weka.csv')
print(df)
dh = pd.read_csv('data/weather-nominal-weka.csv')
print('The stock_price data: dh')
print(dh)
dp = pd.read_csv('../Data_science_visualization/stock_price.csv')
print("Stock price data")
print(dp)

newmerg = pd.concat([df, dh, dp])
print("concatenated all the data sets")
print(newmerg)


data = pd.merge(df, dh, on='outlook', how='inner')
print(data['humidity_x'])


a = list(df[['temperature','humidity']].agg(np.mean))
print(a)