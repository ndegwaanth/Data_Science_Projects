# Sample data for years and sales
years <- 2010:2021
sales <- c(120, 130, 135, 140, 150, 160, 165, 170, 175, 180, 185, 190)

# Step 1: Split the sales and years data into two halves
n <- length(sales)
half <- floor(n / 2)

# Splitting years and sales into two halves
years_first_half <- years[1:half]
sales_first_half <- sales[1:half]
years_second_half <- years[(half + 1):n]
sales_second_half <- sales[(half + 1):n]

# Step 2: Calculate the average of each half for sales and years
avg_sales_first_half <- mean(sales_first_half)
avg_sales_second_half <- mean(sales_second_half)
avg_years_first_half <- mean(years_first_half)
avg_years_second_half <- mean(years_second_half)

# Step 3: Calculate the slope (m) and intercept (b) for the trend line
slope <- (avg_sales_second_half - avg_sales_first_half) / 
  (avg_years_second_half - avg_years_first_half)
intercept <- avg_sales_first_half - slope * avg_years_first_half

# Generate the trend line for the existing years
trend_line <- slope * years + intercept

# Step 4: Predict future sales
future_years <- 2022:2025  # Extend years as needed
future_trend <- slope * future_years + intercept  # Predicted sales for future years

# Combine existing and predicted data for plotting
all_years <- c(years, future_years)
all_sales <- c(sales, future_trend)

# Plotting the sales data with the trend line and future predictions
plot(all_years, all_sales, type = "o", col = "blue", xlab = "Year", ylab = "Sales",
     main = "Semi-Average Method with Future Predictions")
lines(years, trend_line, type = "o", col = "red", lwd = 2)
lines(future_years, future_trend, type = "o", col = "green", lwd = 2)
legend("topleft", legend = c("Actual Sales", "Trend Line", "Future Predictions"), 
       col = c("blue", "red", "green"), lty = 1, pch = 1, cex = 0.8)

# Display predicted values for future years
data.frame(Year = future_years, Predicted_Sales = future_trend)

