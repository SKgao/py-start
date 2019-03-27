#!/usr/bin/env python
#-*- coding: utf-8 -*-
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# 数字精度损失
print(1.1 + 2.2)

# 字符的 unicode编码
print(ord('a')) # 97
print(chr(98))  # b
print(ord('高'))
print(chr(24605)) # 思

# 字符串格式
print('This is a String 01.')
print("This is a String 02.")
print(
    '''
        This is a String 03.
        This is a String 04.
    '''
)

# 数字字符串类型转换
print(int('3'))
print(float('3.35'))
print(str(3.3565))

# input输入
# age = input('Please enter your age: an int number, e.g: 22')
# if int(age) > 18:
#     print('you are a man!')
# else:
#     print('you are youth!')

# 转义字符 \
print('wow, it\'s a cute dog~')


# 字符串操作
# 字符串拼接
print('my' + ' ' + 'name is' + '..')
# 字符串repate
print('abc' * 3)
print('123' * 3)
# 字符串查找
print('o' in 'hello~')
# 字符串循环
s = 'python'
for char in s:
    print(char, s.index(char))

for j in range(len(s)):
    print(s[j])

# s[index] —— 返回索引值为 index 的那个字符
# s[start:] —— 返回从索引值为 start 开始一直到字符串末尾的所有字符
# s[start:stop] —— 返回从索引值为 start 开始一直到索引值为 stop 的那个字符之前的所有字符
# s[:stop] —— 返回从字符串开头一直到索引值为 stop 的那个字符之前的所有字符
# s[start:stop:step] —— 返回从索引值为 start 开始一直到索引值为 stop 的那个字符之前的，以 step 为步长提取的所有字符
print(s[1])
print(s[2:])
print(s[2:5])
print(s[:4])
print(s[1:5:3])
print(s[1:6:1])


# 字符串处理
print(s.upper())
print('ABCD'.lower())
# print('\u0132'.casefold())
t = 'here is my workspace.'
print(t.capitalize()) # 首字母大写
print(t.title()) # 每个单词首字母大写
print(t.swapcase()) # 逐个字母替换大小写
print(t.title().swapcase())
ch = '中文'
print(ch.encode()) # 中文转码


# 字符串搜索、替换
s = 'Simple is better than complex. Simple is better~ Simple!'
# count 指定字符串出现的次数 [start, end] 分别代表起始、截止位置
print(s.lower().count('si'))
print(s.lower().count('si', 10))
print(s.lower().count('si', 10, 40))
# find 指定字符串首次出现的位置，未找到返回-1
print(s.lower().find('imple'))
print(s.lower().find('simple', 30))
print(s.lower().find('is', 15, 20))
# rfind 指定字符串最后出现的位置，未找到返回-1
print(s.lower().rfind('imple'))
print(s.lower().rfind('simple', 10, 40))
print(s.lower().rfind('simple', 0, 10))
# index() 与 find() 相同，但如果没找到的话，会触发 ValueError 异常
print(s.lower().index('imple'))
# print(s.lower().index('www'))
# rindex() 与 rfind() 相同，但如果没找到的话，会触发 ValueError 异常
print(s.lower().rindex('imple'))
# print(s.lower().rindex('www'))

# startswith(), endswith() 判断起始、终止字符
print(s.lower().startswith('S'))
print(s.lower().startswith('simple'))
print(s.lower().startswith('simple', 1))
print(s.lower().startswith('b', 10))
print(s.lower().endswith('!'))
print(s.lower().endswith('.', 10, 30))
print(s.lower().endswith('!', 10, 20))
print(s.lower().endswith('!', 10))

# 查找是否存在字符 in
print('better' in s)

# 字符串替换 [, count]可选参数，指替换次数
t = 'abcdaefgaa'
print(t.replace('a', 'A'))
print(t.replace('a', 'A', 1))
print(t.replace('a', 'A', 3))
# expandtabs() 替换制表符 \t， 默认替换为8个空格
t = 'abac\tqwer\txyz\t.'
print(t.expandtabs())
print(t.expandtabs(2))

# 去除子串
# strip() 去除首位空白，包括空格、\t、\n 等
t = '\t  Simple is better than complex. \n \t '
s = 'Simple is better than complex.'
print(t.strip())
print(s.strip('Six.p'))
print(s.strip('pSix.mle'))
# lstrip()只对左侧处理，只对右侧处理 rstrip()
print(s.lstrip('Six.p'))
print(s.lstrip('pSix.mle'))
print(s.rstrip('Six.p'))
print(s.rstrip('pSix.mle'))

# 字符串拆分
# splitlines() 拆分为一个列表, 默认替换 \n
s = '''Name,Age,Location
John,18,New York
Mike,22,San Francisco
Janny,25,Miami
Sunny,21,Shanghai'''
print(s.splitlines())
# split()  sep参数指定规则分隔, maxsplit可选参数，指分隔次数，默认=-1即全部拆分
t = 'Mike,22,San Francisco'
print(t.split(','))
print(t.split(sep = ',')) # 跟上面一毛一样
print(t.split(',', maxsplit = 1))
print(t.split(',', maxsplit = 0)) # =0 即不拆分

# 字符串拼接
# join() 竟然可传入数组跟字符串(⊙o⊙)…
s = '-'
q = ''
t = ['p', 'y', 't', 'h', 'o', 'n', '!']
print(s.join(t))
print(q.join('(⊙o⊙)…'))

# 字符串排版
# center() 居中，若指定宽度小于字符串长度，返回原字符串
s = 'abcxyz'
print(s.title().center(10))
print(s.swapcase().center(20))
print(s.center(20, '-'))
# 同理 ljust()左对齐， rjust()又对齐
print(s.lower().ljust(10, '.'))
print(s.upper().rjust(10, '~'))
# zfill()将左侧，由0填充指定长度字符串
for i in range(1, 12):
    filename = str(i).zfill(3) + '.mp3'
    print(filename)

# format() 插入一个或者多个占位符， 用大括号 {} 括起来
name = 'zs'
sex = 'boy'
age = 20
print('{} is a {}, age is {}'.format(name, sex, age))
print('{} is youth ? {}'.format(name, age <= 18))
print('{1} years old is {0}'.format(name, age))
# f-string 同上，字符串模板
print(f'{name} is a {sex}, age is {age}')
print(f'{name} is youth ? {age <= 18}')

# 字符串判断
print('123abc'.isalnum())  # 是否由字母和数字组成
print('123456'.isdigit())  # 是否只由数字组成
print('abcdef'.isalpha())  # 否只由字母组成
print('abcdef'.islower())  # 是否由小写字母组成
print('ABCDEF'.isupper())  # 是否由大写字母组成
print('      '.isspace())  # 是否只由空格组成
print('This Is String!'.istitle())  # 首字母是否为大写，且其他字母为小写
print('a'.isascii())       # 是否为Ascii码字符