# Package	Syntax
# NumPy	    np.random.poisson(lam)
# SciPy	    scipy.stats.poisson(lam)
# The Poisson distribution is a discrete probability distribution that expresses the probability of
# a given number of events occurring in a fixed interval of time or space, given a constant mean rate of occurrence.
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Step 1: Define the parameter
lambda_ = 3  # Average rate of occurrence

# Step 2: Create a Poisson random variable
rv = poisson(mu=lambda_)

# Step 3: Generate random samples
samples = rv.rvs(size=1000)

# Step 4: Compute the probability mass function (PMF) for first few values
x = np.arange(0, 15)  # Values for which to compute the PMF
pmf_values = rv.pmf(x)

# Step 5: Compute the cumulative distribution function (CDF) for first few values
cdf_values = rv.cdf(x)

print(f"PMF values: {pmf_values}")
print(f"CDF values: {cdf_values}")

# Optional: Plot the PMF and CDF
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# PMF plot
ax[0].bar(x, pmf_values, tick_label=x)
ax[0].set_title('Poisson Distribution PMF')
ax[0].set_xlabel('Number of Events')
ax[0].set_ylabel('Probability')

# CDF plot
ax[1].plot(x, cdf_values, marker='o')
ax[1].set_title('Poisson Distribution CDF')
ax[1].set_xlabel('Number of Events')
ax[1].set_ylabel('Cumulative Probability')

plt.tight_layout()
plt.show()

# Optional: Plot the samples to visualize the Poisson distribution
plt.hist(samples, bins=np.arange(0, max(samples) + 1) - 0.5, edgecolor='black', density=True)
plt.title('Poisson Distribution (lambda=3)')
plt.xlabel('Number of Events')
plt.ylabel('Frequency')
plt.show()