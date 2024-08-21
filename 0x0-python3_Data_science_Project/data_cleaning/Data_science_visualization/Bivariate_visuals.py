import pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt
import seaborn as sns


dh = pd.read_csv('stock_price.csv')
df = pd.read_csv('stocks_toy.csv')
dk = pd.read_csv('iris.csv')
dh.pivot(index='Date', columns='Close')

print(dk)
fig, ax = plt.subplots()
# dk.plot(ax=ax)
# sns.lineplot(data=dk, color='red')
# sns.relplot(y='Sepal.Length', x='Species', data=dk, kind='line', color='cyan')
#
# f = sns.FacetGrid(dk, hue='Species', height=9)
# f.map(plt.scatter, 'Sepal.Length', 'Petal.Length').add_legend()

# g = sns.FacetGrid(dk, col = 'Species', hue = 'Species', height = 5)
# g.map(plt.scatter, 'Sepal.Width', 'Sepal.Length').add_legend()
#
# m = sns.FacetGrid(dk, col='Species', hue='Species', height=6)
# m.map(sns.scatterplot, 'Petal.Length', 'Petal.Width').add_legend()
#
# dk.plot(kind='scatter', x='Species', y='Sepal.Length')
#
# sns.pairplot(data=dk)
# print(plt.style.available)
# plt.style.use('Solarize_Light2')
# n = sns.PairGrid(dk, diag_sharey=False)
# n.map_diag(sns.kdeplot, lw=2)
# n.map_lower(sns.kdeplot, color='yellow')
# n.map_upper(sns.scatterplot)

sns.boxplot(dk, x=dk['Species'], y=dk['Sepal.Length'])

plt.grid()
plt.show()

