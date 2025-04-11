import numpy as np

a_mul = np.array([[[1,2,3, 1],
                  [4,5,6, 1],        # her listedeki eleman sayısı aynı olmak zorunda
                  [7,8,9, 1]],
                 [[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]])

print(a_mul.shape)   # shape
print(a_mul.ndim)    # dimension
print(a_mul.size)    # amount of elements
print(a_mul.dtype)