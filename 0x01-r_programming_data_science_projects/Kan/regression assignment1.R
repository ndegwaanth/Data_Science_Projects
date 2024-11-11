# Load necessary library for reading Excel files
library(readxl)

# Set the working directory for R to correspond with the directory for MVGraded.xlsx
setwd("Documents/university/sem_doc_4.1/Regression Analysis/")

# Load the data from the Excel file
my_scores <- read_excel("MVGraded.xlsx")

# Output the first few rows of the data for confirmation
head(my_scores)

# Fitting a simple linear model
my_model <- lm(ses_mean ~ ses, data = my_scores)

# Display the summary of the model
summary(my_model)

# Get coefficients for the fitted regression line
coefficients <- coef(my_model)
intercept <- coefficients[1]
slope <- coefficients[2]

# Write the fitted regression line
fitted_line <- paste("ses_mean =", round(intercept, 6), "+", round(slope, 6), "* ses")
print(fitted_line)

# Interpretation of the results
cat("\nInterpretation of Results:\n")
cat("1. The intercept is approximately", round(intercept, 6), 
    ", i.e when ses is 0, the expected value of ses_mean is approximately", 
    round(intercept, 6), ".\n") #the round" key word rounds off the results to the nearest 6dp
cat("2. The slope is approximately", round(slope, 6), 
    ", indicating that the rate of change in one-unitin ses is directly proprtional to ses_mean", 
    round(slope, 6), ".\n")
cat("3. The multiple R-squared value is approximately", 
    round(summary(my_model)$r.squared, 4), 
    ", indicating that about", round(summary(my_model)$r.squared * 100, 2), 
    "% of the variability in ses_mean can be explained by the variability in ses.\n")
cat("4.  with p-values less than 0.05,this indicates that the values(ses and ses_mean) are statiscticall significant indicating \n")

#plotting the fitted model
plot(my_scores$ses, my_scores$ses_mean,main = "A scatter Plot with simple Fitted Regression Line",xlab = "SES (x)",ylab = "SES Mean (y)",pch = 19,col = "red",cex = 0.5)

# Adding the fitted regression line to the scatter plot
abline(my_model, color = "blue", lwd = 2)