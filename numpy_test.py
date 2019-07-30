import numpy as np

# 创建
vector = np.array([1, 2, 3, 4])
matrix = np.array([[1, 'Tim'], [2, 'Joey'], [3, 'Frank']])

print(vector)
print(matrix)

a = np.arange(9).reshape(3, 3)
print(a)

zero = np.zeros((5, 5))
print(zero)
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
