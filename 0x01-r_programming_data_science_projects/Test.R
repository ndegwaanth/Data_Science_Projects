# Creating data frame
sales_data <- data.frame(
  Year = c(2001, 2002, 2003, 2004, 2005, 2006, 
           2007, 2008, 2009, 2010, 2011, 2012),
  Sales = c(6.5, 6.6, 7, 7.1, 4.5, 5.5, 
            13, 12.7, 9.7, 10.4, 6.0, 15.0)
)

# Ploting time series
plot(sales_data$Year, sales_data$Sales, type = "o", col = "blue",
     xlab = "Year", ylab = "Sales", main = "Sales Time Series with Linear Trend")

# Fiting a linear trend
linear_model <- lm(Sales ~ Year, data = sales_data)
abline(linear_model, col = "red", lwd = 2)

# Printing the linear model summary
summary(linear_model)
