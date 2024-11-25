library(tseries)

X11(width = 5, height = 8)
par(mfrow=c(2,2))


# Simulate a non-stationary time series
set.seed(123)
non_stationary_data <- cumsum(rnorm(100))

# Plot the non-stationary series
plot(non_stationary_data, type = "l", main = "Non-Stationary Time Series", ylab = "Value", xlab = "Time")

# Perform ADF Test
adf_test <- adf.test(non_stationary_data)
print(adf_test)

# Differencing to make it stationary
stationary_data <- diff(non_stationary_data)

# Plot the stationary series
plot(stationary_data, type = "l", main = "Stationary Time Series (After Differencing)", ylab = "Value", xlab = "Time")

# Perform ADF Test on stationary data
adf_test_stationary <- adf.test(stationary_data)
print(adf_test_stationary)
