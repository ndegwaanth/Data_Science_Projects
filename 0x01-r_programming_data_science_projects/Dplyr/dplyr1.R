library(tidyverse)
library(ggplot2)
  
data("airquality")
  
head(airquality)
  
ggplot(data = airquality, aes(x=Ozone)) + geom_histogram()

# convert wide data (airquality) to long data formart

wide_long <- pivot_longer(
  data = airquality,
  cols = c(Ozone, Solar.R, Wind, Temp),
  names_to = "environmental_factors",
  values_to = "measurement"
)

ggplot(data=wide_long, aes(x=environmental_factors, y=measurement)) + geom_col()

long_wide <- pivot_wider(
  data = wide_long,
  names_from = environmental_factors,
  values_from = measurement
)

# Tidyr functions - unite(), separate()
df <- data.frame(
     first_name = c("Anthony", "David", "Alice", "Willy"),
     last_name = c("Ndegwa", "Wachira", "Gathoni", "Thumbi"),
     height_metre = c(2, 1.75, 1.5, 2.3),
     weight = c(70, 65, 90, 100)
)
df_unite <- unite(
  data = df,
  col = full_name,
  c(first_name, last_name),
  sep = " ",
  remove = TRUE
)

df_2 <- data.frame(
  full_name = c("Anthony Ndegwa", "David Wachira ", "Alice Gathoni", "Willy Thumbi"),
  height_metre = c(2, 1.75, 1.5, 2.3),
  weight = c(70, 65, 90, 100)
)
df_2
mean(df_2$height_metre, na.rm = TRUE)
separate(
  data = df_2,
  col = full_name,
  into = c("first_name", "last_name"),
  sep = " ",
  remove = FALSE
) 