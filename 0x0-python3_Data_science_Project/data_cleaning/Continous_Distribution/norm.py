import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Step 1: Define the parameters
mu = 0     # Mean
sigma = 1  # Standard deviation

# Step 2: Create a normal random variable
rv = norm(loc=mu, scale=sigma)

# Step 3: Generate random samples
samples = rv.rvs(size=1000)

# Step 4: Compute the probability density function (PDF) for a range of values
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)  # Values for which to compute the PDF
pdf_values = rv.pdf(x)

# Step 5: Compute the cumulative distribution function (CDF) for a range of values
cdf_values = rv.cdf(x)

print(f"PDF values: {pdf_values}")
print(f"CDF values: {cdf_values}")

# Optional: Plot the PDF and CDF
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# PDF plot
ax[0].plot(x, pdf_values)
ax[0].set_title('Normal Distribution PDF')
ax[0].set_xlabel('Value')
ax[0].set_ylabel('Probability Density')

# CDF plot
ax[1].plot(x, cdf_values)
ax[1].set_title('Normal Distribution CDF')
ax[1].set_xlabel('Value')
ax[1].set_ylabel('Cumulative Probability')

plt.tight_layout()
plt.show()

# Optional: Plot the samples to visualize the normal distribution
plt.hist(samples, bins=30, edgecolor='black', density=True, alpha=0.6, color='b')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, sigma)
plt.title(title)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()