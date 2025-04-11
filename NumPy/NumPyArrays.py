import numpy as np

a = np.array([1,2,3,4,5])
print(a)
print(a[1])
print(a[1:])                  # notice that the elements in the list are separated by space, not comma
print(a[:-2])

a[2] = 10
print(a)


a_mul = np.array([[1,2,3],
                  [4,5,6],       # yan yana yazsan da aynı şey
                  [7,8,9]])
print(a_mul)
print(a_mul[0])
print(a_mul[0,1])