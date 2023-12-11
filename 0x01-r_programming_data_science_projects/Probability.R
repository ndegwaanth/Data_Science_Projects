set.seed(123) # Set seed
#Generate Binomial process
Quiz <- 20
guess_prob <- 0.6
Choices <- 4
n_sim <- 20
scenario <- matrix(rbinom(n_sim, Quiz, guess_prob),
                   nrow = n_sim,ncol = Choices)
scenario
least_11_correct <- apply(scenario, 1, function(x) sum(x >= 11) / Quiz)
prob <- mean(least_11_correct)
prob
quantile_99 <- quantile(apply(scenario, 1, sum), 0.99)
quantile_99

install.packages("xlsx")
