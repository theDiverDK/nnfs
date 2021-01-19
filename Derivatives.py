import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2 * x ** 2


x = np.arange(0, 5, 0.001)
y = f(x)
print(x)
print(y)

print((y[1] - y[0]) / (x[1] - x[0]))
print((y[3] - y[2]) / (x[3] - x[2]))

p2_delta = 0.0001
x1 = 1
x2 = x1 + p2_delta

y1 = f(x1)
y2 = f(x2)

approximate_derivative = (y2 - y1) / (x2 - x1)
print(approximate_derivative)

plt.plot(x, y)
plt.show()
