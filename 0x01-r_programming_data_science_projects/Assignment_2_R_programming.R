#this code generate the sequence defined by 2an - a(n-1) + 6n where
#a1(first_term)= 1 and a2(second_term)= 8
#and including the 1000th term

first_term <- 1
second_term <- 8
third_term <- 3
list_of_element <- c(first_term, second_term)
for (sequence_of_element in third_term:1000){
  next_term <- 2 * list_of_element[sequence_of_element - 1] - list_of_element[sequence_of_element - 2] + 6 *(sequence_of_element - 1)
  list_of_element <- c(list_of_element, next_term)
}
print(list_of_element)

print("................................................................")

# this code form a 2x2 matrix following this condition
# a is the sum of the first 200 elements
# b is the sum of the first 500 elements
# c is the sum of the is the sum of the last 300 elements
# d is the sum of the middle 400 elements
a <- sum(list_of_element[1:200])
b <- sum(list_of_element[201:700])
c <- sum(list_of_element[701:1000])
d <- sum(list_of_element[501:900])
matrix_formation <- matrix(c(a, b, c, d), nrow = 2, ncol = 2, TRUE)
print(matrix_formation)

print("................................................................")

# This code print the inverse of the matrix formed above
inverse_matrix <- solve(matrix_formation)
print(inverse_matrix)
