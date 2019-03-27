# 数据容器 container
# 包括字符串 string、 range()生成的等差数列、列表List、元组Tuple、集合Set、字典Dictionary。
# 其中分为可变容器与不可变容器
# 可变容器：列表、Set、字典
# 不可变容器：字符串、range()、元组、Frozen Set
# 集合Set 分为Set与Frozen Set，另集合中无重复元素

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
import random

######################################################################
# 列表 List
# 可变有序容器， 用 [] 标识

a_list = []
b_list = [1, 2, 3]
a_list.append('a')
a_list.append('b')
print(a_list)
b_list = list(range(8))
b_list.append(11)
print(b_list)
c_list = [2**x for x in range(8)]
print(c_list)

n = 10
a_list = [random.randrange(1, 100) for i in range(n)]
print(a_list)
b_list = [x for x in a_list if x % 2 == 0]
print(b_list)

# 列表操作符
# 拼接 +
# 复制 *
# 逻辑运算 in, not in, <, <=, >, >=, ==, !=
a_list = [1, 2, 3]
b_list = [4, 5, 6]
c_list = a_list + b_list * 3
print(c_list)
print(7 not in c_list)
print(a_list > b_list)

# 根据索引提取数组
c_list = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
print(c_list[3])        # 返回索引值为 3 的元素值
print(c_list[:])        # 返回整个列表
print(c_list[5:])       # 从索引为 5 的值开始直到末尾
print(c_list[:3])       # 从索引 0 开始，直到索引 3 之前（不包括 3）
print(c_list[2:6])      # 从索引 2 开始，直到索引 6 之前（不包括 6）

# 根据索引删除
del c_list[3]
print(c_list)
del c_list[7]
print(c_list)

# 根据索引替换
# s[start:stop:step] = t，跟 range 的三个参数类似；
c_list[1:6:2] = ['a', 'b', 'c']
print(c_list)

# 可用内建函数 len(), max(), min()
n = 4
a_list = [random.randrange(65, 91) for i in range(n)]
b_list = [chr(random.randrange(65, 91)) for i in range(n)]
print(a_list)
print(b_list)
print(len(a_list), max(b_list), min(a_list))

# sort() 排序, 列表必须是同一种数据类型元素构成
n = 10
a_list = [random.randrange(1, 100) for i in range(n)]
print(a_list)
a_list.sort()
print(a_list)
a_list.sort(reverse = True) # 倒序
print(a_list)
# b_list = [1, 2, 'a', 'b'] # not supported between instances of 'str' and 'int'
# b_list.sort()
# print(b_list)
n = 3
a_list = [random.randrange(65, 91) for i in range(n)]
b_list = [chr(random.randrange(65, 91)) for i in range(n)]
c_list = a_list + b_list + a_list * 2
print(a_list, '\n', b_list, '\n', c_list)

# append() 同js
c_list.append('1')
print(c_list)

# clear() 清空序列
a_list.clear() # 同 a_list = []
print(a_list)

# copy() 复制列表，不会影响到原列表
d_list = c_list.copy()
print(d_list)
del d_list[2:5]
print(d_list, '\n', c_list)

# extend() 再末尾追加列表，同js concat()
d_list.extend(b_list)
print(d_list)

# insert() 指定位置插入
b_list.insert(3, 'xyz')
print(b_list)

# reverse() 倒序，同js
b_list.reverse()
print(b_list)

# pop() 指定索引删除
a_list = [1, 242, 'vw', 'vh', 't']
a_list.pop(0)
print(a_list)

# remove() 指定元素删除
a_list.remove('t')
print(a_list)



######################################################################
# 元组 Tuple
# 不可变有序容器， 用 () 标识

a = 1, 2, 3  # 创建元组可省略括号 (不推荐)
b = (1, 2, 3)
print(a, b, a == b)

# 创建单个元素的元组，无论是否使用圆括号，在那唯一的元素后面一定要补上一个逗号 ,
c = 2   # 不是元组，是int
print(c, type(c))
cc = 2,
print(cc, type(cc))
d = (2)  # 不是元组，是int
print(d, type(d))
dd = (2,)
print(dd, type(dd))

a = (1,)
print(a, id(a))
# 用 + 向元组中追加元素
a += (3, 5)
print(a, id(a))

a = range(10)
b = tuple(a) # 转为元组
c = list(a)  # 转为列表
print(a, b, c)



######################################################################
# 集合 Set
# 不包含重合元素，并且是无序的， 用 {} 标识

# 创建集合
a = {2, 3, 4, 5, 6}
print(a)
b = {}  # 注意这样创建的是一个 dict（字典），而不是 set 集合
print(b, type(b))
bb = set() # 使用set(), 创建空集合
print(b, type(bb))

# 用set() 去重
a = 'abcabcdeabcdbcdef'
b = range(10)
c = [1, 2, 2, 3, 3, 1]
d = ('a', 'b', 'e', 'b', 'a')
print(set(a), '\n', set(b), '\n', set(c), '\n', set(d))

# 过滤
e = {x for x in a if x not in 'abc'}
print(e, 'e' in e)

# 内置函数 in 判断存在
# copy(), max(), min(), len() 同列表
a = {22, 22, 3, 3, 4, 5, 0, 0, 0, 1}
b = a.copy()
print(b, '\n', max(a), '\n', min(a), '\n', len(a))

# 使用 remove() 删除set中的元素， Frozen Set无法删除元素
b.remove(22)
print(b)


# 并集 | ，交集 & ， 差集 - ， 对称差集 ^
admins = {'Moose', 'Joker', 'Joker'}
members = {'Ann', 'Chris', 'Jane', 'Moose', 'Zero'}
print('Joker' in admins)
print(admins | members) # 并集，两者中所有的元素
print(admins & members) # 交集，领着中都有的元素
print(admins - members) # 差集，前者中存在并且后者总不存在
print(admins ^ members) # 对称差集，不是同时存在两者中的，交集的反面

# 内置方法同上
print(admins.union(members)) # 并集
print(admins.intersection(members)) # 交集
print(admins.difference(members)) # 差集
print(admins.symmetric_difference(members)) # 对称差集

# 逻辑运算
a = {1, 2, 3}
b = {1, 1, 2, 2, 3}
c = {1, 2, 3, 4}
d = {4, 5, 6}
print(a == b)
print(a != c)
print(a.isdisjoint(d), a & d == set()) # a 与 d 完全不重合
print(a.isdisjoint(c))
print(a.issubset(c), a <= c)    # a 是 c 的子集
print(a < c, a < b)             # a 是 c 的真子集
print(c.issuperset(a), c >= a)  # c 是 a 的超集
print(c > a, b > a)             # c 是 a 的真超集

# 集合方法
# add(), remove(), pop(), clear() 增删
x = {'a', 'b', 'c'}
y = {'c', 'd', 'e'}
z = {'f', 'g', 'c'}

# add() 添加到集合中，如果元素已存在，则不进行任何操作
x.add('c')
print(x)
x.add(1)
print(x)
# update() 参数可以是列表，元组，字典等
x.update(y)
print(x)

# intersection_update() 计算交集
x.intersection_update(z)
print(x)

# difference_update() 移除两个集合中都存在的元素
y.difference_update(z)
print(y)



######################################################################
# 字典 Dictionary

phonebook = {'ann': 6575, 'bob': 8982, 'joe': 2598, 'zoe': 1225, 'ann': 6585}
print(phonebook, phonebook['ann'])
phonebook['bob'] = 'bbbb'
print(phonebook)

# 添加元素
p1 = {'ann': 6575, 'bob': 8982}
p2 = {'zoe': 1225, 'joe': 2598}
p1.update(p2)
print(p1)

# 删除元素
del p1['ann']
print(p1)

# 逻辑操作符
p = {'ann': 6575, 'bob': 8982, 'zoe': 1225, 'joe': 2598}
print('ann' in p)
print(p.keys(), 'ann' in p.keys())
print(p.values(), 6575 in p.values())
print(p.items(), ('ann', 6575) in p.items())

# 内建函数
print(len(p))
print(max(p))
print(min(p))
print(list(p))
print(tuple(p))
print(set(p))
print(sorted(p))
print(sorted(p, reverse = True))

# 方法
o = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# setdefault(),  key不存在，设置默认值
o.setdefault('sex', None)
print(o)
# pop(), 删除指定键
o.pop('sex')
print(o)
# popitem(), 随机返回并删除字典中的一对键和值(一般删除末尾对)
o.popitem()
print(o)