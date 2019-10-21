#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：数据集按比例切分为训练集和测试集
时间：2017年3月11日 12:48:57
"""
import numpy as np
from sklearn.model_selection import train_test_split

# from sklearn.cross_validation import train_test_split

# 生成200个句子，前100个和后100个类别分别对应1和2
X = [[u"这是", u"第1个", u"测试"]] * 100 + [[u"这是", u"第2个", u"测试"]] * 100
y = [1] * 100 + [2] * 100

# 随机抽取20%的测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(len(X_train), len(X_test))

# 查看句子和标签是否仍然对应
for i in range(len(X_test)):
    print("".join(X_test[i]), y_test[i])

if __name__ == "__main__":
    X, y = np.arange(10).reshape((5, 2)), range
    X = np.array([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]])
    y = [0, 1, 2, 3, 4]
    print(X)
    print(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
    print(X_train)
    print(y_train)
    print(X_test)
    print(y_test)
