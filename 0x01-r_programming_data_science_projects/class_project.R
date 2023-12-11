exp_1 <- expression(3*x^2 - 2*x + 4)
results <- D(exp_1, "x")
print(results)

exp_2 <- expression((exp(2*x) + 4*x + 4)/ (exp(x)/ 2 + x))
results_2 <- D(exp_2, "x")
print(results_2)

exp_3 <- expression(cos(2*t))
results_3 <- D(exp_3, "t")
print(results_3)

root_finding <- function(x){
  x^3 - 2*x^2 - 3*x + 3
}
polyroot(c(1, 3, 4))
integrate(root_finding, 0, 10)
optimize(root_finding, c(0, 10))
f -> 
print(my_func)