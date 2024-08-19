import pandas as pd
import matplotlib.pyplot as plt
from  matplotlib.colors import ListedColormap

colors = ListedColormap(['#0343df', '#e50000', '#ffff14', '#929591', '#583003'])

df = pd.read_csv('https://anvil.works/blog/img/plotting-in-python/uk-election-results.csv')
print(df)

ax = df.plot.bar(x = 'year', colormap = colors)

plt.show()