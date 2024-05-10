import numpy as np
import matplotlib.pyplot as plt

# select weights for the straight line
print("weight")
weight = np.array([[2], [3]])
print(weight)

# select intercept for the straight line
print("gamma")
gamma = np.array([[-10], [-10]])
print(gamma)

# select points
print("point")
point = np.array([[5.5, 1.5], [4.5, -1.8]])
print(point)

# determine label error
print("hat")
hat = np.dot(point, weight) + gamma
print(hat)

# assign class labels
print("label")
label = np.array([[1], [-1]])
print(label)

# check for minimum error
print("minimum error")
print(label * hat)

# calculate SVM measure
print("SVM meseaurement")
print(np.mean(weight * weight))

slope = weight[0][0]/weight[1][0]
intercept = gamma[0][0]/weight[1][0]

print("slope", slope)
print("intercept", intercept)

x = np.arange(10)
y = -intercept -slope * x

plt.plot(x, y, color="red")
plt.scatter(point[0][0], point[0][1], color="blue")
plt.scatter(point[1][0], point[1][1], color="green")
plt.show()