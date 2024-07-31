# Package	Syntax
# NumPy	    np.random.negative_binomial(alpha, beta/(1+beta))
# SciPy	    scipy.stats.nbinom(alpha, beta/(1+beta))
# Stan	    neg_binomial(alpha, beta)
# The negative binomial distribution is a discrete probability distribution that models the number of trials needed
# to achieve a specified number of successes in a series of independent Bernoulli trials
import numpy as np
from scipy.stats import nbinom
import matplotlib.pyplot as plt

# Step 1: Define the parameters
r = 5  # Number of successes
p = 0.3  # Probability of success on each trial

# Step 2: Create a negative binomial random variable
rv = nbinom(r, p)

# Step 3: Generate random samples
samples = rv.rvs(size=1000)

# Step 4: Compute the probability mass function (PMF) for first few values
x = np.arange(0, 20)  # Values for which to compute the PMF
pmf_values = rv.pmf(x)

# Step 5: Compute the cumulative distribution function (CDF) for first few values
cdf_values = rv.cdf(x)

print(f"PMF values: {pmf_values}")
print(f"CDF values: {cdf_values}")

# Optional: Plot the PMF and CDF
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# PMF plot
ax[0].bar(x, pmf_values, tick_label=x)
ax[0].set_title('Negative Binomial Distribution PMF')
ax[0].set_xlabel('Number of Trials (k)')
ax[0].set_ylabel('Probability')

# CDF plot
ax[1].plot(x, cdf_values, marker='o')
ax[1].set_title('Negative Binomial Distribution CDF')
ax[1].set_xlabel('Number of Trials (k)')
ax[1].set_ylabel('Cumulative Probability')

plt.tight_layout()
plt.show()

# Optional: Plot the samples to visualize the negative binomial distribution
plt.hist(samples, bins=max(samples)-min(samples), edgecolor='black', density=True)
plt.title('Negative Binomial Distribution (r=5, p=0.3)')
plt.xlabel('Number of Trials')
plt.ylabel('Frequency')
plt.show()