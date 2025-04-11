import numpy as np

a = np.array([[1,2,3],
              [4,"hello",6],
              [7,8,9]])

# tüm elemanlar aynı türden olmalı
# karışık veri varsa hepsini stringe çevirir. çünkü bir string i sayıya çeviremezsin
# ama bir sayıyı string e çevirebilirsin

print(a.dtype)
print(a[0][0].dtype)

# <U21 demesinin nedeni NumPy, her eleman için 21 karakter yer ayırmış. bu değer, dizideki en uzun
# string e ve NumPy ın iç hesaplarına göre belirleniyor

print(type(a[0][0]))


b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(type(b[0][0]))

print(type(a))


c = np.array([[1,2,3],
              [4,"5",6],
              [7,8,9]])

print(c.dtype)      # "5" değeri int e çevrilebiliyor olmasına rağmen string e çevirdi
print(type(c[0][0]))

c = np.array([[1,2,3],
              [4,"5",6],
              [7,8,9]], dtype=np.int64)     # float64 dersek ona göre sonuç verir

print(c.dtype)
print(type(c[0][0]))