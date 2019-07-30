python语言学习

基础

一、基本类型
Number:int、float、bool、complex
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
type(x)
3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
4、在混合计算时，Pyhton会把整型转换成为浮点数。


String
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
    print(r'C:\some\name')
2、字符串可以用+运算符连接在一起，用*运算符重复。
print('dog'*3)
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
arr[0] = arr[-1]
arr[1:2]

4、Python中的字符串不能改变

len()
append()

List
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
l[1:2]
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。
l[0] = 2

for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)

for f in sorted(set(basket)):
...     print(f)

Tuple
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含0或1个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
5、元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组

tup1.tuple(list1)

Set
创建一个空集合必须用 set() 而不是 { }，因为{ }是用来创建一个空字典。
集合交并差运算

Dictionaries
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用{ }
list(tel.keys())  # 返回所有key组成的list
del dict['Name'] # 删除键 'Name'
dict.clear()     # 删除字典
del dict         # 删除字典
str(dict)   #输出字典以可打印的字符串表示

for k, v in knights.items():
...     print(k, v)



二、运算符

数学运算符
x**y表示x的y次方
9//2 = 4

逻辑运算符
x and y
x or y
not x

成员运算符
in
not in

身份运算符
is
not is

三、条件控制
1、Python中用elif代替了else if，所以if语句的关键字为：if – elif – else。
2、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
3、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
4、在Python中没有switch – case语句。
5、在Python中没有do..while循环
range()函数
pass语句什么都不做

四、迭代器
it = iter(list)
next(it)
yield 的函数:每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值

五、数据结构
list
stack = list
deque

六、模块
import fibo
from fibo import fib, fib2
from modname import *
if __name__ == '__main__':

七、IO
 repr((x, y, ('spam', 'eggs')))
 print('The value of PI is approximately %5.3f.' % math.pi)
 f = open('/tmp/workfile', 'w')
 for line in f:
...     print(line, end='')
os.listdir(path)

八、对象
class MyClass:
    """一个简单的类实例"""
    i = 12345
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    def __init__(self):
    self.data = []

    def f(self):
        return 'hello world'

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

继承
class DerivedClassName(BaseClassName1):

九、标准库
网络 urllib.request
随机数 random
日期和时间   date time
since = time.time()



实战篇

1.爬虫：从一个网页爬取所要的信息

参考：https://blog.csdn.net/aaalswaaa1/article/details/81280588

2.numpy的使用
创建
获取维度
数组索引与切片
数组比较
替代值
数据类型转换
统计计算方法

3.正则表达式
