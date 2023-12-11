A <- matrix(c(1,2,3,4), 2,2, byrow = TRUE)
B <- matrix(c(5,6,7,8),2,2, byrow = TRUE)
prod <- A %*% B

days <- c("Mon", "Tues", "Wed", "Thur","Fri", "Sat", "Sun")
for (m in 1:7){
  print("m:". days[m])
  m = m + 1
}
