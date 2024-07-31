import numpy as np
import  matplotlib.pyplot as plt
import  pandas as pd


data = pd.read_csv("delaney_solubility_with_descriptors.csv")
print(data)

# This are the data columns
# MolLogP    MolWt  NumRotatableBonds  AromaticProportion   logS

fig, ax= plt.subplots()
fig, az = plt.subplots()
width = 0.15

ax.bar(data['MolWt'], data['NumRotatableBonds'], width, label = "NumRotatableBonds", color='#0343df')
ax.bar(data['MolWt'], data['MolLogP'], width, label = "MolLogP", color='#e50000')
ax.bar(data['MolWt'], data['AromaticProportion'], width, label = "AromaticProportion", color='#ffff14')
ax.bar(data['MolWt'], data['logS'], width, label = "logS", color='#929591')
ax.set_ylabel('MolWt')
ax.set_xlabel('NumRotatableBonds')
ax.set_title('NumRotatableBonds')
ax.legend()

data['MolWt'].fillna(0)
data.fillna(0)
print(plt.gca())
print(plt.gcf())

az.scatter(data['MolWt'], data['NumRotatableBonds'], width, label = "NumRotatableBonds", color='#0343df')
az.scatter(data['MolWt'], data['MolLogP'], width, label = "MolLogP", color='#e50000')
az.scatter(data['MolWt'], data['AromaticProportion'], width, label = "AromaticProportion", color='#ffff14')
az.scatter(data['MolWt'], data['logS'], width, label = "logS", color='#929591')

az.set_ylabel('MolWt')
az.set_xlabel('NumRotatableBonds')
az.set_title('NumRotatableBonds')
az.legend()

plt.show()