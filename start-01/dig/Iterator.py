#!/usr/bin/env python
#-*- coding: utf-8 -*-

from  IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

################## Iterator 迭代器 ##################

# Python 中所有可迭代元素，都有Iterator。 如所有的容器

string = 'I write javascript'
alist = ['a', 'b', 123,  'xx', 'zyz']
aset = ('aa', 'ba', 456, 'aa', 1, 1)

for i in string:
    print(i, end=',')
print()

for l in alist:
    print(l, end=',')
print()

for s in set(aset):
    print(s, end=',')
print()


# 使用内建函数，就是用来把一个 '可迭代对象'(Iterable)转换成 '迭代器'(Iterator) 的函数 iter()

s = iter('Python!')
print(type(s))
t = iter((1, 2, 3, 4))
print(type(t))
l = iter(['a', 'b', 'c', 'd'])
print(type(l))

# next() 函数
s = iter('Python')
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
# print(next(s)) # 迭代完成，再被调用，会触发 StopIteration 错误

class Counter(object):
    def __init__(self, start, end):
        self.current = start
        self.stop = end

    # __iter__，Counter 这个类就被会被识别为 Iterator 类型
    def __iter__(self):
        return self

    # __next__， 完整迭代器， 可做遍历
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration  # 可以通过raise显示地引发异常
        else:
            c = self.current
            self.current += 1
        return c

c = Counter(10, 13)
print(next(c))
print(next(c))
print(next(c))
print(type(Counter))

for c in Counter(100, 105):
    print(c)

c = Counter(201, 205)
while True:
    try:
        print(next(c), sep=',')
    except StopIteration:
        break
