import numpy as np

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

a1 = np.array(l1)
a2 = np.array(l2)

print(l1 * 5)      # repeat the list five times
print(a1 * 5)      # multiply each element with 5
print(l1 + l2)
#  print(l1 * l2)   error
#  print(l1 - l2)   error
#  print(l1 / l2)   error
print(a1 + a2)      # we get vector addition
print(a1 * a2)
print(a1 / a2)      # we get infinity value, because we are dividing by zero
print(a1 - a2)


b1 = np.array([1,2,3])       # shape of 1 x 3
b2 = np.array([[1],          # shape of 2 x 1
               [2]])                                     # b2 nin üstünü 1,1 ve altını da 2,1 yapsak hata
                                                         # verir çünkü hesaplamaya uygun değil
print(b1 + b2)

c = np.array([[1,2,3],
              [4,5,6]])

print(np.sqrt(c))
print(np.sin(c))
print(np.log2(c))
