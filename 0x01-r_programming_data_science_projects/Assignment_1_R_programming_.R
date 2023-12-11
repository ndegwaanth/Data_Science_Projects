# an R-script to containing function that accepts
# the radius and the height of a cone and calculate
# the area of the cone and the volume of the cone

Area_of_the_cone <- function(radius, height){
  #this calculate the total surface are of the cone
  pi <- 3.142
  length_1 <- radius + height
  TSA <- pi * radius * length_1
  print("The total area of the total surface are is")
  print(TSA)
  
  print(".....................................................................")
  
  #this code calculate the area of the right circular cone 
  add_1 <- length_1
  square <- sqrt(add_1)
  add_2 <- radius + square
  Area <- pi * radius * add_2
  cat("The area of the right circualr cone is: ")
  print(Area)
  
  print("......................................................................")
  
  # this code calculate the volume of the cone 
  volume <- 0.3333 * pi * radius **2 * height
  cat("The volume of the cone is: ")
  print(volume)
  print(".......................................................................")
}
area <- Area_of_the_cone(10, 6)
print(area)

#The second code is used to solve the system of the linear equation
# x  + 4y +z = 6
# 4x - y -z = 2
install.packages("matlib") 
library(matlib)
co_ordinate = matrix(c(1, -2, 2, 7, 4, 1, 4, -1, -1), nrow = 3, ncol = 3, TRUE)
print(co_ordinate)
total <- c(3, 6, 2)
print(total)
showEqn(co_ordinate, total)

#solve the equation using the solve function
results <- c(solve(co_ordinate, total), nrow(3))
print(results)

# plotting the results got on the linear equation
plotEqn(co_ordinate, total)
# 7x

# This program output the square of all the prime number between 20 and 100
arry <- c(20:100)
print(arry)
flag <- FALSE
for (number in arry){
  if ((arry %% number) == 0){
    square_prime <- number ** 2
    print(square_prime)
    flag <- TRUE
  }
}
if (flag){
  print("the number is not prime")
} else {
  print("The numbers are prime") 
}

# Function to check if a number is prime
check_prime <- function(n) {
  if (number <= 1) {
    return(FALSE)
  }
  if (number <= 3) {
    return(TRUE)
  }
  if (number %% 2 == 0 || number %% 3 == 0) {
    return(FALSE)
  }
  
  iterate <- 5
  while (iterate * iterate <= number) {
    if (number %% iterate == 0 || number %% (iterate + 2) == 0) {
      return(FALSE)
    }
    iterate <- iterate + 6
  }
  
  return(TRUE)
}
primes_output <- function() {
  primes <- c()
  for (i in 20:100) {
    if (check_prime(i)) {
      primes <- c(primes, i)
      square_prime <- primes ** 2
    }
  }
  return(square_primes)
}
print(primes_output())