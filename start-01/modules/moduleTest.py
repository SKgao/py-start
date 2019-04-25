#!/usr/bin/env python
#-*- coding: utf-8 -*-
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

################## Module 模块 ##################

# 导入内建模块
import sys
# 导入本地模块
import utils

print(sys.path) # 模块路径
module_names = sys.builtin_module_names # 获取系统内建模块的列表
print(module_names, '_io' in module_names, 'gc' in module_names)

print(utils.__name__)
print('utils.is_prime:', utils.is_prime(7))
print('utils.is_leap:', utils.is_leap(1900))

# dir() 函数，查看模块中可触达的变量名称和函数名称
print('utils_dir::', dir(utils))


# 导入模块中指定函数
from utils import is_leap
print('is_leap:', is_leap(2000))

# 导入模块中所有内容
from utils import *
print('is_prime:', is_prime(17))

# 导入并指定别名
from utils import is_leap as leap_year
print('is_leap alias:', leap_year(2004))

# 模块中的非函数部分的可执行代码，只执行一次
import this

# this 模块导入即执行一次
print(this.d) # 访问模块中变量
print(this.s)

love = this
print(this is love)
print(love is True)
print(love is False)
print(love is not True or False)
print(id(this), id(love))
print(id(True), id(False))

# 不会自动执行
import that
that.main()