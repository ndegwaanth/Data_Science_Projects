library(ggplot2)

hours <- c(4, 9, 10, 14, 4, 7, 12, 22, 1, 17)
scores <- c(31, 58, 65, 73, 37, 44, 60, 91, 21, 84)

real <- data.frame(hours, scores)
print(real)
data <- data.frame(hours= c(3, 9.5, 12, 5, 6, 18, 16, 2, 8, 13))

model <- lm(scores ~ hours)
model_predict <- predict(model)
print(model_predict)
predicted_value <- predict(model, data)

print(predicted_value)

new_data = data.frame(
  scores=scores,
  hours=hours,
  model_predicted_value=model_predict,
  new_Data=data,
  predicted_value=predicted_value
)

print(new_data)

ggplot(new_data, aes(sample = scores)) +
  stat_qq() +
  stat_qq_line(color='blue') +
  ggtitle('QQ plot for new data')