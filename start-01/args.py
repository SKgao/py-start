#!/usr/bin/env python
#-*- coding: utf-8 -*-

from  IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# py中关键字
import keyword
print(keyword.kwlist)
print('None' in keyword.kwlist)
print(keyword.iskeyword('if'))

# 无参数、无return语句的函数
def do_nothing():
    print('done!')

# 无return语句，默认函数返回None 相当于是 False
if not do_nothing():
    print('no return')

# 传参函数
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap(2000))

# 可以接受一系列参数 *
def say_hi(*names):
    for n in names:
        print(f'hi {n}~')
say_hi()  # 未传参时 for in 语句 return False 所以不会执行
say_hi('zs_3', 'zs_4', 'zs_5')

names = ('ls_1', 'li_2', 'li_3')
say_hi(*names) # 可以传入容器为函数参数

a_sting = 'Python'
say_hi(*a_sting) # 传入迭代字符串

a_range = range(10)
say_hi(*a_range) # 传入 range

a_list = list(a_range)
say_hi(*a_list) #  传入 list

# 参数预设值
def say_hi(greeting, *names, capitalized=True):
    for n in names:
        if capitalized:
            n = n.capitalize()
        print(f'{greeting}, {n}')
a_list = ['Gs_1', 'gs_2', 'gS_3']
say_hi('Hello', *a_list)

# 接收一系列值的关键字参数
def say_hi(**greeting_names):
    for names, greeting in greeting_names.items():
        print(f'{greeting}, {names}~')
say_hi(mike="hello", john="hi")

a_dictionary = {'mike': 'hello', 'john': 'hi'}
say_hi(**a_dictionary)