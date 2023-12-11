# This code is used to calculate a linear equation 
# 4x + 2y +2z = 6
# x + 4y -z = 10
# 5x + y - 5z = 7
#  it solve the above system of linear equation

matrix_eqn <- matrix(c(4, 2, 2, 1, 4, -1, 5, 1, -5), nrow= 3, ncol = 3, byrow = TRUE)
print(eqn)
output <- matrix(c(6, 10, 7), ncol = 1, nrow = 3, byrow = TRUE)
print(output)

my_final_results <- solve(matrix_eqn, output)
variable_assignment <- c(x = my_final_results[1], y = my_final_results[2], z = my_final_results[3])
print(variable_assignment)

#this command is used to plot the above
library(ggplot2)
library(dplyr)
assignment_df <- data.frame(variable = names(variable_assignment), value = variable_assignment)

# Create a bar plot
ggplot(assignment_df, aes(x = variable, y = value)) +
  geom_bar(stat = "identity", fill = "blue") +
  labs(title = "Variable Assignments", x = "Variable", y = "Value") +
  theme_minimal()
