"""
1 )、random() 返回0<=n<1之间的随机实数n；
2 )、choice(seq) 从序列seq中返回随机的元素；
3 )、getrandbits(n) 以长整型形式返回n个随机位；
4 )、shuffle(seq[, random]) 原地指定seq序列；
5 )、sample(seq, n) 从序列seq中选择n个随机且独立的元素；

"""
import numpy as np
import numpy.random as random

a1 = random.random(10)
print("a1")
print(a1)

arr = range(10)
a2 = random.choice(arr, 5)
print("a2")
print(a2)

a5 = np.random.choice(arr, 3, replace=False)
print("a5")
print(a5)

a3 = [1, 2, 3, 4, 9, 6]
print("before:")
print(a3)
a4 = random.shuffle(a3)
print("after")
print(a3)

a4 = random.sample(10)
print("a4")
print(a4)

a6 = np.random.randint(50, 100, 3)
print("a6")
print(a6)
