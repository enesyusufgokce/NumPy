import numpy as np

a1 = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])

a2 = np.array([[11,12,13,14,15],
              [16,17,18,19,20]])

a = np.concatenate((a1, a2), axis=0)       # shape leri a1 = (2,5) ,  a2 = (2,5)
print(a)                                          # axis=0 dediğimiz için x leri yani 2 leri birleştirdi
                                                  # o yüzden 4 satır oluştu

a = np.concatenate((a1, a2), axis=1)        # y leri birleştirdi, 10 sütun oluştu
print(a)

""" aynı boyutta olmalılar. veri yeterli değilse array'a 0 ekleyip boyutları eşitle """

a = np.stack((a1, a2))      # adds a new dimension. added one more parentheses
print(a)



a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])

print(np.split(a, 4, axis=0))    # x e paralel şekilde 4 e ayır, (satır satır ayırdı)
print(np.split(a, 5, axis=1))    # y ye paralel şekilde 5 e ayır, (sütun sütun ayırdı)
