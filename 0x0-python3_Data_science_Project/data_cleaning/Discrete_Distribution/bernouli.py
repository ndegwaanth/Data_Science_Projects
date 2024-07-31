import  bokeh.io

# A Bernoulli trial is an experiment that has two outcomes that can be encoded as success (y=1)
# or failure (y=0). The result y of a Bernoulli trial is Bernoulli distributed.

# Package	Syntax
# NumPy	    np.random.choice([0, 1], p=[1-theta, theta])
# SciPy	    scipy.stats.bernoulli(theta)
# Stan	    bernoulli(theta)

import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

# Step 1: Define the probability of success
p = 0.6

# Step 2: Create a Bernoulli random variable
rv = bernoulli(p)

# Step 3: Generate random samples
samples = rv.rvs(size=1000)

# Step 4: Compute the probability mass function (PMF) for 0 and 1
pmf_0 = rv.pmf(0)
pmf_1 = rv.pmf(1)

# Step 5: Compute the cumulative distribution function (CDF) for 0 and 1
cdf_0 = rv.cdf(0)
cdf_1 = rv.cdf(1)

print(f"PMF at 0: {pmf_0}")
print(f"PMF at 1: {pmf_1}")
print(f"CDF at 0: {cdf_0}")
print(f"CDF at 1: {cdf_1}")

# Optional: Plot the samples to visualize the Bernoulli distribution
plt.hist(samples, bins=2, edgecolor='black')
plt.xticks([0, 1])
plt.title('Bernoulli Distribution (p=0.6)')
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.show()