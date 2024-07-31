import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# data columns include
# MolLogP MolWt  NumRotatableBonds  AromaticProportion   logS

# fig, vis = plt.subplot(2, 4, 6)
# vis[new_data['MolWt', 'NumRotatableBonds']].plot()

a = np.zeros(5)
print(a.shape)
print(a)
print('Arrange()')
e = np.arange(0,5,10)
p = np.arange(0,10,5)
print(e)
print(p)
print("linspace()")
e = np.linspace(0,10,5)
print(e)

a = np.array([[0, 2, 2, 5, 6],
 [2, 5, 5, 0, 2],
 [1, 3, 8, 9, 4],
 [3, 9, 1, 6, 9]])

print("quiz 1")
print(a[:,-1])
print("quiz 2")
print(a[:,1:2].shape)
print("quiz 3")
print(a[1][2])
print("quiz 4")
print(a[:,1].shape)
print("quiz 5")
print(a[1,2])
print("quiz 6")
print(a[1:2,2:3])

a = np.array([[7, 9, 1, 9, 0],
     [2, 1, 9, 8, 0],
     [0, 9, 3, 9, 3],
     [6, 3, 9, 6, 8]])

print('quiz 1')
print(a[::-1,:])
print('quiz 2')
print(a[:,::-1])
print('quiz 3')
print(a[:,-1:-4:-1])
print('quiz 4')
print(a[-1:-4:-1,:])

a = np.array([[2, 2, 2, 3, 2],
                 [3, 2, 1, 4, 1],
                 [1, 1, 1, 3, 4],
                 [4, 1, 2, 3, 4]])

new_a = np.where(a == 3, 22, a)
print(new_a)
