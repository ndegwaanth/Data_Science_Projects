m <- c(64, 55, 34, 76, 80)
lab <- c("Kenya", "Usa", "Tanzania", "Ugand", "Ethiopia")
percent <- round((100 * m/sum(m)), 1)
pie(m, labels = percent, radius = 1,main = "Country resource distribution", col = rainbow(length(m)))
legend("bottomleft", c("Kenya", "Usa", "Tanzania", "Ugand", "Ethiopia"), cex = 0.4, fill = rainbow(length(m)))

library(plotrix)
pie3D(m, labels = lab, explode = 0.5,main = "A 3D pie is beign drawn")

Clients = c("kamau", "John", "Justus", "Kenney", "Anthony", "Kelvin", "wambui", "johnson", "Alexandra", "Moses")
balance = seq(1000, 1900, 100)
balance
mdata = data.frame(Clients, balance)
barplot(balance, names.arg = Clients, xlab = "Clients", ylab = "Account Balance", col = "blue", border = "red")