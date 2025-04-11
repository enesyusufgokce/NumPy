import numpy as np

a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])

np.save("myarray.npy", a)           # dosya uzantısını npy yap. sen yapmazsan otomatik kendi yapıyor
b = np.load("myarray.npy")

print(b)


np.savetxt("myarray.csv", a, delimiter=",")      # the file is comma seperated values file
b = np.loadtxt("myarray.csv", delimiter=",")

print(b)
