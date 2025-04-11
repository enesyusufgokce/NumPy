import numpy as np

a = np.array([1,2,3])

print(np.append(a, [7,8,9]))
print(a)

# numpy, a nın kendi değerini değiştirmedi, append yapmamıza rağmen ilk değer korundu

a = np.append(a, [7,8,9])
print(a)

a = np.insert(a, 3, [4,5,6])
print(a)

print(np.delete(a, 1))
print(np.delete(a, 3))          # en son a = şu   dediğimiz değeri a olarak alıyor. immutable durum
print(np.delete(a, 4))          # 1,3,4   ler indexler


b = np.array([[1,2,3],
              [4,5,6]])

print(np.delete(b, 0, 0))      # b array inde 0. indexteki satırı(sxis is 0) sil
print(np.delete(b, 1, 0))      # b array inde 1. indexteki satırı sil
print(np.delete(b, 1, 1))      # b array inde 1. indexteki sütunu(axis is 0) sil
# siliyor, sildikten sonra oluşan matrix i yazdırıyor