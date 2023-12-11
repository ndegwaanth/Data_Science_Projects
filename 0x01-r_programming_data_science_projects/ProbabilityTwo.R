set.seed(123)
choice <- 4
n_sim <- 20
n_trial <- 20
prob <- 0.6
scenario <- matrix(rbinom(n_sim * choice, n_trial, prob), nrow = n_trial, ncol = choice)
scenario
probability_at_least_11 <- 1 - sum(pbinom(11, n_trial, prob))
print(probability_at_least_11)

correct_guesses <- rowSums(scenario)
correct_guesses