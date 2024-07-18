import random

import numpy as np

observations = ['Real', 'Fake']
flowers = ['Iris setosa', 'Iris virginica', 'Iris versicolor']

with open('DB_data.dat', 'w') as f:
    for _ in range(20):
        observation = random.choice(observations)
        flower = str(random.choice(flowers))
        sepal_width = random.random()
        sepal_length = random.random()
        petal_width = random.random()
        petal_length = random.random()

        str((f.write('{} {} {:.3f} {:.3f} {:.3f} {:.3f}\n'.format(
            observation,
            flower,
            sepal_length,
            sepal_width,
            petal_length,
            petal_width))))

data = np.loadtxt('DB_data.dat')
print(data)