# 数据容器 container
# 包括字符串 string、 range()生成的等差数列、列表List、元组Tuple、集合Set、字典Dictionary。
# 其中分为可变容器与不可变容器
# 可变容器：列表、Set、字典
# 不可变容器：字符串、range()、元组、Frozen Set
# 集合Set 分为Set与Frozen Set，另集合中无重复元素

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
import random

# 列表 List
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