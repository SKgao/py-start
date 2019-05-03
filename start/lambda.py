#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random

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
def double_it(n):
    return n * 2

a_list = [1, 2, 3, 4, 4, 6]
print(list(map(double_it, a_list)))
print(list(map(lambda x: x *2, a_list))) # map() 方法，传入函数，可迭代对象

phonebook = [
    {
        'name': 'john',
        'phone': 9876
    },
    {
        'name': 'mike',
        'phone': 5603
    },
    {
        'name': 'stan',
        'phone': 6898
    },
    {
        'name': 'eric',
        'phone': 7898
    }
]
print(list(map(lambda x: x['name'], phonebook)))

a_list = [1, 2, 3]
b_list = [4, 5, 6]
print(list(map(lambda x, y: x * y, a_list, b_list)))  # map() 可以传多个可迭代对象

paris = [(2, 'two'), (4, 'four'), (3, 'three'), (1, 'one'), (5, 'five')]
paris.sort(key=lambda p: p[0], reverse=True)
print(paris, (2, 'two')[0])

# sort()
# cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）


################## 递归 ##################

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n -1)
print(factorial(5))

print(not random.randrange(0, 2))

def in_dream(day=0, deal=False, kick=False):
    deal = not random.randrange(0, 5)
    kick = not random.randrange(0, 10)
    day += 1
    if deal:
        print(f'I sleep {day} days, weaked by deal!')
        return day
    elif kick:
        print(f'I sleep {day} days, weaked by kick!')
        return day
    else:
        return in_dream(day)
print(in_dream())


################## Docstring (函数文档) ##################

# 必须在函数定义的内部语句块的开头，与其它语句一样保持相应的缩进(Indention)
# 1. 无论是单行还是多行的 Docstring，一概使用三个双引号扩起；
# 2. 在 Docstring 内部，文字开始之前，以及文字结束之后，都不要有空行；
# 3. 多行 Docstring，第一行是概要，随后空一行，再写其它部分；
# 4. 完善的 Docstring，应该概括清楚以下内容：参数、返回值、可能触发的错误类型、可能的副作用，以及函数的使用限制等等；
# 5. 每个参数的说明都使用单独的一行
def max_num(a, b):
    """
    Return two number who is max
    :type a: int
    :type b: int
    :rtype: int
    """
    return a if a > b else b
print(max_num.__doc__, max_num(2, 3))