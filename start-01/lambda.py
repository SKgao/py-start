#!/usr/bin/env python
#-*- coding: utf-8 -*-

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# 函数重命名
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap(1900))
year_isleap = is_leap # 函数重命名
print(id(is_leap), id(year_isleap))    # 指向相同的内存地址
print(type(is_leap), type(year_isleap)) # 相同类型


################## lambda ##################

# 很短的函数可以使用 lambda关键字
add = lambda x, y: x + y   # : 之前为参数，之后为返回值，函数为匿名函数
print(add(2, 4))

# lambda 表达式可作为函数返回值
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(100)
print(f(1))
print(f(100))

# lambda 表达式可作为函数参数
