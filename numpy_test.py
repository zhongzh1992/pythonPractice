import numpy as np

# 创建
vector = np.array([1, 2, 3, 4])
matrix = np.array([[1, 'Tim'], [2, 'Joey'], [3, 'Frank']])

print(vector)
print(matrix)

a = np.arange(9).reshape(3, 3)
print(a)

print(vector)
print("reshape:--------")
print(vector.reshape(2, -1))

print("zeros")
zero = np.zeros((5, 5))
print(zero)
print("ones")
ones = np.ones(5)
print(ones)

randoms = np.random.random(5)
print(randoms)
d = np.linspace(0, 2 * np.pi, 5)
print(d)

# 获取维度
size1 = vector.shape
print(size1)
size2 = matrix.shape
print(size2)

print(matrix.size)
print(matrix.ndim)

# 文件读入
nf = np.genfromtxt("data/price.csv", dtype='U75', delimiter=",")
print(nf)

# 索引和切片
print(matrix[0][0])
print(matrix[0:1, 1])

# 比较
# m = (matrix == 5)
# print(m)

# 类型转换
fv = vector.astype(float)
print(fv)

# 统计计算方法
sum = vector.sum()
print(sum)
sum2 = a.sum(axis=1)  # 行之和
print(sum2)

# 矩阵运算
x1 = np.array([[1, 2], [3, 4]])
x2 = np.array([[5, 6], [7, 8]])
print(x1 * x2)
print(x1.dot(x2))

# where
a = np.arange(0, 100, 10)
b = np.where(a < 50)
c = np.where(a >= 50)[0]
print(a)
print(b)
print(c)

a = [1, 1, 1]
b = [0, 0, 0]
c = a + b
print("a+b=")
print(c)

a = [[1, 2, 3], [4, 5, 6]]
a = np.array(a)
b = [[1, 2], [4, 5], [3, 6]]
b = np.array(b)
# 一个（2，3）， 一个（3，2），是可以正常的矩阵相乘的
c = np.dot(a, b)
print("c=a*b:")
print(c)

# c = a * b
# result: error 不能相乘
# 注意：这里用的是array不是matrix, 如果定义为matrix则＊ 表示矩阵乘，是OK的。
# print(c)

c = np.outer(a, b)
print("outer:")
# 说明outer是a的第一个元素跟b的每一个元素相乘作为第一行，第二个元素跟b的每一个元素相乘作为第二个元素...
print(c)

arr = [1, 0, 1, 0, 1, 0, 0]
a = np.asarray(arr)
print(arr.index(1))
print(list(a).index(1))

a = [
    [
        [1, 2, 3, 2],
        [1, 2, 3, 2],
        [2, 3, 4, 1]
    ],
    [
        [1, 0, 2, 0],
        [2, 1, 2, 0],
        [2, 1, 1, 1]
    ]
]
r = np.sum(a, axis=2)
print("np.sum------------")
print(r)

r = np.amax(a, axis=2)
print("np.amax------------")
print(r)

a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print('我们的数组是：')
print(a)
print('\n')
print('调用 amin() 函数：')
print(np.amin(a, 1))
print('\n')
print('再次调用 amin() 函数：')
print(np.amin(a, 0))
print('\n')
print('调用 amax() 函数：')
print(np.amax(a))
print('\n')
print('再次调用 amax() 函数：')
print(np.amax(a, axis=0))
