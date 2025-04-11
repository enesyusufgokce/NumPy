import numpy as np

a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])

print(a.shape)     # four lists and five elements
print(a.reshape((5,4)))        # the order is the same (1,2,3,4,5,6,7,8,9...)
print(a.reshape(20))
print(a.reshape(20, 1))
print(a.reshape(2,2,5))

a.reshape(5,4)           # we need to assign in order to change the array
print(a)

a = a.reshape(5,4)
print(a)

a.resize(2,10)           # resize fonksiyonunun işlemesi için assign etmemize gerek yok
print(a)                 # apply the transformation on the array without returning.
                         # we don't have to return it and store it

print(a.flatten())       # the different is flatten returns the copy of array,
print(a.ravel())         # ravel only returns the same array with a flattened view on it

var1 = a.flatten()
var1[2] = 100
print(var1)          # array ın kopyasını oluşturdu, o kopyadaki 2. indexi 100 olarak değiştirdi
print(a)             # original array is not changed

var2 = a.ravel()
var2[2] = 100
print(var2)          # it changed the original value because we are not returning a copy
print(a)             # original array is changed now



a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])

print(a.transpose())
print(a.T)                # transpose demek bu da

print(a.swapaxes(0,1))      # if we have a high dimensional array, we may be just want to swap
                                     # two axes. but transposing swaps everything