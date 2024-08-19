import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pandas_data = pd.read_csv('weather-weka.csv')
numpy_data = np.genfromtxt('weather-weka.csv', delimiter=',', skip_header=1, dtype=None)

sns.set_context('paper')
sns.set(rc={'figure.figsize': (8, 6)})
sns.set_style('white', {'font.family':'sans-serif', 'text.color':'1'})
tips = sns.load_dataset("tips")

x = numpy_data.T[0]
y = numpy_data.T[1]

# plt.plot(x=x, y=x, c='o')
print(tips)
# sns.catplot(data=tips, x='total_bill', y='tip')
sns.scatterplot(x="total_bill", y="tip", data=tips)
# pandas_data.plot(x='outlook', y='temperature', kind='hist')
sns.histplot(data=pandas_data, x='outlook', y='temperature')
plt.title('outlook vs temperature')
plt.show()

