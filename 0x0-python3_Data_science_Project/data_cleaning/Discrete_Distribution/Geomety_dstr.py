# Package	Syntax
# NumPy	    np.random.geometric(theta)
# SciPy	    scipy.stats.geom(theta, loc=-1)
# Stan	    neg_binomial(1, theta/(1-theta))
import numpy as np
from scipy.stats import geom
import matplotlib.pyplot as plt

# Step 1: Define the probability of success
p = 0.3

# Step 2: Create a geometric random variable
rv = geom(p)

# Step 3: Generate random samples
samples = rv.rvs(size=1000)

# Step 4: Compute the probability mass function (PMF) for first few values
x = np.arange(1, 11)  # Values for which to compute the PMF
pmf_values = rv.pmf(x)

# Step 5: Compute the cumulative distribution function (CDF) for first few values
cdf_values = rv.cdf(x)

print(f"PMF values: {pmf_values}")
print(f"CDF values: {cdf_values}")

# Optional: Plot the PMF and CDF
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# PMF plot
ax[0].bar(x, pmf_values, tick_label=x)
ax[0].set_title('Geometric Distribution PMF')
ax[0].set_xlabel('Number of Trials')
ax[0].set_ylabel('Probability')

# CDF plot
ax[1].plot(x, cdf_values, marker='o')
ax[1].set_title('Geometric Distribution CDF')
ax[1].set_xlabel('Number of Trials')
ax[1].set_ylabel('Cumulative Probability')

plt.tight_layout()
plt.show()

# Optional: Plot the samples to visualize the geometric distribution
plt.hist(samples, bins=max(samples), edgecolor='black', density=True)
plt.title('Geometric Distribution (p=0.3)')
plt.xlabel('Number of Trials')
plt.ylabel('Frequency')
plt.show()