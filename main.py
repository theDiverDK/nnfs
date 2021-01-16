import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]
           ]
bias = [2.0, 3.0, 0.5]

output = np.dot(weights, inputs) + bias
print(output)

print('---')

a = [1, 2, 3]
print(np.array(a))
print(np.array([a]))
print(np.expand_dims(np.array(a), axis=0))

print('---')

b = [2, 3, 4]

a = np.array([a])
b = np.array([b]).T

print(a, b)
print(np.dot(a, b))
print('---')