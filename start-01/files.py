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
f.write('abc line\ndef line\nthird xyz\n')
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

lines = ['1', '2', '3']
f.writelines(lines)
for line in f.readlines():
    print(line)
f.close()