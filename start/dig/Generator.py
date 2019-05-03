#!/usr/bin/env python
#-*- coding: utf-8 -*-

################## Generator 生成器 ##################

# yield 语句
def counter(start, end):
    while start <= end:
        yield start
        start += 1

for i in counter(1, 5):
    print(i)
# yield 语句与 return 最明显的不同在于，在它之后的语句依然会被执行
# 生成器函数被 next() 调用后，执行到 yield 生成一个值返回（然后继续执行 next() 外部剩余的语句）；
# 下次再被 next() 调用的时候，从上次生成返回值的 yield 语句处继续执行

# 生成器表达式
even = (e for e in range(10) if not e % 2)
print('even::', even)
for i in even:
    print(i)

# 表达式使用 (), 即是用生成器创造的迭代器
# 表达式使用 [], 即是用生成器创造的列表
# 表达式使用 {}, 即是用生成器创造的集合
odd = [e for e in range(10, 20) if e % 2 == 1]
print('odd::', odd)
for i, v in enumerate(odd):
    print(f'{i}-{v}')

sum_of_odd = sum(s for s in range(20, 30) if s % 2)
print('sum::', sum_of_odd)

# 函数体嵌套
def a_fun():
    def b_fun():
        print('this is b fun')
    print('this is a fun')
a_fun()

def aa_fun():
    def bb_fun():
        print('this is b fun')
    print('this is a fun')
    return bb_fun()
aa_fun()