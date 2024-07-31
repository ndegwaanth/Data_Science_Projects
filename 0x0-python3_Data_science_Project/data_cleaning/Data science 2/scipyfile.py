import numpy
import  pandas
import  scipy.stats
import  matplotlib.pyplot as plt

fig, ax = plt.subplots()
mich = pandas.read_csv("https://risk-engineering.org/static/data/michelson-speed-light.csv")
mich.rename(columns={"velocity of light in air (km/s)": "speed"}, inplace=True)
print(mich.head())

plt.xlabel('Measured speed (km.s)')
plt.ylabel("Measurements")
plt.title("Michelson speed of light measurement")
ax.hist(mich.speed, alpha=.9)

# speed mean
print(f"The mean of the speed of light is : {mich['speed'].mean()}")
plt.show()