# Package	Syntax
# NumPy	    np.random.chisquare(nu)
# SciPy	    scipy.stats.chi2(nu)
import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

# Step 1: Define the parameters
k = 4  # Degrees of freedom

# Step 2: Create a chi-square random variable
rv = chi2(df=k)

# Step 3: Generate random samples
samples = rv.rvs(size=1000)

# Step 4: Compute the probability density function (PDF) for a range of values
x = np.linspace(0, 15, 1000)  # Values for which to compute the PDF
pdf_values = rv.pdf(x)

# Step 5: Compute the cumulative distribution function (CDF) for a range of values
cdf_values = rv.cdf(x)

print(f"PDF values: {pdf_values}")
print(f"CDF values: {cdf_values}")

# Optional: Plot the PDF and CDF
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# PDF plot
ax[0].plot(x, pdf_values)
ax[0].set_title('Chi-Square Distribution PDF')
ax[0].set_xlabel('Value')
ax[0].set_ylabel('Probability Density')

# CDF plot
ax[1].plot(x, cdf_values)
ax[1].set_title('Chi-Square Distribution CDF')
ax[1].set_xlabel('Value')
ax[1].set_ylabel('Cumulative Probability')

plt.tight_layout()
plt.show()

# Optional: Plot the samples to visualize the chi-square distribution
plt.hist(samples, bins=30, edgecolor='black', density=True, alpha=0.6, color='b')
plt.title(f'Chi-Square Distribution (df={k})')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()