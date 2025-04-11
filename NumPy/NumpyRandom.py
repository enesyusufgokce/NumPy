import numpy as np

number = np.random.randint(100)
print(number)

numbers = np.random.randint(100, size=(2,3,4))
print(numbers)

numbers = np.random.randint(1, size=(2,3,4))
print(numbers)

numbers = np.random.randint(2, size=(2,3,4))
print(numbers)

numbers = np.random.randint(90, 100, size=(2,3,4))
print(numbers)

numbers = np.random.binomial(10, p=0.5, size=(5, 10))
print(numbers)

numbers = np.random.normal(170, scale=15, size=(5, 10))
print(numbers)

numbers = np.random.choice([10,20,30,40,50])
print(numbers)

numbers = np.random.choice([10,20,30,40,50], size=(4,6))
print(numbers)
