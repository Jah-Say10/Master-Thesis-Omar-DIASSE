import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 1, 2, 5, 5, 6, 1, 1, 2])
y = np.array([1, 2, 1, 5, 6, 5, 9, 10, 9])

c1 = np.array([1, 1])
c2 = np.array([1, 2])
c3 = np.array([3.42, 6.42])

def d(p1, p2):
    return np.sqrt(np.square(p2[0] - p1[0]) + np.square(p2[1] - p1[1]))

# print(d(np.array([1, 1]), np.array([4, 4])))

for i in range(len(x)):
    dt1 = d(c1, [x[i], y[i]])
    dt2 = d(c2, [x[i], y[i]])
    dt3 = d(c3, [x[i], y[i]])
    print("Distance C1, P{index} = {distance}".format(index=(i+1), distance=dt1))
    print("Distance C2, P{index} = {distance}".format(index=(i+1), distance=dt2))
    print("Distance C3, P{index} = {distance}".format(index=(i+1), distance=dt3))
    print("-----")

plt.scatter(x, y)
plt.show()
