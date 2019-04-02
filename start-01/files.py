#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

# 创建文件
open('../file/test-file.txt', 'w')

f = open('../file/test-file.txt', 'w')
print(f, f.name)
f.close()

# 删除文件
# if os.path.exists(f.name):
#     os.remove(f.name)
#     print(f'{f.name} is deleted!')
# else:
#     print(f'{f.name} is not exists!')

# 读写文件
# w 写入模式
f = open('../file/test-file.txt', 'w')
f.write('abc \ndef \nthird \n')
f.close()
# r 只读模式
f = open('../file/test-file.txt', 'r')
# s = f.read()
# print(s)
# r = f.readline().strip()
# print(r)
# r = f.readline().strip()
# print(r)
# readlines(), 返回每一行列表
l = f.readlines()
print(l)

# lines = ['1', '2', '3']
# f.writelines(lines)
# for line in f.readlines():
#     print(line)
# f.close()

# with 语句块
# with open('../file/test-file.txt', 'w') as f:
#     f.write('first \n second \n third')

# with open('../file/test-file.txt', 'r') as f:
#     for line in f.readlines():
#         print(line)

def sum_of_words(str):
    sum = 0
    for s in str:
        sum += ord(s) - 96
    return sum

with open('../file/test-file.txt', 'r') as file:
    for line in file.readlines():
        if sum_of_words(line) == 6:
            print(line)