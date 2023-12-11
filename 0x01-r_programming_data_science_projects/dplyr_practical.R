mat <- matrix(c(1,3,4,5,6, 7, 8, 9, 2,1), nrow = 5, ncol = 2, byrow = TRUE)
dim(mat)
mat
diag(1,4,0.5)
A <- matrix(1:9, 3, 3, byrow = TRUE)
diag(A)
my <- eigen(A)
my
my$values
my$vectors