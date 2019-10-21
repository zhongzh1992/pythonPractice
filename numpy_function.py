import numpy as np

print("-------shape------")
a = np.array([1, 2, 3, 4, 5])
b = a[:, np.newaxis]
print(a.shape, b.shape)
print(a)
print(b)

print("-------linspace------")
x = np.linspace(0, 10, 100)
print(x)

print("-------random------")
x_train = np.random.random((2, 3))
print(x_train)

print("-------shuffle------")
list1 = [1, 2, 3, 4, 5]
np.random.shuffle(list1)  # 打乱数组顺序
print(list1)
arr = np.arange(9).reshape(3, 3)
np.random.shuffle(arr)  # 对于多维数组，只沿着第一条轴打乱顺序
print(arr)
