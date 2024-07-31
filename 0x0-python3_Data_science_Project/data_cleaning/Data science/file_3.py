import  numpy as np
import pandas
import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()

array_A = np.array([[1,2,3], [4,5,6], [0,2,1]])
print(array_A.shape)
print(array_A.size)
print(array_A)

# array_B = array_A.reshape(3,2)
# print(array_B)

# print(array_B[0])
# print(array_B[:,0])
# print(array_B[0,:])

# np.int16
array = np.array([])

array_A = np.array([[1,2,3], [4,5,6], [0,2,1]])
print(array_A)
array_C = np.array([[1], [3], [7]])
print(array_C)
print("sum")
print(array_C + array_A)
print("##############################################")
rng = np.random.normal(0,1,5)
print(rng)

print(np.arange(10))
print(np.array([3,2]))
print("This id array C")
print(array_A)
print("Maximum value in colum {}".format(array_A.argmax(axis=0)))
print("Maximum value in row {}".format(array_A.argmax(axis=1)))
print("Mininum value in colum {}".format(array_A.argmin(axis=0)))
print("Minimum value in row {}".format(array_A.argmin(axis=1)))

sorting = np.argsort(array_A)[1]
print(array_A[..., 2])
print(np.array([1,3,3]).transpose())
print(array_A.T)
np.random.RandomState(43)
print("dot product")
print(array_A.dot(array_C))

#
# few = np.linspace(0, 1, 200)
# few2 = np.random.normal(200)
x = np.linspace(0, 1, 201)
y = np.random.random(201)
few = np.column_stack((x, y))
head = 'X-column, Y-column\n'
data1 = np.savetxt('data.xlsx', few, header=head)

load = np.loadtxt("data.xlsx")
load1 = pd.DataFrame(load)
figure, az = plt.subplots()
ax.plot(load1[0], load1[1], c='blue')
az.scatter(load1[0], load1[1], c='red')

x = np.linspace(0,1,201)
with open('BB_data.dat', 'w') as f:
    f.write('# This is the header\n')
    for data in x:
        f.write(str(data) + '\n')