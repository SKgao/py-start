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