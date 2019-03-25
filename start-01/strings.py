from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# 数字精度损失
print(1.1 + 2.2)

# 字符的 unicode编码
print(ord('a'))
print(chr(98))
print(ord('高'))
print(chr(24605))

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