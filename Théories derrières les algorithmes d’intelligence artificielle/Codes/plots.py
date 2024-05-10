import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([.1, 6.9, 7.2, 20, 28, 32, 53, 62, 78, 104.5])
w = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
# w = np.array([9, 18, 27, 36, 45, 54, 63, 72, 81, 90])

plt.scatter(x, y)
plt.plot(x, w, color="red")
plt.show()