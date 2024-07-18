import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Step 1: Load the Dataset
url = "https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv"
data = pd.read_csv(url)

# Step 2: Explore the Data
print(data.head())

# Step 3: Split the Data into Training and Testing Sets
X = data[['MolLogP', 'MolWt', 'NumRotatableBonds', 'AromaticProportion']]
y = data['logS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make Predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Step 6: Evaluate the Model
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)
mae = mean_absolute_error(y_test, y_test_pred)

print(f'Training MSE: {train_mse:.4f}')
print(f'Testing MSE: {test_mse:.4f}')
print(f'Training RMSE: {train_rmse:.4f}')
print(f'Testing RMSE: {test_rmse:.4f}')
print(f'Training R^2: {train_r2:.4f}')
print(f'Testing R^2: {test_r2:.4f}')
print(f'Testing MAE: {mae:.4f}')

# Step 7: Visualize the Results
plt.figure(figsize=(14, 6))

# Plotting predictions vs true values
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, color='blue', alpha=0.6, label='Training data')
plt.scatter(y_test, y_test_pred, color='green', alpha=0.6, label='Testing data')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='--', label='Ideal fit')
plt.xlabel('True values')
plt.ylabel('Predicted values')
plt.title('Predicted vs True values')
plt.legend()

# Residual plot
plt.subplot(1, 2, 2)
plt.scatter(y_test_pred, y_test_pred - y_test, color='green', alpha=0.6, label='Testing data residuals')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.legend()

plt.tight_layout()
plt.show()