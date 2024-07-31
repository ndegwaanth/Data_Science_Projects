import numpy as np

# Function to perform bootstrap resampling
def bootstrap_resample(data, num_samples, statistic):
    n = len(data)
    bootstrap_samples = np.random.choice(data, (num_samples, n), replace=True)
    bootstrap_statistics = np.array([statistic(sample) for sample in bootstrap_samples])
    return bootstrap_statistics

# Example data
data = np.array([10, 12, 13, 15, 17, 19, 21, 23, 24, 26])

# Number of bootstrap samples
num_samples = 1000

# Statistic of interest (e.g., mean)
statistic = np.mean

# Perform bootstrap resampling
bootstrap_means = bootstrap_resample(data, num_samples, statistic)

# Estimate the standard error of the mean
bootstrap_se = np.std(bootstrap_means)

# Construct a 95% confidence interval for the mean
confidence_interval = np.percentile(bootstrap_means, [2.5, 97.5])

print(f"Bootstrap Mean Estimate: {np.mean(bootstrap_means)}")
print(f"Bootstrap Standard Error: {bootstrap_se}")
print(f"95% Confidence Interval: {confidence_interval}")