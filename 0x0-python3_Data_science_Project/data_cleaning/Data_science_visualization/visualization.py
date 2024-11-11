import pandas as pd
import numpy as np
import seaborn as sns

urlg = 'https://raw.githubusercontent.com/'
repo = 'bsheese/CSDS125ExampleData/master/'
fnme1 = 'data_corgis_state_crime.csv'
df = pd.read_csv(urlg + repo + fnme1)
test = df.Population.sample(20).corr(df["Rates.Violent.All"])
print(test)