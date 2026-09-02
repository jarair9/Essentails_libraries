import numpy as np


x = np.array([10, 20, 30, 40, 50])
y = np.array([1, 2, 3, 4, 5])


print(x + y)
print(x - y)
print(x * y)
print(np.dot(x, y))  # 10*1 + 20*2 + 30*3 + 40*4 + 50*5 = 550
print(x / y)
print(x % y)
print(x ** 2)  # square each element in x
