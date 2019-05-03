#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys

# print 函数各个参数
# sep=' '：接收多个参数之后，输出时，分隔符号默认为空格，' '；
# end='\n'：输出行的末尾默认是换行符号 '\n'；
# file=sys.stdout：默认的输出对象是 sys.stdout（即，用户正在使用的屏幕）……
print('Hello', 'World')
print('Hello', 'World', sep='', end='\t', file=sys.stdout, flush=False)
print('Hello', 'World', sep='~')
print('Hello', 'World', sep='\n')

# 字符串模板
name = 'zs'
age = 18
sex = 'boy'
print(f'here is a {sex}: {name} age is {age}.')

# 排序
print(sorted('abcde'))
print(sorted('abcde', reverse=True))

# 取商、余数
a, b = divmod(11, 3)
print(a, b, divmod(11, 3))
a, b = divmod(3, 11)
print(a, b)

# 幂运算
print(pow(2, 3))
# 第三个参数 x^y % z
print(pow(2, 3, 7))

# boolean类型转换
print(bool())
print(bool('zs'))
print(bool(-293))
print(bool(1 == 2))
print(bool(False))
print(bool(None))