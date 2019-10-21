# 切片[起点：终点：步长]
arr = [1, 2, 3, 4, 5, 6]

print(arr[1:5:2])
print(arr[::-1])

# list遍历1：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# map遍历
for k, v in {'cat': 10, 'dog': 2}.items():
    print(k, v)

# id()
a = 1
print(id(a))
a = 3
print(id(a))

b = [1, 2, 3]
print(id(b))
b[1] = 0
print(id(b))

# isInstance()
c = 2
print(isinstance(c, int))

# range(5,0,-1)
for i in range(5, 0, -1):
    print(i)

wlist = [w for w in range(5)]
print(wlist)

# time
import time

since = time.time()
cnt = 0
for j in range(1000000):
    cnt += j
after = time.time()
print("cost:%f" % (after - since))

# str
print(str([1, 2, 3, 4, 5, 6, 7, 8]))
print(str({'cat': 10, 'dog': 2}))
print("abc".startswith('ab'))

aList = [123, 'xyz', 'runoob', 'abc']
print ("xyz 索引位置: ", aList.index('xyz'))
print("runoob 索引位置 : ", aList.index('runoob', 1, 3))
