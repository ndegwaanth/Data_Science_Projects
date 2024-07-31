# Package	Syntax
# NumPy	    np.random.binomial(N, theta)
# SciPy	    scipy.stats.binom(N, theta)
# The binomial distribution is a discrete probability distribution that models the number of successes in a
# fixed number of independent Bernoulli trials, each with the same probability of success
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

# Step 1: Define the parameters
n = 10  # Number of trials
p = 0.5  # Probability of success on each trial

# Step 2: Create a binomial random variable
rv = binom(n, p)

# Step 3: Generate random samples
samples = rv.rvs(size=1000)

# Step 4: Compute the probability mass function (PMF) for first few values
x = np.arange(0, n + 1)  # Values for which to compute the PMF
pmf_values = rv.pmf(x)

# Step 5: Compute the cumulative distribution function (CDF) for first few values
cdf_values = rv.cdf(x)

print(f"PMF values: {pmf_values}")
print(f"CDF values: {cdf_values}")

# Optional: Plot the PMF and CDF
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# PMF plot
ax[0].bar(x, pmf_values, tick_label=x)
ax[0].set_title('Binomial Distribution PMF')
ax[0].set_xlabel('Number of Successes')
ax[0].set_ylabel('Probability')

# CDF plot
ax[1].plot(x, cdf_values, marker='o')
ax[1].set_title('Binomial Distribution CDF')
ax[1].set_xlabel('Number of Successes')
ax[1].set_ylabel('Cumulative Probability')

plt.tight_layout()
plt.show()

# Optional: Plot the samples to visualize the binomial distribution
plt.hist(samples, bins=np.arange(0, n + 2) - 0.5, edgecolor='black', density=True)
plt.title('Binomial Distribution (n=10, p=0.5)')
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.show()