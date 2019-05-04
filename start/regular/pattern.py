#!/usr/bin/env python
#-*- coding: utf-8 -*-

# from  IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = 'all'
import re

################## 正则表达式 ##################

str = 'The quick brown fox jumps over the lazy dog'
pttn = re.compile(r'\wo\w')
result = re.findall(pttn, str)
print(result)