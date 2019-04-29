#!/usr/bin/env python
#-*- coding: utf-8 -*-
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# 定义类 class关键字
class One(object):  # object 代表所有类的基类，也叫作超类
    # 类变量
    x = 1
    y = 2

def __init__(self, name, age):  # 类的初始化
    self.name = name
    self.age = age

def func(self):
    z = 'zoro'
    print(f'hello {z}~')

one = One()  # 穿件对象，类的实例化


# 类的封装
class Student(object):
    def __init__(self, name, score):
        # 属性前面带 __ 代表为类的私有属性，外部无法访问
        self.__name = name
        self.__score = score
        self.publicName = name

    def getInfo(self):
        print(f'name is {self.__name}, score is {self.__score}')

    def getScore(self):
        print(f'my score is {self.__score}')

    def setScore(self, score):
        self.__score = score

zoro = Student('zoro', 80)
zoro.getInfo()
zoro.getScore()
zoro.setScore(95)
zoro.getScore()
print(zoro.publicName)



# 引入Person基类
from person import Person

# 单继承Person类
class Worker(Person):
    def __init__(self, name, sex, height, money):
        # super关键字来调用父类的中相应的方法
        # super()调用父类的 __init__(), 初始化并传参
        super(Worker, self).__init__(name, sex, money) # 让父类的self当做子类的对象
        self.height = height

aleen = Worker('zoo', 'boy', 180, '50w')
print(aleen.getMoney())
aleen.running()
aleen.setMoney('100w')
print(aleen.name, aleen.sex, aleen.height, aleen.getMoney())

# 引入类
from parents import Father
from parents import Mother

# 多继承
class Child(Father, Mother):
    def __init__(self, house, sister, age):
        # 多继承时调用父类的属性
        Father.__init__(self, house)
        Mother.__init__(self, sister)
        self.age = age
        Child.attrtest = 'exist'

bob = Child('PuDong', 'sun', 7)
print(bob.getHouse())
print(bob.myFather(), bob.myMother(), bob.getSister())
bob.setHouse('WuHan')
print(bob.getHouse(), bob.age)
# mro列表就是一个简单的所有基类的线性顺序列表(相当于原型链)
print('mro---->', Child.__mro__)
# 查看类上的所有方法 接口
help(Child)
print('dict--->', Child.__dict__)
print('dir---->', dir(Child))

# hasattr, getattr, setattr
print(hasattr(Child, 'getHouse'))
print(getattr(Child, 'attrtest'))
print(setattr(Child, 'attrtest', 'not exist!'))
print(getattr(Child, 'attrtest'))


# 多态
# 多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。
class Animal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        pass

    def runAnimal(self):
        self.run()

class Dog(Animal):
    def run(self):
        print('Dog is runing')

class Cat(Animal):
    def run(self):
        print('Cat is runing')
dog = Dog('ddd')
cat = Cat('ccc')
Animal.runAnimal(dog)
Animal.runAnimal(cat)
print(dog.name, cat.name)

# 处理时间库
import datetime
import time
print('now', time.time())
print('year', datetime.date.today().year)

class Golem:
    __population = 0
    __life_span = 10

    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.__population += 1

    def say_hi(self):
        print('Hi!')

    def cease(self):
        self.__active = False
        Golem.__population -= 1

    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem.__life_span:
            self.cease
        return self.__active

    @property
    def population(self):
        return Golem.__population

    @population.setter
    def population(self, value):
        Golem.__population = value

g = Golem('Clay')
print(g.population)
g.population = 100
print(g.population)
print(g.is_active())