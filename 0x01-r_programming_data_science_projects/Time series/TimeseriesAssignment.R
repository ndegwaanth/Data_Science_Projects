library(dplyr)
library(ggplot2)

# Load the CSV file
final_anormal_data_set <- read.csv("/home/anthony/Datasets/final-anormal-data-set.csv")
final_normal_data_set <- read.csv("/home/anthony/Datasets/final-normal-data-set.csv")
#View(final_anormal_data_set)
#View(final_normal_data_set)

getwd()
print("The column names of the final_anormal_data_set")
colnames(final_anormal_data_set)

print("The column names of the final_anormal_data_set")
colnames(final_normal_data_set)

plot(final_anormal_data_set$cpu_total, final_anormal_data_set$cpu_user, 
     main = "CPU User vs CPU Total", 
     xlab = "CPU Total", 
     ylab = "CPU User")

# Fiting a linear model
model <- lm(cpu_user ~ cpu_total, data = final_anormal_data_set)

#Adding the regression line
abline(model, col = "red")

# the original dataset timestamp
timestamp <- final_anormal_data_set$timestamp
timestamp2 <- final_normal_data_set$timestamp

# converting character format to date format
#ts_timestamps <- as.POSIXct(final_anormal_data_set$timestamp, format="%Y-%m-%d %H:%M:%S")
#ts_timestamps2 <- as.POSIXct(final_normal_data_set$timestamp, format="%Y-%m-%d %H:%M:%S")

final_anormal_data_set$timestamp <- ts_timestamps
final_normal_data_set$timestamp <- ts_timestamps2

# Checking for missing values
sum(is.na(final_anormal_data_set$cpu_total))
sum(is.na(final_anormal_data_set$timestamp))


# Removing rows with missing cpu_total
final_anormal_data_set <- final_anormal_data_set %>% 
  filter(!is.na(cpu_total))

# Checking for missing values
sum(is.na(final_anormal_data_set$cpu_total))
sum(is.na(final_anormal_data_set$timestamp))


final_anormal_data_set <- final_anormal_data_set %>%
  mutate(hour = format(as.POSIXct(timestamp), "%Y-%m-%d %H")) %>%
  group_by(hour) %>%
  summarise(cpu_total = mean(cpu_total, na.rm = TRUE))

ggplot(final_anormal_data_set, aes(x = hour, y = cpu_total)) +
  geom_bar(stat = "identity", fill = 'blue') +
  labs(title = "Average CPU Total by Hour During Cryptojacking",
       x = 'Hour',
       y = "Average CPU Total") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Filling NA values in cpu_total with 0 using base R
final_normal_data_set$cpu_total[is.na(final_normal_data_set$cpu_total)] <- 0

# Creating a time series object
cpu_ts <- ts(final_normal_data_set$cpu_total, frequency = 12)
# Decomposing the time series
decomposed_ts <- decompose(cpu_ts)
# Ploting the decomposed components
plot(decomposed_ts)