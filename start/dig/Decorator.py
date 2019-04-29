#!/usr/bin/env python
#-*- coding: utf-8 -*-

from  IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

################## Decorator 装饰器 ##################

# 装饰器操作符 @

def a_decorator(fun):
    def warpper():
        print('doing something here:')
        fun()
        print('well done!')
    return warpper

@ a_decorator
def a_fun():
    print('I`m coding...')
a_fun()

# 装饰器作用
# 1.改变其他函数的行为
# 2.装饰器类

def uppercase(func):
    def warpper():
        result = func()
        return result.upper()
    return warpper

def adddot(func):
    def warpper():
        result = func()
        return f'{result} ..... the end'
    return warpper

def a_string():
    return 'Learning python is very interesting'
print(a_string())

@uppercase
def b_string():
    return 'Learning python is very boring'
print(b_string())

@adddot
@uppercase
def c_string():
    return 'Learning python Decorator'
print(c_string()) # LEARNING PYTHON DECORATOR ..... the end

@uppercase
@adddot
def d_string():
    return 'Learning python Decorator'
print(d_string()) # LEARNING PYTHON DECORATOR ..... THE END

# 可见多个装饰器时，执行顺序为 至下朝上 ↑, 即为由内朝外


# 装饰带有参数函数
def lowercaer(func):
    def warpper(*args):
        result = func(*args)
        return result.lower()
    return warpper

@lowercaer
def e_string(str):
    return f'writing here LOWER WORDS: {str}'
print(e_string('MY WECHAT IS ZORO'))

# 追溯 调用函数，及其传入的参数
def trace(func):
    def warpper(*args, **kwargs):
        print(f"Trace: You called function: {func.__name__}()")
        print(f"fn with args: {args} kwargs: {kwargs}")
        original_result = func(*args, **kwargs)
        print(f"Trace: {func.__name__} {args} returned: {original_result}")
        return original_result
    return warpper

@trace
def say_hi(greeting, name='ZORO'):
    return f'{greeting}, {name} Nice to meet you'
print(say_hi('Hi', name = 'John Snow'))


# 类也可以用来构建装饰器
from functools import wraps

# functools，用于高阶函数：指那些作用于函数或者返回其它函数的函数
# cmp_to_key，将一个比较函数转换关键字函数；
# partial，针对函数起作用，并且是部分的；
# reduce，与python内置的reduce函数功能一样；
# total_ordering，在类装饰器中按照缺失顺序，填充方法；
# update_wrapper，更新一个包裹（wrapper）函数，使其看起来更像被包裹（wrapped）的函数；
# wraps，可用作一个装饰器，简化调用update_wrapper的过程；

class logit(object):
    def __init__(self, logfile='../../file/logout.txt'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string, self.logfile)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass

@logit()
def logfunc():
    print('log write succeed 0.0')
logfunc()