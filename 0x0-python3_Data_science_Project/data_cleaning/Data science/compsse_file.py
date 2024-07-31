import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Prepare the data
data = {
    'new': np.arange(1, 11),
    'new1': np.random.rand(10) * 10
}
data = pd.DataFrame(data)

# Define the plots to be created
plots_to_create = []

# Line plot
if not data['new'].empty and not data['new1'].empty:
    plots_to_create.append('line')

# Scatter plot
if not data['new'].empty and not data['new1'].empty:
    plots_to_create.append('scatter')

# Horizontal bar plot
if not data['new'].empty and not data['new1'].empty:
    plots_to_create.append('barh')

# Histogram
if not data['new1'].empty:
    plots_to_create.append('hist')

# Bar plot
if not data['new'].empty and not data['new1'].empty:
    plots_to_create.append('bar')

# Pie chart
if not data['new'].empty and not data['new1'].empty:
    plots_to_create.append('pie')

# Create subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Flatten the axs array for easier iteration
axs = axs.flatten()

# Track the used axes
used_axes = []

# Create plots based on the conditions
for i, plot_type in enumerate(plots_to_create):
    if plot_type == 'line':
        axs[i].plot(data['new'], data['new1'])
        axs[i].set_title('Line Plot')
        used_axes.append(axs[i])
    elif plot_type == 'scatter':
        axs[i].scatter(data['new'], data['new1'])
        axs[i].set_title('Scatter Plot')
        used_axes.append(axs[i])
    elif plot_type == 'barh':
        axs[i].barh(data['new'], data['new1'])
        axs[i].set_title('Horizontal Bar Plot')
        used_axes.append(axs[i])
    elif plot_type == 'hist':
        axs[i].hist(data['new1'], bins=5)
        axs[i].set_title('Histogram')
        used_axes.append(axs[i])
    elif plot_type == 'bar':
        axs[i].bar(data['new'], data['new1'])
        axs[i].set_title('Bar Plot')
        used_axes.append(axs[i])
    elif plot_type == 'pie':
        axs[i].pie(data['new1'], labels=data['new'], autopct='%1.1f%%')
        axs[i].set_title('Pie Chart')
        used_axes.append(axs[i])

# Remove unused axes
for ax in axs:
    if ax not in used_axes:
        fig.delaxes(ax)

# Adjust layout
plt.tight_layout()
plt.show()