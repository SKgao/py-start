#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random
r = random.randrange(1, 100)

# if 流程控制
if r % 2 == 0:
    print(r, 'is even')
else:
    print(r, 'is odd')


# for 循环
for i in range(10):
    if i % 2 == 1:
        print(i, 'is odd')


# 输出质数
for m in range(2, 100):
    if m == 2:
        print('质数：', m)
        continue
    for n in range(2, m):
        if m % n == 0:
            break
    else:
        print('质数：', m)

# 输出质数 (优化)
for s in range(2, 100):
    if s == 2:
        print('质数：', s)
        continue
    for t in range(2, int(s ** 0.5) + 1):
        if s % t == 0:
            break
    else:
        print('质数：', s)

# 绝对值
a = abs(-3.1415926)
print(a)


# 定义函数
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n ** 0.5) + 1):
        if n % m == 0:
            return False
    else:
        return True

# 函数调用
for x in range(1, 20):
    if is_prime(x):
        print(x)