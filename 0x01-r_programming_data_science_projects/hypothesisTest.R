set.seed(123)
sugar_cookies <- rnorm(30, 9.9, 0.04)
#H_0: Aversge sugar is equal to 10
#H_1: Average sugar is not equal to 10
t.test(sugar_cookies, mu = 10)

b <- c(9,3,5,6,2,4)
c <- order(b)
c
d <- sort.list(b)
d
r <- sort(b)
r
n <- 10
num <- c(1:(n-1))
num
num2 <- c(1:n-1)
num2
s4 <- seq(length=51, from=-5, by=.5)
s4
print(length(s4))
s5 <- rep(s4, times = 5)
s5
mynan <- c(1:3, NA)
mynan
two <- is.na(mynan)
two
fruit <- c(5, 10, 1, 20)
names(fruit) <- c("orange", "banana", "apple", "peach")
lunch <- fruit[c("apple","orange")]
lunch
attr(sugar_cookies, "dim") <- c(1:30)