import numpy as np

a = np.full((2,3,4), 9)     # numpy array filled with one value given a certain shape
print(a)

b = np.zeros((1,2,2))
print(b)

b = np.ones((1,2,2))
print(b)

c = np.empty((2,2,2,2))
print(c)

x_values = np.arange(0, 100, 5)       # 5 is the step size
print(x_values)

x_values = np.linspace(0, 100, 10)   # 10 is how many values we want to have
print(x_values)

