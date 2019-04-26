# 定义一个基类
class Person(object):
    def __init__(self, name, sex, money):
        self.name = name
        self.sex = sex
        # 私有属性
        # 被引入时，继承不了，但他们的set，get函数可以继承
        self.__money = money

    def setMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def running(self):
        print('The people is running')

