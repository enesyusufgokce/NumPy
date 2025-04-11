import numpy as np

d = {'1': 'A'}

a = np.array([[1,2,3],
              [4,d,6],
              [7,8,"hello"]])

print(a.dtype)
print(type(a[1][0]))
# print(a[1][0].dtype)     türü object e çevirdiği için artık elemanlar birer python nesnesi olur, dtype
                           # özelliği olmaz
# type casting yapamıyorsa hepsinin type'ı object e döüşür


a = np.array([[1,2,3],
              [4,d,6],
              [7,8,"hello"]], dtype=np.str_)   # dict i zorla string e dönüştürdü "{'1': 'A'}" gibi olur

print(a.dtype)
print(type(a[1][0]))
print(a[1][0].dtype)


a = np.array([[1,2,3],
              [4,d,6],
              [7,8,"hello"]], dtype="<U7")

print(a.dtype)
print(type(a[1][0]))