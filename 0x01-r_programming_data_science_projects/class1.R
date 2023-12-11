current.sumAdd = 0
class(current.sumAdd)
mode(current.sumAdd)
for (m in 1:100)
{
  print (m)
  current.sumAdd = current.sumAdd + m
  print(current.sumAdd)
}
hist(x,breaks=c(­10,­5,­2,0,2,5,10),freq=F)