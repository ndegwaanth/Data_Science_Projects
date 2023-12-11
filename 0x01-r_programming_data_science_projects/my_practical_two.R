#This code is used to implement a function that accept to arguments Y and X1
# Secondly handles fits of the linear regression model Y1 = B0 + B1X1 + e1
# And compute the L for statistics sum(Y1 - B0 - B1X1)/ S^2
# where S^2 is given by sum(Y1 - mean(Y1))/(n-1)
# B0 (Beta-Zero) is the predicted values representing the dependent variable which is Y in this code
# B1 (Beta-One) is the slope coefficient it's the independent variable x1
regression_modelling <- function(Y, X1)
{
  # this code estimate fit the linear regression to the data and estimate the coefficient
  # of the Beta-One and Beta-Zero
  Y1 <- lm(Y ~ X1)
  
  # this program check the difference btw the observed and the predicted values from Y1 model
  program_residual <- residuals(Y1)
  
  # this program calculate the mean of the vector being passed when the function is beign called
  mean_of_Y <- mean(Y)
  
  # This code is used to calculate the sample variance 
  S2 <- sum(program_residual^2) / (length(Y) - 1)
  
  # also the the sample variance can be calculated as 
  #Another_way_to_implement_S2 <- sum((Y - mean(Y))^2) / (n - 1)
  
  # this code is used to calculate the final static code L
  L <- sum((Y - Y1$coef[1] - Y1$coef[2] * X1)^2) / S2
  return (L)
}

#passing the value to the function and initializing th vectors
one <- c(1, 2, 3, 4, 5)
two <- c(6, 7, 8, 9, 10)
regression_modelling(one, two)
#print(my_results)