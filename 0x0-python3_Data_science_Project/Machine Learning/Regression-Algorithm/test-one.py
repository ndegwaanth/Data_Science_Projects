import pandas as pd
from sklearn.model_selection import  train_test_split


url = "https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv"

# Reading the data
dh = pd.read_csv(url)

# Separating logS with the rest of the data in this format
# y = f(x) where y == logS and f(x) == the data under it
y = dh['logS']

# removing the logS in the main dataset dh in order to form this y = f(x)
x = dh.drop('logS', axis=1)

# separating the data to train and on that we are going to test
x_train, x_test, y_train ,y_test = train_test_split(x, y, test_size=0.2, random_state=100 )
print(y_test)