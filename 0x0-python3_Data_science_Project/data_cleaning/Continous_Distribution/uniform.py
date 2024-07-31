# Package	Syntax
# NumPy	    np.random.uniform(alpha, beta)
# SciPy	    scipy.stats.uniform(alpha, beta)
import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

# Step 1: Define the parameters
a = 0  # Lower bound
b = 1  # Upper bound

# Step 2: Create a uniform random variable
rv = uniform(loc=a, scale=b-a)

# Step 3: Generate random samples
samples = rv.rvs(size=1000)

# Step 4: Compute the probability density function (PDF) for first few values
x = np.linspace(a, b, 100)  # Values for which to compute the PDF
pdf_values = rv.pdf(x)

# Step 5: Compute the cumulative distribution function (CDF) for first few values
cdf_values = rv.cdf(x)

print(f"PDF values: {pdf_values}")
print(f"CDF values: {cdf_values}")

# Optional: Plot the PDF and CDF
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# PDF plot
ax[0].plot(x, pdf_values)
ax[0].set_title('Uniform Distribution PDF')
ax[0].set_xlabel('Value')
ax[0].set_ylabel('Probability Density')

# CDF plot
ax[1].plot(x, cdf_values)
ax[1].set_title('Uniform Distribution CDF')
ax[1].set_xlabel('Value')
ax[1].set_ylabel('Cumulative Probability')

plt.tight_layout()
plt.show()

# Optional: Plot the samples to visualize the uniform distribution
plt.hist(samples, bins=30, edgecolor='black', density=True)
plt.title('Uniform Distribution (a=0, b=1)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()