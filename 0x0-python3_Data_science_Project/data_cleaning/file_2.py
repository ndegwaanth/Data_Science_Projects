import numpy as np
import  pandas as pd
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn import metrics

# pivot Table
"""
Reshape data based on column values
does not support data aggregation
foo bar baz zoo
________________
0   one  A   X
1   one  B   Y
2   one  C   Z      ===>     bar    A   B   C           ===> df.pivot(index='foo'.
3   two  A   Q               foo                                       columns='bar',
4   two  B   W               ___________________                       values='baz')
5   two  C   T                one   1   2   3
                              two   4   5   6
"""

# .pivot_table
"""
Create a spreadsheet-style pivot table
support data aggregation
"""

new_data = pd.read_csv('delaney_solubility_with_descriptors.csv')
print(new_data)